import streamlit as st

# Set page configuration
st.set_page_config(page_title="AI Chat Dashboard", layout="wide", initial_sidebar_state="collapsed")

# Custom CSS for a sleek, professional look
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;700&display=swap');
    
    body {
        font-family: 'Roboto', sans-serif;
        background-color: #1E1E1E;
        color: #FFFFFF;
    }
    .stApp {
        background-color: #1E1E1E;
    }
    .app-title {
        font-size: 3.5rem;
        font-weight: 700;
        text-align: center;
        margin-bottom: 2rem;
        color: #FFFFFF;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
    }
    .app-description {
        font-size: 1.2rem;
        text-align: center;
        margin-bottom: 3rem;
        color: #B0B0B0;
    }
    .custom-button {
        display: inline-block;
        width: 100%;
        padding: 1.5rem;
        background: linear-gradient(145deg, #2E2E2E, #1A1A1A);
        border: none;
        border-radius: 15px;
        box-shadow: 5px 5px 15px #0D0D0D, -5px -5px 15px #2D2D2D;
        text-align: center;
        text-decoration: none;
        color: #FFFFFF;
        font-size: 1.2rem;
        font-weight: 500;
        transition: all 0.3s ease;
    }
    .custom-button:hover {
        background: linear-gradient(145deg, #1A1A1A, #2E2E2E);
        transform: translateY(-5px);
        box-shadow: 8px 8px 20px #0D0D0D, -8px -8px 20px #2D2D2D;
    }
    .icon {
        font-size: 3rem;
        margin-bottom: 1rem;
    }
    .icon-websites { color: #FF6B6B; }
    .icon-database { color: #4ECDC4; }
    .icon-pdf { color: #45B7D1; }
    .footer {
        text-align: center;
        color: #B0B0B0;
        margin-top: 3rem;
        padding: 1rem;
        font-size: 0.9rem;
    }
</style>
""", unsafe_allow_html=True)

# App title and description
st.markdown('<h1 class="app-title">AI Chat Apps by Paras</h1>', unsafe_allow_html=True)
st.markdown('<p class="app-description">Built with Langchain, ChromaDB, Pinecone, and Streamlit</p>', unsafe_allow_html=True)

# Create three columns for the buttons
col1, col2, col3 = st.columns(3)

# Button 1: Chat with Websites
with col1:
    st.markdown("""
    <a href="https://websiteschat.streamlit.app/" class="custom-button">
        <div class="icon icon-websites">🌐</div>
        Chat with Websites
    </a>
    """, unsafe_allow_html=True)

# Button 2: Chat with Database
with col2:
    st.markdown("""
    <a href="https://chatwithdb.streamlit.app/" class="custom-button">
        <div class="icon icon-database">🗄️</div>
        Chat with Database
    </a>
    """, unsafe_allow_html=True)

# Button 3: Chat with PDF
with col3:
    st.markdown("""
    <a href="https://chatwithpdffiles.streamlit.app/" class="custom-button">
        <div class="icon icon-pdf">📄</div>
        Chat with PDF
    </a>
    """, unsafe_allow_html=True)

# Footer
st.markdown('<div class="footer">© 2024 Your Company Name. All rights reserved.</div>', unsafe_allow_html=True)