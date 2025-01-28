# # -- coding: utf-8 --
# """chatbot_streamlit.py"""

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
# data = '''GIKI Chapter
# Website
# www.acmgiki.com
# About GIK Institute
# The Ghulam Ishaq Khan Institute of Engineering Sciences and Technology is one of Pakistan's most
# prestigious engineering institutes. It is dedicated to promoting excellence in engineering, sciences,
# emerging technologies, and other disciplines, serving as a center of change in the country. GIKI has
# set the standard for brilliance in engineering by producing graduates working in some of the most
# sought-after national and international organizations.
# About ACM GIKI Chapter
# The Association for Computing Machinery (ACM) is a worldwide professional organization focused
# on advancing computer science theory and practice.
# ACM GIKI Activities
# Student workshops
# Specialized courses
# Introductory seminars
# Software and computer game competitions
# Message from the President
# "Welcome to ACM GIKI! We are a community of passionate computer scientists and engineers
# working to build a better future. We offer events and activities to help you learn, grow, and connect
# with others. Make the most of your time at GIKI!"
# - President ACM
# Our Events
# Softcom
# ICPC Pakistan
# Association for Computing Machinery (ACM)
# Hackathons
# Workshops
# Outreach Programs
# Softcom
# An annual nationwide competition organized by GIKI since 2000. It includes:
# Software competitions
# Multimedia presentations
# Quizzes
# Speed programming
# Event Highlights
# Hackathon: Collaborative project introductions.
# Speed Programming: Solve algorithmic problems efficiently.
# Game Development: Hands-on sessions for beginners.
# ICPC Pakistan
# The ACM International Collegiate Programming Contest (ICPC) is the oldest and most prestigious
# programming competition in the world. It is often referred to as the "Olympics of Programming
# Competitions."
# Tips for ICPC
# Master algorithms and data structures
# Practice consistently
# Focus on team collaboration
# Simulate contest conditions
# Optimize code for performance
# Outreach Program
# Mission: To spread awareness, inspire youth, and empower underprivileged students through
# education and mentorship.
# Key Initiatives
# Career Counseling: Discussions on tech roles like AI and data science.
# Motivational Speakers: Personal stories and encouragement to pursue education.
# Workshops
# Hands-on learning opportunities in:
# Python: From basics to advanced levels.
# C++: Help freshmen prepare for labs and exams.
# Data Science: Practical insights for enthusiasts.
# Join us to elevate your tech skills!
# Sponsorship Packages
# Available Packages
# Platinum: PKR 600,000
# Gold: PKR 400,000
# Silver: PKR 200,000
# Bronze: PKR 100,000
# Incentives by Package
# Incentives Platinum Gold Silver Bronze
# Certificate of appreciation ✅ ✅ ✅ ✅
# Social media acknowledgement ✅ ✅ ✅ ✅
# Logo on guidebook ✅ ✅ ✅ ✅
# Logo on all event posters ✅ ✅ ✅ ✅
# VIP invites (opening and closing) 5 5 4 2
# Company banners in venue ✅ ✅ ❌ ❌
# Pamphlets in gift bags ✅ ✅ ✅ ❌
# Logo on host team shirts ✅ ✅ ✅ ❌
# Naming rights to Softcom theme ✅ ❌ ❌ ❌
# Logo on guest certificates ✅ ✅ ❌ ❌
# Session in closing ceremony ✅ ❌ ❌ ❌
# Media coverage of company’s stall ✅ ❌ ❌ ❌
# Highlights of the Event
# Theme Dinner: A formal dinner to foster connections and friendships.
# Concert: A lively performance to conclude the event. Previous performers include **Farhan
# Saeed.
# Previous Sponsors
# Strategic Systems International
# Graana
# Bank Alfalah
# TopCity-1
# Participants
# Students from universities across Pakistan.
# 10K+ followers
# 10K+ alumni
# 2K+ current students
# 300+ participants annually
# Contact Us
# President
# Name: Anas Raza Aslam
# Phone: +92 336 7297360
# Email: anasraza.me@gmail.com
# Event Coordinator
# Name: Ali Iftikhar
# Phone: +92 311 1721609
# Email: mianali5451@gmail.com
# General Inquiries
# Email: acm@giki.edu.pk
# Instagram: @acm.giki
# '''

# # Initialize the LLM
# llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.8)

# # Function to answer questions based on the provided data
# def answer_question(llm, user_question):
#     text_splitter = RecursiveCharacterTextSplitter(
#         chunk_size=100,  # Adjust the chunk size as needed
#         chunk_overlap=20  # Adjust the overlap as needed
#     )
#     chunks = text_splitter.split_text(data)  

#     pages = [Document(page_content=chunk) for chunk in chunks]

#     faiss_index = FAISS.from_documents(pages, OpenAIEmbeddings(model="text-embedding-3-small"))
#     docs = faiss_index.similarity_search(user_question, k=5)

#     # Define the prompt for the LLM
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

#     # Combine prompt with the model
#     chain = prompt | llm

#     # Generate response
#     response = chain.invoke(
#         {
#             "PDF": docs,
#             "input": user_question
#         }
#     )
#     output = response.content

#     # Extract final answer from the output
#     def extract_final_answer(output):
#         start_marker = "Final Answer: "
#         start_index = output.find(start_marker)
#         final_answer = output[start_index + len(start_marker):].strip()
#         return final_answer

#     final_answer = extract_final_answer(output)
#     return final_answer

# # Streamlit UI
# st.title("ACM GIKI Chapter Chatbot")
# st.markdown("Ask any question about the ACM society, and I'll provide you with the most accurate answer based on the document!")

# # User input
# user_question = st.text_input("Enter your query:")

# # Chatbot response
# if user_question:
#     with st.spinner("Generating response..."):
#         response = answer_question(llm, user_question)
#         st.write(response)
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
data = '''GIKI Chapter
Website
www.acmgiki.com
About GIK Institute
The Ghulam Ishaq Khan Institute of Engineering Sciences and Technology is one of Pakistan's most
prestigious engineering institutes. It is dedicated to promoting excellence in engineering, sciences,
emerging technologies, and other disciplines, serving as a center of change in the country. GIKI has
set the standard for brilliance in engineering by producing graduates working in some of the most
sought-after national and international organizations.
About ACM GIKI Chapter
The Association for Computing Machinery (ACM) is a worldwide professional organization focused
on advancing computer science theory and practice.
ACM GIKI Activities
Student workshops
Specialized courses
Introductory seminars
Software and computer game competitions
Message from the President
"Welcome to ACM GIKI! We are a community of passionate computer scientists and engineers
working to build a better future. We offer events and activities to help you learn, grow, and connect
with others. Make the most of your time at GIKI!"
- President ACM
Our Events
Softcom
ICPC Pakistan
Association for Computing Machinery (ACM)
Hackathons
Workshops
Outreach Programs
Softcom
An annual nationwide competition organized by GIKI since 2000. It includes:
Software competitions
Multimedia presentations
Quizzes
Speed programming
Event Highlights
Hackathon: Collaborative project introductions.
Speed Programming: Solve algorithmic problems efficiently.
Game Development: Hands-on sessions for beginners.
ICPC Pakistan
The ACM International Collegiate Programming Contest (ICPC) is the oldest and most prestigious
programming competition in the world. It is often referred to as the "Olympics of Programming
Competitions."
Tips for ICPC
Master algorithms and data structures
Practice consistently
Focus on team collaboration
Simulate contest conditions
Optimize code for performance
Outreach Program
Mission: To spread awareness, inspire youth, and empower underprivileged students through
education and mentorship.
Key Initiatives
Career Counseling: Discussions on tech roles like AI and data science.
Motivational Speakers: Personal stories and encouragement to pursue education.
Workshops
Hands-on learning opportunities in:
Python: From basics to advanced levels.
C++: Help freshmen prepare for labs and exams.
Data Science: Practical insights for enthusiasts.
Join us to elevate your tech skills!
Sponsorship Packages
Available Packages
Platinum: PKR 600,000
Gold: PKR 400,000
Silver: PKR 200,000
Bronze: PKR 100,000
Incentives by Package
Incentives Platinum Gold Silver Bronze
Certificate of appreciation ✅ ✅ ✅ ✅
Social media acknowledgement ✅ ✅ ✅ ✅
Logo on guidebook ✅ ✅ ✅ ✅
Logo on all event posters ✅ ✅ ✅ ✅
VIP invites (opening and closing) 5 5 4 2
Company banners in venue ✅ ✅ ❌ ❌
Pamphlets in gift bags ✅ ✅ ✅ ❌
Logo on host team shirts ✅ ✅ ✅ ❌
Naming rights to Softcom theme ✅ ❌ ❌ ❌
Logo on guest certificates ✅ ✅ ❌ ❌
Session in closing ceremony ✅ ❌ ❌ ❌
Media coverage of company’s stall ✅ ❌ ❌ ❌
Highlights of the Event
Theme Dinner: A formal dinner to foster connections and friendships.
Concert: A lively performance to conclude the event. Previous performers include **Farhan
Saeed.
Previous Sponsors
Strategic Systems International
Graana
Bank Alfalah
TopCity-1
Participants
Students from universities across Pakistan.
10K+ followers
10K+ alumni
2K+ current students
300+ participants annually
Contact Us
President
Name: Anas Raza Aslam
Phone: +92 336 7297360
Email: anasraza.me@gmail.com
Event Coordinator
Name: Ali Iftikhar
Phone: +92 311 1721609
Email: mianali5451@gmail.com
General Inquiries
Email: acm@giki.edu.pk
Instagram: @acm.giki
'''

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
st.set_page_config(page_title="ACM GIKI Chapter Chatbot", layout="wide")

# Custom Styles
st.markdown("""
    <style>
        .title {
            font-size: 36px;
            font-weight: bold;
            color: #003366;
            text-align: center;
            padding-bottom: 20px;
        }
        .subtitle {
            font-size: 18px;
            color: #555;
            text-align: center;
            padding-bottom: 20px;
        }
        .query-input {
            font-size: 18px;
            padding: 12px;
            margin-top: 10px;
            border-radius: 8px;
            border: 2px solid #003366;
            width: 80%;
            margin: 0 auto;
            display: block;
        }
        .response-box {
            margin-top: 20px;
            padding: 20px;
            border-radius: 8px;
            background-color: #f4f7fa;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        .footer {
            text-align: center;
            margin-top: 30px;
            color: #777;
            font-size: 14px;
        }
    </style>
""", unsafe_allow_html=True)

# Title and Description
st.markdown('<div class="title">ACM GIKI Chapter Chatbot</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Ask any question about the ACM society, and I\'ll provide you with the most accurate answer based on the document!</div>', unsafe_allow_html=True)

# User input
user_question = st.text_input("Enter your query:", key="query_input", placeholder="Ask me about ACM GIKI events or activities!")

# Chatbot response
if user_question:
    with st.spinner("Generating response..."):
        response = answer_question(llm, user_question)
        st.markdown(f'<div class="response-box">{response}</div>', unsafe_allow_html=True)

# Footer
st.markdown('<div class="footer">Powered by ACM GIKI Chapter | Streamlit</div>', unsafe_allow_html=True)


