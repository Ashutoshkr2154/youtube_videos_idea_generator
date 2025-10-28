from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware  # <-- 1. IMPORTED THIS
import os
from dotenv import load_dotenv
import requests

# 2. FIXED IMPORTS (removed the leading dot '.')
from google_trends import get_trending_keywords
from youtube_trends import get_youtube_trending_videos

# Load environment variables from .env file
load_dotenv()

# Set up the EURI API key
EURI_API_KEY = os.getenv("EURI_API_KEY")
if not EURI_API_KEY:
    raise ValueError("EURI API key is missing. Please check your .env file.")

# Set up the FastAPI app
app = FastAPI()

# 3. ADDED CORS MIDDLEWARE BLOCK
# This allows your frontend (on a different URL) to call your backend
origins = [
    "http://localhost:8501",  # For local Streamlit testing
    "https://your-frontend-app-name.onrender.com"  # <-- IMPORTANT: REPLACE THIS
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, etc.)
    allow_headers=["*"],
)


@app.get('/generate_ideas/')
def generate_video_ideas(
    topic: str = Query(..., title="Topic"),
    audience: str = Query("Beginners", title="Target Audience"),
    region: str = Query("US", title="Region"),
):
    # Fetch trending keywords
    trending_keywords = get_trending_keywords(topic)    
    if not trending_keywords:
        trending_keywords = ["No trending keywords found for this topic"]
    
    # Fetch trending YouTube videos
    trending_videos = get_youtube_trending_videos(topic, region)
    if not trending_videos:
        trending_videos = [{"title": "No Trending Videos Found", "url": "#"}]
        
    # Prepare the prompt for EURI API
    prompt = f"""
    Generate 5 engaging YouTube video ideas on '{topic}' for '{audience}' that are currently trending.
    Consider these trending keywords: {', '.join(trending_keywords)}.
    Use insights from these trending YouTube videos: {', '.join(video['title'] for video in trending_videos)}.
    """
    
    # Prepare the request to the EURI API
    EURI_API_URL = "https://api.euron.one/api/v1/euri/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {EURI_API_KEY}",
    }
    data = {
        "messages": [{"role": "user", "content": prompt}],
        "model": "gpt-4.1-nano"
    }
    
    try:
        # Make the POST request to the EURI API
        response = requests.post(EURI_API_URL, headers=headers, json=data)
        response.raise_for_status()  # Raise an error for bad status codes
        ideas = response.json().get('choices')[0]['message']['content'].strip()
    except Exception as e:
        ideas = f"EURI API Error: {str(e)}"
        
    return {
        "trending_keywords": trending_keywords,
        "trending_videos": trending_videos,
        "ideas": ideas
    }

# To run the FastAPI app, use: uvicorn main:app --reload