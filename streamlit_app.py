# -- coding: utf-8 --
"""chatbot_streamlit.py"""

import os
import streamlit as st
from io import BytesIO
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.document_loaders import PyPDFLoader

# Set OpenAI API key securely using Streamlit secrets
os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]

# Streamlit UI
st.title("ACM GIKI Chapter Chatbot")
st.markdown("Ask any question about the ACM society, and I'll provide the most accurate answer based on the document!")

# Upload PDF
uploaded_file = st.file_uploader("Upload the ACM society document (PDF):", type="pdf")
if uploaded_file is not None:
    with st.spinner("Loading and splitting the PDF..."):
        # Read the uploaded file into memory
        pdf_data = uploaded_file.read()

        # Load the PDF from the in-memory data
        loader = PyPDFLoader(BytesIO(pdf_data))
        pages = loader.load_and_split()

    # Initialize OpenAI embeddings
    embeddings = OpenAIEmbeddings(model="text-embedding-ada-002")
    faiss_index = FAISS.from_documents(pages, embeddings)

    # Initialize the LLM
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.8)

    # Function to answer questions
    def answer_question(llm, user_question):
        # Perform similarity search
        docs = faiss_index.similarity_search(user_question, k=5)
        context = "\n\n".join([doc.page_content for doc in docs])

        # Define the prompt for the LLM
        prompt = ChatPromptTemplate.from_messages(
            [
                ("system", '''
                This is the data for GIKI ACM CHAPTER. Following is the document for most commonly asked questions about the ACM society.
                If someone asks any question, answer them according to these chunks of the data:

                {context}

                Answer in this format:
                Final Answer: <answer to the user question>
                '''),
                ("human", "{input}")
            ]
        )

        # Generate response
        chain = prompt | llm
        response = chain.invoke(
            {
                "context": context,
                "input": user_question
            }
        )
        output = response.content

        # Extract final answer
        def extract_final_answer(output):
            start_marker = "Final Answer: "
            start_index = output.find(start_marker)
            return output[start_index + len(start_marker):].strip() if start_index != -1 else "Sorry, I couldn't find a clear answer."

        return extract_final_answer(output)

    # User input
    user_question = st.text_input("Enter your query:")
    if user_question:
        with st.spinner("Generating response..."):
            try:
                response = answer_question(llm, user_question)
                st.success("Here's the response:")
                st.write(response)
            except Exception as e:
                st.error(f"An error occurred: {e}")
else:
    st.info("Please upload a PDF to proceed.")
