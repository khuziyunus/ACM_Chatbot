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
os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]

# Set Hugging Face token securely using Streamlit secrets
from huggingface_hub import HfFolder
HfFolder.save_token(st.secrets["HF_API_TOKEN"])

documents = [
    {
        'metadata': {'source': '/content/chat bot sponser data.pdf', 'page': 0},
        'page_content': '''GIKI Chapter
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
Association for Computing Machinery (ACM)'''
    },
    {
        'metadata': {'source': '/content/chat bot sponser data.pdf', 'page': 1},
        'page_content': '''Hackathons
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
Motivational Speakers: Personal stories and encouragement to pursue education.'''
    },
    {
        'metadata': {'source': '/content/chat bot sponser data.pdf', 'page': 2},
        'page_content': '''Workshops
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
Certificate of appreciation ✅ ✅✅✅
Social media acknowledgement✅ ✅✅✅
Logo on guidebook ✅ ✅✅✅
Logo on all event posters ✅ ✅✅✅
VIP invites (opening and closing) 5 5 4 2
Company banners in venue ✅ ✅❌❌
Pamphlets in gift bags ✅ ✅✅❌
Logo on host team shirts ✅ ✅✅❌
Naming rights to Softcom theme ✅ ❌❌❌
Logo on guest certificates ✅ ✅❌❌
Session in closing ceremony ✅ ❌❌❌
Media coverage of company’s stall ✅ ❌❌❌
Highlights of the Event
Theme Dinner: A formal dinner to foster connections and friendships.
Concert: A lively performance to conclude the event. Previous performers include **Farhan Saeed.
Previous Sponsors'''
    },
    {
        'metadata': {'source': '/content/chat bot sponser data.pdf', 'page': 3},
        'page_content': '''Strategic Systems International
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
Instagram: @acm.giki'''
    }
]


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
