# # # -- coding: utf-8 --
# # """chatbot_streamlit.py"""

# # import os
# # import streamlit as st
# # from langchain_openai import OpenAIEmbeddings, ChatOpenAI
# # from langchain.text_splitter import RecursiveCharacterTextSplitter
# # from langchain.docstore.document import Document
# # from langchain_community.vectorstores import FAISS
# # from langchain_core.prompts import ChatPromptTemplate

# # # Set OpenAI API key securely using Streamlit secrets
# # os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]

# # # Data for the ACM GIKI Chapter
# # data = '''GIKI Chapter
# # Website
# # www.acmgiki.com
# # About GIK Institute
# # The Ghulam Ishaq Khan Institute of Engineering Sciences and Technology is one of Pakistan's most
# # prestigious engineering institutes. It is dedicated to promoting excellence in engineering, sciences,
# # emerging technologies, and other disciplines, serving as a center of change in the country. GIKI has
# # set the standard for brilliance in engineering by producing graduates working in some of the most
# # sought-after national and international organizations.
# # About ACM GIKI Chapter
# # The Association for Computing Machinery (ACM) is a worldwide professional organization focused
# # on advancing computer science theory and practice.
# # ACM GIKI Activities
# # Student workshops
# # Specialized courses
# # Introductory seminars
# # Software and computer game competitions
# # Message from the President
# # "Welcome to ACM GIKI! We are a community of passionate computer scientists and engineers
# # working to build a better future. We offer events and activities to help you learn, grow, and connect
# # with others. Make the most of your time at GIKI!"
# # - President ACM
# # Our Events
# # Softcom
# # ICPC Pakistan
# # Association for Computing Machinery (ACM)
# # Hackathons
# # Workshops
# # Outreach Programs
# # Softcom
# # An annual nationwide competition organized by GIKI since 2000. It includes:
# # Software competitions
# # Multimedia presentations
# # Quizzes
# # Speed programming
# # Event Highlights
# # Hackathon: Collaborative project introductions.
# # Speed Programming: Solve algorithmic problems efficiently.
# # Game Development: Hands-on sessions for beginners.
# # ICPC Pakistan
# # The ACM International Collegiate Programming Contest (ICPC) is the oldest and most prestigious
# # programming competition in the world. It is often referred to as the "Olympics of Programming
# # Competitions."
# # Tips for ICPC
# # Master algorithms and data structures
# # Practice consistently
# # Focus on team collaboration
# # Simulate contest conditions
# # Optimize code for performance
# # Outreach Program
# # Mission: To spread awareness, inspire youth, and empower underprivileged students through
# # education and mentorship.
# # Key Initiatives
# # Career Counseling: Discussions on tech roles like AI and data science.
# # Motivational Speakers: Personal stories and encouragement to pursue education.
# # Workshops
# # Hands-on learning opportunities in:
# # Python: From basics to advanced levels.
# # C++: Help freshmen prepare for labs and exams.
# # Data Science: Practical insights for enthusiasts.
# # Join us to elevate your tech skills!
# # Sponsorship Packages
# # Available Packages
# # Platinum: PKR 600,000
# # Gold: PKR 400,000
# # Silver: PKR 200,000
# # Bronze: PKR 100,000
# # Incentives by Package
# # Incentives Platinum Gold Silver Bronze
# # Certificate of appreciation ✅ ✅ ✅ ✅
# # Social media acknowledgement ✅ ✅ ✅ ✅
# # Logo on guidebook ✅ ✅ ✅ ✅
# # Logo on all event posters ✅ ✅ ✅ ✅
# # VIP invites (opening and closing) 5 5 4 2
# # Company banners in venue ✅ ✅ ❌ ❌
# # Pamphlets in gift bags ✅ ✅ ✅ ❌
# # Logo on host team shirts ✅ ✅ ✅ ❌
# # Naming rights to Softcom theme ✅ ❌ ❌ ❌
# # Logo on guest certificates ✅ ✅ ❌ ❌
# # Session in closing ceremony ✅ ❌ ❌ ❌
# # Media coverage of company’s stall ✅ ❌ ❌ ❌
# # Highlights of the Event
# # Theme Dinner: A formal dinner to foster connections and friendships.
# # Concert: A lively performance to conclude the event. Previous performers include **Farhan
# # Saeed.
# # Previous Sponsors
# # Strategic Systems International
# # Graana
# # Bank Alfalah
# # TopCity-1
# # Participants
# # Students from universities across Pakistan.
# # 10K+ followers
# # 10K+ alumni
# # 2K+ current students
# # 300+ participants annually
# # Contact Us
# # President
# # Name: Anas Raza Aslam
# # Phone: +92 336 7297360
# # Email: anasraza.me@gmail.com
# # Event Coordinator
# # Name: Ali Iftikhar
# # Phone: +92 311 1721609
# # Email: mianali5451@gmail.com
# # General Inquiries
# # Email: acm@giki.edu.pk
# # Instagram: @acm.giki
# # '''

# # # Initialize the LLM
# # llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.8)

# # # Function to answer questions based on the provided data
# # def answer_question(llm, user_question):
# #     text_splitter = RecursiveCharacterTextSplitter(
# #         chunk_size=100,  # Adjust the chunk size as needed
# #         chunk_overlap=20  # Adjust the overlap as needed
# #     )
# #     chunks = text_splitter.split_text(data)  

# #     pages = [Document(page_content=chunk) for chunk in chunks]

# #     faiss_index = FAISS.from_documents(pages, OpenAIEmbeddings(model="text-embedding-3-small"))
# #     docs = faiss_index.similarity_search(user_question, k=5)

# #     # Define the prompt for the LLM
# #     prompt = ChatPromptTemplate.from_messages(
# #         [
# #             ("system", '''
# #             This is the data for GIKI ACM CHAPTER following is the document for most commonly asked questions about the ACM society.
# #             If someone asks any question, answer them according to these chunks of the data:

# #             {PDF}

# #             Answer in this format:
# #             Final Answer: <answer to the user question>
# #             '''),

# #             ("human", "{input}")
# #         ]
# #     )

# #     # Combine prompt with the model
# #     chain = prompt | llm

# #     # Generate response
# #     response = chain.invoke(
# #         {
# #             "PDF": docs,
# #             "input": user_question
# #         }
# #     )
# #     output = response.content

# #     # Extract final answer from the output
# #     def extract_final_answer(output):
# #         start_marker = "Final Answer: "
# #         start_index = output.find(start_marker)
# #         final_answer = output[start_index + len(start_marker):].strip()
# #         return final_answer

# #     final_answer = extract_final_answer(output)
# #     return final_answer

# # # Streamlit UI
# # st.title("ACM GIKI Chapter Chatbot")
# # st.markdown("Ask any question about the ACM society, and I'll provide you with the most accurate answer based on the document!")

# # # User input
# # user_question = st.text_input("Enter your query:")

# # # Chatbot response
# # if user_question:
# #     with st.spinner("Generating response..."):
# #         response = answer_question(llm, user_question)
# #         st.write(response)
# # import os
# # import streamlit as st
# # from langchain_openai import OpenAIEmbeddings, ChatOpenAI
# # from langchain.text_splitter import RecursiveCharacterTextSplitter
# # from langchain.docstore.document import Document
# # from langchain_community.vectorstores import FAISS
# # from langchain_core.prompts import ChatPromptTemplate

# # # Set OpenAI API key securely using Streamlit secrets
# # os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]

# # # Data for the ACM GIKI Chapter
# # data = '''GIKI Chapter
# # Website
# # www.acmgiki.com
# # About GIK Institute
# # The Ghulam Ishaq Khan Institute of Engineering Sciences and Technology is one of Pakistan's most
# # prestigious engineering institutes. It is dedicated to promoting excellence in engineering, sciences,
# # emerging technologies, and other disciplines, serving as a center of change in the country. GIKI has
# # set the standard for brilliance in engineering by producing graduates working in some of the most
# # sought-after national and international organizations.
# # About ACM GIKI Chapter
# # The Association for Computing Machinery (ACM) is a worldwide professional organization focused
# # on advancing computer science theory and practice.
# # ACM GIKI Activities
# # Student workshops
# # Specialized courses
# # Introductory seminars
# # Software and computer game competitions
# # Message from the President
# # "Welcome to ACM GIKI! We are a community of passionate computer scientists and engineers
# # working to build a better future. We offer events and activities to help you learn, grow, and connect
# # with others. Make the most of your time at GIKI!"
# # - President ACM
# # Our Events
# # Softcom
# # ICPC Pakistan
# # Association for Computing Machinery (ACM)
# # Hackathons
# # Workshops
# # Outreach Programs
# # Softcom
# # An annual nationwide competition organized by GIKI since 2000. It includes:
# # Software competitions
# # Multimedia presentations
# # Quizzes
# # Speed programming
# # Event Highlights
# # Hackathon: Collaborative project introductions.
# # Speed Programming: Solve algorithmic problems efficiently.
# # Game Development: Hands-on sessions for beginners.
# # ICPC Pakistan
# # The ACM International Collegiate Programming Contest (ICPC) is the oldest and most prestigious
# # programming competition in the world. It is often referred to as the "Olympics of Programming
# # Competitions."
# # Tips for ICPC
# # Master algorithms and data structures
# # Practice consistently
# # Focus on team collaboration
# # Simulate contest conditions
# # Optimize code for performance
# # Outreach Program
# # Mission: To spread awareness, inspire youth, and empower underprivileged students through
# # education and mentorship.
# # Key Initiatives
# # Career Counseling: Discussions on tech roles like AI and data science.
# # Motivational Speakers: Personal stories and encouragement to pursue education.
# # Workshops
# # Hands-on learning opportunities in:
# # Python: From basics to advanced levels.
# # C++: Help freshmen prepare for labs and exams.
# # Data Science: Practical insights for enthusiasts.
# # Join us to elevate your tech skills!
# # Sponsorship Packages
# # Available Packages
# # Platinum: PKR 600,000
# # Gold: PKR 400,000
# # Silver: PKR 200,000
# # Bronze: PKR 100,000
# # Incentives by Package
# # Incentives Platinum Gold Silver Bronze
# # Certificate of appreciation ✅ ✅ ✅ ✅
# # Social media acknowledgement ✅ ✅ ✅ ✅
# # Logo on guidebook ✅ ✅ ✅ ✅
# # Logo on all event posters ✅ ✅ ✅ ✅
# # VIP invites (opening and closing) 5 5 4 2
# # Company banners in venue ✅ ✅ ❌ ❌
# # Pamphlets in gift bags ✅ ✅ ✅ ❌
# # Logo on host team shirts ✅ ✅ ✅ ❌
# # Naming rights to Softcom theme ✅ ❌ ❌ ❌
# # Logo on guest certificates ✅ ✅ ❌ ❌
# # Session in closing ceremony ✅ ❌ ❌ ❌
# # Media coverage of company’s stall ✅ ❌ ❌ ❌
# # Highlights of the Event
# # Theme Dinner: A formal dinner to foster connections and friendships.
# # Concert: A lively performance to conclude the event. Previous performers include **Farhan
# # Saeed.
# # Previous Sponsors
# # Strategic Systems International
# # Graana
# # Bank Alfalah
# # TopCity-1
# # Participants
# # Students from universities across Pakistan.
# # 10K+ followers
# # 10K+ alumni
# # 2K+ current students
# # 300+ participants annually
# # Contact Us
# # President
# # Name: Anas Raza Aslam
# # Phone: +92 336 7297360
# # Email: anasraza.me@gmail.com
# # Event Coordinator
# # Name: Ali Iftikhar
# # Phone: +92 311 1721609
# # Email: mianali5451@gmail.com
# # General Inquiries
# # Email: acm@giki.edu.pk
# # Instagram: @acm.giki
# # '''

# # # Initialize the LLM
# # llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.8)

# # # Function to answer questions based on the provided data
# # def answer_question(llm, user_question):
# #     text_splitter = RecursiveCharacterTextSplitter(
# #         chunk_size=100,
# #         chunk_overlap=20
# #     )
# #     chunks = text_splitter.split_text(data)  

# #     pages = [Document(page_content=chunk) for chunk in chunks]

# #     faiss_index = FAISS.from_documents(pages, OpenAIEmbeddings(model="text-embedding-3-small"))
# #     docs = faiss_index.similarity_search(user_question, k=5)

# #     prompt = ChatPromptTemplate.from_messages(
# #         [
# #             ("system", '''
# #             This is the data for GIKI ACM CHAPTER following is the document for most commonly asked questions about the ACM society.
# #             If someone asks any question, answer them according to these chunks of the data:

# #             {PDF}

# #             Answer in this format:
# #             Final Answer: <answer to the user question>
# #             '''),

# #             ("human", "{input}")
# #         ]
# #     )

# #     chain = prompt | llm
# #     response = chain.invoke(
# #         {
# #             "PDF": docs,
# #             "input": user_question
# #         }
# #     )
# #     output = response.content

# #     def extract_final_answer(output):
# #         start_marker = "Final Answer: "
# #         start_index = output.find(start_marker)
# #         final_answer = output[start_index + len(start_marker):].strip()
# #         return final_answer

# #     final_answer = extract_final_answer(output)
# #     return final_answer

# # # Streamlit UI
# # st.set_page_config(page_title="ACM GIKI Chapter Chatbot", layout="wide")

# # # Custom Styles
# # st.markdown("""
# #     <style>
# #         .title {
# #             font-size: 36px;
# #             font-weight: bold;
# #             color: #003366;
# #             text-align: center;
# #             padding-bottom: 20px;
# #         }
# #         .subtitle {
# #             font-size: 18px;
# #             color: #555;
# #             text-align: center;
# #             padding-bottom: 20px;
# #         }
# #         .query-input {
# #             font-size: 18px;
# #             padding: 12px;
# #             margin-top: 10px;
# #             border-radius: 8px;
# #             border: 2px solid #003366;
# #             width: 80%;
# #             margin: 0 auto;
# #             display: block;
# #         }
# #         .response-box {
# #             margin-top: 20px;
# #             padding: 20px;
# #             border-radius: 8px;
# #             background-color: #f4f7fa;
# #             box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
# #         }
# #         .footer {
# #             text-align: center;
# #             margin-top: 30px;
# #             color: #777;
# #             font-size: 14px;
# #         }
# #     </style>
# # """, unsafe_allow_html=True)

# # # Title and Description
# # st.markdown('<div class="title">ACM GIKI Chapter Chatbot</div>', unsafe_allow_html=True)
# # st.markdown('<div class="subtitle">Ask any question about the ACM society, and I\'ll provide you with the most accurate answer based on the document!</div>', unsafe_allow_html=True)

# # # User input
# # user_question = st.text_input("Enter your query:", key="query_input", placeholder="Ask me about ACM GIKI events or activities!")

# # # Chatbot response
# # if user_question:
# #     with st.spinner("Generating response..."):
# #         response = answer_question(llm, user_question)
# #         st.markdown(f'<div class="response-box">{response}</div>', unsafe_allow_html=True)

# # # Footer
# # st.markdown('<div class="footer">Powered by ACM GIKI Chapter | Streamlit</div>', unsafe_allow_html=True)

# import os
# import streamlit as st
# from langchain_openai import OpenAIEmbeddings, ChatOpenAI
# from langchain.text_splitter import RecursiveCharacterTextSplitter
# from langchain.docstore.document import Document
# from langchain_community.vectorstores import FAISS
# from langchain_core.prompts import ChatPromptTemplate

# # Set OpenAI API key securely using Streamlit secrets
# os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]

# # Data for the ACM GIKI Chapter
# data = '''(Your ACM GIKI Chapter data here)'''

# # Initialize the LLM
# llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.8)

# # Function to answer questions based on the provided data
# def answer_question(llm, user_question):
#     text_splitter = RecursiveCharacterTextSplitter(
#         chunk_size=100,
#         chunk_overlap=20
#     )
#     chunks = text_splitter.split_text(data)  

#     pages = [Document(page_content=chunk) for chunk in chunks]

#     faiss_index = FAISS.from_documents(pages, OpenAIEmbeddings(model="text-embedding-3-small"))
#     docs = faiss_index.similarity_search(user_question, k=5)

#     prompt = ChatPromptTemplate.from_messages(
#         [
#             ("system", '''
#             This is the data for GIKI ACM CHAPTER following is the document for most commonly asked questions about the ACM society.
#             If someone asks any question, answer them according to these chunks of the data:

#             {PDF}

#             Answer in this format:
#             Final Answer: <answer to the user question>
#             '''),

#             ("human", "{input}")
#         ]
#     )

#     chain = prompt | llm
#     response = chain.invoke(
#         {
#             "PDF": docs,
#             "input": user_question
#         }
#     )
#     output = response.content

#     def extract_final_answer(output):
#         start_marker = "Final Answer: "
#         start_index = output.find(start_marker)
#         final_answer = output[start_index + len(start_marker):].strip()
#         return final_answer

#     final_answer = extract_final_answer(output)
#     return final_answer

# # Streamlit UI
# st.set_page_config(page_title="ACM GIKI Chapter Chatbot", layout="wide")

# # Compact Styles
# st.markdown("""
#     <style>
#         body {
#             font-family: Arial, sans-serif;
#             background-color: #f9f9f9;
#             color: #333;
#         }
#         .title {
#             font-size: 28px;
#             font-weight: bold;
#             color: #003366;
#             text-align: center;
#             margin-top: 20px;
#         }
#         .subtitle {
#             font-size: 14px;
#             color: #555;
#             text-align: center;
#             margin-bottom: 20px;
#         }
#         .query-input {
#             font-size: 16px;
#             padding: 10px;
#             margin: 10px 0;
#             border-radius: 6px;
#             border: 1px solid #ddd;
#             width: 80%;
#             margin: 0 auto;
#             display: block;
#         }
#         .response-box {
#             margin-top: 10px;
#             padding: 15px;
#             border-radius: 6px;
#             background-color: #fff;
#             border: 1px solid #ddd;
#             box-shadow: 0 3px 5px rgba(0, 0, 0, 0.1);
#             width: 80%;
#             margin: 0 auto;
#         }
#         .footer {
#             text-align: center;
#             margin-top: 20px;
#             color: #777;
#             font-size: 12px;
#         }
#     </style>
# """, unsafe_allow_html=True)

# # Title and Description
# st.markdown('<div class="title">ACM GIKI Chapter Chatbot</div>', unsafe_allow_html=True)
# st.markdown('<div class="subtitle">Ask questions about ACM GIKI events or activities!</div>', unsafe_allow_html=True)

# # User input
# user_question = st.text_input("Enter your query:", key="query_input", placeholder="e.g., What is Softcom?")

# # Chatbot response
# if user_question:
#     with st.spinner("Generating response..."):
#         response = answer_question(llm, user_question)
#         st.markdown(f'<div class="response-box">{response}</div>', unsafe_allow_html=True)

# # Footer
# st.markdown('<div class="footer">Powered by ACM GIKI Chapter | Streamlit</div>', unsafe_allow_html=True)

import os
import streamlit as st
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.docstore.document import Document
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate

# Set OpenAI API key securely using Streamlit secrets
os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]

# Data for the ACM GIKI Chapter
data = '''(Your ACM GIKI Chapter data here)'''

# Initialize the LLM
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.8)

# Function to answer questions based on the provided data
def answer_question(llm, user_question):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=100,
        chunk_overlap=20
    )
    chunks = text_splitter.split_text(data)  

    pages = [Document(page_content=chunk) for chunk in chunks]

    faiss_index = FAISS.from_documents(pages, OpenAIEmbeddings(model="text-embedding-3-small"))
    docs = faiss_index.similarity_search(user_question, k=5)

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

    chain = prompt | llm
    response = chain.invoke(
        {
            "PDF": docs,
            "input": user_question
        }
    )
    output = response.content

    def extract_final_answer(output):
        start_marker = "Final Answer: "
        start_index = output.find(start_marker)
        final_answer = output[start_index + len(start_marker):].strip()
        return final_answer

    final_answer = extract_final_answer(output)
    return final_answer

# Streamlit UI
st.set_page_config(page_title="ACM GIKI Chapter Chatbot", layout="Centered")

# Compact Styles
st.markdown("""
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f9f9f9;
            color: #333;
        }
        .logo {
            display: block;
            margin: 0 auto;
            max-width: 100px;  /* Adjust size */
        }
        .title {
            font-size: 28px;
            font-weight: bold;
            color: #003366;
            text-align: center;
            margin-top: 20px;
        }
        .subtitle {
            font-size: 14px;
            color: #555;
            text-align: center;
            margin-bottom: 20px;
        }
        .query-input {
            font-size: 16px;
            padding: 10px;
            margin: 10px 0;
            border-radius: 6px;
            border: 1px solid #ddd;
            width: 80%;
            margin: 0 auto;
            display: block;
        }
        .response-box {
            margin-top: 10px;
            padding: 15px;
            border-radius: 6px;
            background-color: #fff;
            border: 1px solid #ddd;
            box-shadow: 0 3px 5px rgba(0, 0, 0, 0.1);
            width: 80%;
            margin: 0 auto;
        }
        .footer {
            text-align: center;
            margin-top: 20px;
            color: #777;
            font-size: 12px;
        }
    </style>
""", unsafe_allow_html=True)

# Title and Description with Logo
st.markdown(
    """
    <img src="data:image/jpeg;base64,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" class="logo" alt="ACM GIKI Logo"/>
    """, unsafe_allow_html=True
)
st.markdown('<div class="title">ACM GIKI Chapter Chatbot</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Ask questions about ACM GIKI events or activities!</div>', unsafe_allow_html=True)

# User input
user_question = st.text_input("Enter your query:", key="query_input", placeholder="e.g., What is Softcom?")

# Chatbot response
if user_question:
    with st.spinner("Generating response..."):
        response = answer_question(llm, user_question)
        st.markdown(f'<div class="response-box">{response}</div>', unsafe_allow_html=True)

# Footer
st.markdown('<div class="footer">Powered by ACM GIKI Chapter | Streamlit</div>', unsafe_allow_html=True)

