# PresenceAI - AI-Powered Interview Coach

A complete full-stack application for AI-powered interview coaching with video recording and analysis capabilities.

## Project Structure

```
PresenceAI/
├── presence-ai-backend/          # Python FastAPI backend
│   ├── requirements.txt         # Python dependencies
│   ├── main.py                  # FastAPI server
│   └── ai_processor.py         # AI analysis module
└── presence-ai-frontend/        # React frontend
    ├── src/
    │   ├── components/
    │   │   ├── InterviewScreen.js    # Webcam recording component
    │   │   └── FeedbackDisplay.js    # Analysis results display
    │   ├── App.js                     # Main React app
    │   └── App.css                    # Styling
    └── package.json
```

## Setup Instructions

### Backend Setup (Python/FastAPI)

1. Navigate to the backend directory:
   ```bash
   cd presence-ai-backend
   ```

2. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the FastAPI server:
   ```bash
   uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```

The backend will be available at `http://localhost:8000`

### Frontend Setup (React)

1. Navigate to the frontend directory:
   ```bash
   cd presence-ai-frontend
   ```

2. Install dependencies (if not already done):
   ```bash
   npm install
   ```

3. Start the React development server:
   ```bash
   npm start
   ```

The frontend will be available at `http://localhost:3000`

## Features

- **🤖 AI-Generated Questions**: Personalized interview questions based on job role using Google's Gemini LLM
- **🎯 Domain-Specific Practice**: Tailored questions for any job position (Software Engineer, Data Scientist, etc.)
- **📹 Webcam Recording**: Record interview sessions directly in the browser
- **🧠 Real AI Analysis**: Advanced speech-to-text and computer vision analysis including:
  - **Speech-to-Text**: Automatic transcription of your speech
  - **Speaking Pace**: Real-time calculation of words per minute
  - **Filler Word Detection**: Counts "um", "uh", "like", "so", "you know", "i mean"
  - **Eye Contact Analysis**: Face detection to estimate eye contact percentage
  - **Transcript Display**: See exactly what you said during the interview
- **💡 Smart Feedback**: Intelligent recommendations based on your performance
- **🔄 Complete Interview Flow**: Setup → Practice → Analysis → Restart
- **🎨 Modern UI**: Beautiful dark theme with responsive design

## Usage

1. **Setup**: Start both the backend and frontend servers
2. **Get API Key**: Follow the setup instructions in `presence-ai-backend/SETUP_INSTRUCTIONS.md`
3. **Open App**: Navigate to `http://localhost:3000`
4. **Enter Job Role**: Type your desired job position (e.g., "Software Engineer")
5. **Generate Questions**: Click "Start Interview" to get AI-generated questions
6. **Practice**: Record your answers to the personalized questions
7. **Get Feedback**: View your AI-generated analysis and improvement tips
8. **Practice Again**: Use the restart button to try different job roles

## Development Notes

- **🤖 LLM Integration**: Uses Google's Gemini Pro model for intelligent question generation
- **🎯 Domain Expertise**: AI generates role-specific questions based on job requirements
- **🧠 Real AI Analysis**: Speech-to-text (Google Web Speech API) and computer vision (OpenCV)
- **📹 Audio Processing**: MoviePy for video-to-audio extraction with SpeechRecognition
- **👁️ Face Detection**: OpenCV's Haar Cascade classifier for eye contact analysis
- **🛡️ Error Handling**: Graceful fallback to demo data if analysis fails
- **🔄 State Management**: Complete interview flow with setup, practice, and feedback
- **🎨 Modern UI**: Responsive design with beautiful cards and hover effects

## Technical Implementation

- **Backend**: FastAPI with Google Gemini LLM integration
- **Question Generation**: AI-powered personalized interview questions
- **Speech Recognition**: Google Web Speech API for accurate transcription
- **Computer Vision**: OpenCV for face detection and analysis
- **Audio Processing**: MoviePy for video-to-audio extraction
- **Frontend**: React with multi-screen state management
- **API Integration**: RESTful endpoints for questions and analysis

## Next Steps for Production

- Add user authentication and session management
- Implement video storage and retrieval
- Add sentiment analysis using NLP libraries
- Improve eye contact detection with more sophisticated algorithms
- Add more detailed feedback metrics (gesture analysis, voice tone)
- Deploy to cloud platforms
