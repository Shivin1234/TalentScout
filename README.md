# 🎯 TalentScout AI — Intelligent Technical Screening Assistant

TalentScout AI is a conversational, AI-driven technical screening assistant that automates the first round of hiring. It conducts structured, real-time interviews with candidates, dynamically generates technical questions based on their tech stack, and extracts structured candidate data — bridging the gap between static application forms and human interviews.

🔗 **Live Demo:** [Try TalentScout AI](https://lnkd.in/dd5qhQGu)

---

## 📌 Overview

Traditional first-round technical screening is time-consuming and inconsistent. TalentScout AI solves this by using a **dual-LLM pipeline** to conduct adaptive, role-based interviews — asking relevant technical questions, tracking profile completion in real time, and converting free-form conversation into clean, structured data recruiters can act on immediately.

---

## 🚀 Key Features

- 🤖 **AI-Powered Conversational Flow** — Natural, multi-turn interview experience instead of rigid forms
- 🧠 **Dynamic Technical Questioning** — Questions generated on the fly based on the candidate's declared tech stack
- 📊 **Real-Time Progress Tracking** — Live profile completion indicator throughout the conversation
- 🗂️ **Structured Data Extraction** — Automatically parses conversation into structured JSON (skills, experience, responses)
- 🎨 **Dashboard-Style UI** — Clean, recruiter-friendly interface built with Streamlit
- 🔐 **Secure API Handling** — Environment-variable-based key management, no hardcoded secrets
- 💾 **Session State Management** — Maintains conversational memory and context across the interview

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Language | Python |
| UI Framework | Streamlit |
| LLM Infrastructure | Groq Cloud (LPU Inference) |
| Primary Model | LLaMA 3.3 70B |
| Secondary Model | LLaMA 3.1 8B |
| Core Technique | Prompt Engineering (role-based & phase-driven) |

---

## 🧩 How It Works

1. **Candidate Onboarding** — Candidate enters basic details and declares their tech stack
2. **Adaptive Interview Phase** — The dual-LLM pipeline drives a phase-based conversation:
   - **LLaMA 3.3 70B** handles complex reasoning, question generation, and technical evaluation
   - **LLaMA 3.1 8B** handles lightweight tasks like entity extraction and quick validations, keeping the pipeline fast and cost-efficient
3. **Dynamic Question Generation** — Questions adapt in real time based on the candidate's responses and stated skills
4. **Structured Extraction** — Key information (skills, experience, answers) is parsed into JSON as the conversation progresses
5. **Progress Dashboard** — Recruiters/candidates see live profile completion status throughout

---

## ⚙️ Architecture Highlights

- **Multi-model design**: splits reasoning-heavy and lightweight tasks across two LLMs for speed and cost efficiency
- **Role-based & phase-driven prompting**: each interview phase (intro, technical deep-dive, wrap-up) uses tailored system prompts
- **Session state management**: Streamlit session state preserves conversational memory across turns
- **Secure configuration**: API keys and secrets managed via environment variables, never committed to source

---

## 🏗️ Installation & Setup

```bash
# Clone the repository
git clone https://github.com/<your-username>/talentscout-ai.git
cd talentscout-ai

# Create a virtual environment
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
echo "GROQ_API_KEY=your_groq_api_key" > .env

# Run the app
streamlit run app.py
```

---

## 🧠 What I Learned

- Designing multi-model AI systems that balance speed, cost, and reasoning quality
- Role-based and phase-driven prompt engineering for structured conversational flows
- Secure API key handling using environment variables
- Managing session state for coherent multi-turn conversational memory
- Building production-ready, recruiter-facing AI interfaces

---

## 🔮 Future Improvements

- Resume parsing integration for auto-filled candidate profiles
- Interview scoring and recruiter-facing analytics dashboard
- Multi-language support for global candidate pools
- Export structured results directly to ATS platforms

---
