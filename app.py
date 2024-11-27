# -- coding: utf-8 --
"""chatbot_streamlit.py"""

import os
import streamlit as st
from langchain_community.embeddings.sentence_transformer import SentenceTransformerEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.document_loaders import PyPDFLoader

# Set OpenAI API key securely using Streamlit secrets

!python -c "from huggingface_hub.hf_api import HfFolder; HfFolder.save_token('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')"
os.environ["OPENAI_API_KEY"] = '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'
# Load the PDF and preprocess
loader = PyPDFLoader("chat_bot_sponser_data.pdf")  # Replace with correct path to PDF
pages = loader.load_and_split()

# Initialize the LLM
llm = ChatOpenAI(model="gpt-4", temperature=0.8)

# Function to answer questions based on the provided PDF
def answer_question(llm, user_question):
    # Create FAISS index
    faiss_index = FAISS.from_documents(pages, OpenAIEmbeddings())
    docs = faiss_index.similarity_search(user_question, k=5)

    # Define the prompt for the LLM
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", '''
            This is the data for GIKI ACM CHAPTER following is the document for most commonly asked questions about the ACM society.
            If someone asks any question, answer them according to these chunks of the data:

            {PDF}

            Answer in this format:
            Final Answer: <answer to the user question>
            '''),
            ("human", "{input}")
        ]
    )

    # Combine prompt with the model
    chain = prompt | llm

    # Generate response
    response = chain.invoke(
        {
            "PDF": docs,
            "input": user_question
        }
    )
    output = response.content

    # Extract final answer from the output
    def extract_final_answer(output):
        start_marker = "Final Answer: "
        start_index = output.find(start_marker)
        final_answer = output[start_index + len(start_marker):].strip()
        return final_answer

    final_answer = extract_final_answer(output)
    return final_answer

# Streamlit UI
st.title("ACM GIKI Chapter Chatbot")
st.markdown("Ask any question about the ACM society, and I'll provide you with the most accurate answer based on the document!")

# User input
user_question = st.text_input("Enter your query:")

# Chatbot response
if user_question:
    with st.spinner("Generating response..."):
        response = answer_question(llm, user_question)
        st.success("Here's the response:")
        st.write(response)
