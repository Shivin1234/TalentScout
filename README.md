🎯 TalentScout: AI Recruitment Assistant

📖 Project Overview

TalentScout is an intelligent, automated technical screening tool designed to simplify the hiring process. Built with Streamlit and powered by the lightning-fast Groq LPU Inference Engine, this application acts as a first-line recruiter. It engages candidates in natural conversation to collect essential details and then pivots into a customized technical interview based on their specific skills. 🚀

🧠 How It Works

The assistant operates using a dual-model logic. While the primary model (Llama 3.3 70B) handles the complex task of interviewing, a secondary, faster model (Llama 3.1 8B) works silently in the background. This "Observer" model scans the chat history to extract structured data like names and emails, updating the candidate's profile in real-time without interrupting the flow of conversation. 🔍

✨ Key Features

The app features a reactive Dashboard UI that provides immediate feedback to the user. As you chat, a sidebar displays your professional profile and a progress bar that tracks how close you are to completing the screening. By automating the information-gathering phase, TalentScout allows human recruiters to focus their time on the most qualified candidates, significantly reducing the "time-to-hire." 📊

🛠️ Technical Foundation

On the backend, the project leverages Python and the Groq API to achieve sub-second response times. Security is a top priority, so the app is designed to manage API secrets through environment variables and .gitignore files, ensuring that sensitive keys are never exposed on public platforms like GitHub. The interface is further polished with custom CSS to provide a modern, chat-centric user experience. 💻

🚀 Getting Started

To run this project locally, you simply need to clone the repository, install the dependencies listed in the requirements.txt file, and provide your own Groq API key in a .env file. Once configured, a single command—streamlit run app.py—launches the full recruitment portal in your browser, ready to screen the next top talent. 🌟
