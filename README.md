**#PresenceAI - AI-Powered Interview Coach 🤖#**

An AI-powered web application that serves as a personal interview coach. PresenceAI generates domain-specific questions, records your practice sessions, and provides real-time, data-driven feedback on your verbal and non-verbal communication skills.

(Recommended: Add a GIF of your application in action here. A tool like Giphy Capture can create this easily.)

About The Project
PresenceAI is designed to help users build confidence and improve their interview performance. Unlike generic practice tools, it leverages a Large Language Model (Google's Gemini) to create relevant questions for any job role, from "Software Engineer" to "HR Manager." After the user records their answers, the application uses computer vision and speech recognition to analyze their performance, providing a detailed feedback report.

Tech Stack
This project is a full-stack application built with a modern tech stack:

Frontend: React.js

Backend: Python, FastAPI

AI / ML:

LLM: Google Gemini Pro

Computer Vision: OpenCV

Speech Recognition: Google Web Speech API, SpeechRecognition

Audio Processing: MoviePy

Features
🤖 AI-Generated Questions: Get personalized interview questions for any job role.

📹 Webcam Recording: Practice your answers in a realistic interview setting.

🧠 Real-Time Analysis: Receive instant feedback on key communication metrics:

Speaking Pace (Words Per Minute)

Filler Word Count ("um," "uh," "like," etc.)

Eye Contact (Estimated via face detection)

Full Speech-to-Text Transcript

💡 Smart Feedback: A comprehensive dashboard to review your performance.

🔄 Unlimited Practice: A seamless "Restart" flow to practice for different roles.

🎨 Modern UI: A clean, responsive, and intuitive dark-theme interface.

Getting Started
To get a local copy up and running, follow these simple steps.

Prerequisites
Python 3.9+

Node.js and npm

A Google AI API Key

Installation & Setup
Clone the repo

Bash

git clone https://github.com/Aanishnithin07/PresenceAI.git
cd PresenceAI
Backend Setup

Bash

cd presence-ai-backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
Create a .env file in the presence-ai-backend folder and add your API key:

GOOGLE_API_KEY="YOUR_API_KEY_HERE"
Frontend Setup (in a new terminal)

Bash

cd presence-ai-frontend
npm install
Running the Application
Start the Backend Server (from presence-ai-backend)

Bash

uvicorn main:app --reload
Start the Frontend Server (from presence-ai-frontend)

Bash

npm start
Open http://localhost:3000 in your browser.

Future Roadmap
🚀 Deployment: Package the application for deployment on cloud platforms.

👤 User Authentication: Add user accounts to save practice history.

📈 Advanced Metrics:

Implement sentiment and voice tone analysis.

Add gesture and posture analysis.

🎥 Video Storage: Allow users to save and review past practice sessions.
