from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import shutil
import os
import json
import google.generativeai as genai
from dotenv import load_dotenv

from ai_processor import analyze_communication, AnalysisResult

# --- NEW: Load environment variables and configure API ---
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    print("--- FATAL ERROR: GOOGLE_API_KEY not found in .env file.")
    print("--- Please create a .env file with: GOOGLE_API_KEY=your_key_here")
else:
    print("--- DEBUG: API key loaded successfully")
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-pro')
# ---

app = FastAPI()

# Allow CORS for the React frontend
origins = ["http://localhost:3000"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create a directory for uploads
UPLOAD_DIRECTORY = "./uploads"
if not os.path.exists(UPLOAD_DIRECTORY):
    os.makedirs(UPLOAD_DIRECTORY)

# --- NEW ENDPOINT: To generate interview questions ---
@app.get("/api/get-questions/{job_role}")
async def get_interview_questions(job_role: str):
    """
    Generates interview questions for a specific job role using the LLM.
    """
    print("--- DEBUG: Received request for job role:", job_role) # Debug print
    
    # --- START OF FIX & DEBUGGING ---
    try:
        # Verify API key is loaded
        if not os.getenv("GOOGLE_API_KEY"):
            print("--- FATAL ERROR: GOOGLE_API_KEY not found in .env file.")
            return {"error": "Server is missing API key configuration."}
        
        prompt = f"""
        You are an expert hiring manager. Generate 5 common but insightful interview questions for a '{job_role}' position.
        Provide the response ONLY as a JSON array of strings, with no other text, explanation, or markdown backticks.
        Example format: ["Question 1?", "Question 2?", "Question 3?"]
        """
        response = model.generate_content(prompt)
        
        print("--- DEBUG: Raw response from LLM:", response.text) # Debug print
        
        # Clean the response text to ensure it is valid JSON
        cleaned_text = response.text.strip().replace("`", "")
        if cleaned_text.startswith("json"):
             cleaned_text = cleaned_text[4:].strip()
        
        # Parse the JSON to ensure it's valid before sending
        parsed_questions = json.loads(cleaned_text)
        
        return parsed_questions # Return the parsed JSON directly
        
    except Exception as e:
        print(f"--- FATAL ERROR generating questions: {e}")
        
        # Fallback: Return demo questions if API fails
        demo_questions = {
            "Software Engineer": [
                "Tell me about yourself and your programming experience.",
                "What programming languages are you most comfortable with?",
                "Describe a challenging technical problem you solved recently.",
                "How do you approach debugging and testing your code?",
                "What interests you most about software development?"
            ],
            "Data Scientist": [
                "Walk me through your experience with data analysis and machine learning.",
                "How do you approach feature selection in a machine learning project?",
                "Describe a time when you had to work with messy or incomplete data.",
                "What's your experience with different machine learning algorithms?",
                "How do you evaluate the performance of your models?"
            ],
            "Product Manager": [
                "Tell me about your product management experience and approach.",
                "How do you prioritize features in a product roadmap?",
                "Describe a time when you had to make a difficult product decision.",
                "How do you gather and analyze user feedback?",
                "What's your experience working with engineering and design teams?"
            ]
        }
        
        # Return demo questions for common roles, or generic questions
        if job_role.lower() in [key.lower() for key in demo_questions.keys()]:
            for key, questions in demo_questions.items():
                if key.lower() == job_role.lower():
                    print(f"--- Using demo questions for {job_role}")
                    return questions
        
        # Generic fallback questions
        generic_questions = [
            f"Tell me about your experience in {job_role}.",
            f"What skills do you think are most important for a {job_role}?",
            f"Describe a challenging project you worked on in {job_role}.",
            f"How do you stay updated with industry trends in {job_role}?",
            f"What interests you most about working as a {job_role}?"
        ]
        
        print(f"--- Using generic demo questions for {job_role}")
        return generic_questions
    # --- END OF FIX & DEBUGGING ---

@app.post("/api/analyze-interview/", response_model=AnalysisResult)
async def analyze_interview_video(video: UploadFile = File(...)):
    """
    Endpoint to receive a video, save it, and analyze it.
    """
    temp_video_path = os.path.join(UPLOAD_DIRECTORY, video.filename)
    
    # Save the uploaded video file temporarily
    with open(temp_video_path, "wb") as buffer:
        shutil.copyfileobj(video.file, buffer)
    
    # Get analysis results from the AI processor
    analysis_result = analyze_communication(temp_video_path)
    
    # Optional: Clean up the saved file
    os.remove(temp_video_path)
    
    return analysis_result
