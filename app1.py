import streamlit as st
import os
import json
import time
from groq import Groq
from dotenv import load_dotenv

# --- 1. CONFIGURATION & SECURITY ---
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    st.error("⚠️ GROQ_API_KEY not found! Please add it to your .env file.")
    st.stop()

client = Groq(api_key=api_key)

# --- 2. CUSTOM UI STYLING (CSS) ---
st.set_page_config(page_title="TalentScout AI", page_icon="🎯", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .stChatMessage { border-radius: 15px; margin-bottom: 10px; border: 1px solid #e0e0e0; }
    .sidebar-card {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin-bottom: 20px;
    }
    .stProgress > div > div > div > div { background-color: #007BFF; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SESSION STATE MANAGEMENT ---
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! I'm TalentScout. I'll be conducting your initial screening today. To get started, could you please tell me your **Full Name** and the **Position** you are applying for?"}
    ]

if "candidate_data" not in st.session_state:
    st.session_state.candidate_data = {
        "Name": "---", "Email": "---", "Experience": "---", "Tech Stack": "---"
    }

# --- 4. AI PROMPT STRATEGY ---
# Persona for the interviewer
SYSTEM_PROMPT = """
You are 'TalentScout', a professional HR Assistant. 
PHASE 1: Collect Name, Email, Years of Experience, and Tech Stack.
PHASE 2: Once you have the tech stack, ask 3 technical questions specific to those tools.
Tone: Professional, encouraging, and concise. 
If the user asks something irrelevant, politely steer them back to the interview.
"""

# Prompt for the background data extractor
EXTRACTOR_PROMPT = """
Analyze the conversation and extract candidate details.
Return ONLY a valid JSON object with keys: "Name", "Email", "Experience", "Tech Stack".
Use "---" for missing values.
"""

# --- 5. CORE LOGIC FUNCTIONS ---
def get_chat_response(messages):
    try:
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "system", "content": SYSTEM_PROMPT}] + messages,
            temperature=0.7
        )
        return completion.choices[0].message.content
    except Exception as e:
        return f"I'm sorry, I encountered an error: {e}"

def extract_data(messages):
    try:
        completion = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "system", "content": EXTRACTOR_PROMPT}] + messages,
            response_format={"type": "json_object"}
        )
        return json.loads(completion.choices[0].message.content)
    except:
        return st.session_state.candidate_data

# --- 6. SIDEBAR UI ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/942/942799.png", width=80)
    st.title("TalentScoutAI Portal")
    st.divider()
    
    st.markdown("**Candidate Profile**")
    data = st.session_state.candidate_data
    
    # Visual Cards for Data
    st.info(f"👤 **Name:** {data['Name']}")
    st.info(f"📧 **Email:** {data['Email']}")
    st.info(f"⏳ **Experience:** {data['Experience']}")
    st.info(f"💻 **Stack:** {data['Tech Stack']}")
    
    st.divider()
    
    # Progress Calculation
    filled_fields = sum(1 for v in data.values() if v != "---")
    progress = filled_fields / 4
    st.write(f"Profile Completion: {int(progress*100)}%")
    st.progress(progress)
    
    if st.button("Reset Interview", use_container_width=True):
        st.session_state.messages = [st.session_state.messages[0]]
        st.session_state.candidate_data = {"Name": "---", "Email": "---", "Experience": "---", "Tech Stack": "---"}
        st.rerun()

# --- 7. MAIN CHAT INTERFACE ---
st.write("### 💬 TalentScoutAI Screening Chat")

# Display History
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# Chat Input
if prompt := st.chat_input("Type your message here..."):
    # Add User Message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    # Exit check
    if any(x in prompt.lower() for x in ["exit", "bye", "quit"]):
        with st.chat_message("assistant"):
            st.write("Thank you for your time! We have saved your details. Goodbye!")
        st.stop()

    # Generate Assistant Response
    with st.chat_message("assistant"):
        with st.spinner("TalentScout is thinking..."):
            response = get_chat_response(st.session_state.messages)
            st.write(response)
            st.session_state.messages.append({"role": "assistant", "content": response})

    # Background Data Extraction
    new_data = extract_data(st.session_state.messages)
    st.session_state.candidate_data.update(new_data)
    
    # Rerun to update sidebar visuals immediately
    st.rerun()