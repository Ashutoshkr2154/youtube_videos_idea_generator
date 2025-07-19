import requests
import os
from dotenv import load_dotenv

# Load API Key
load_dotenv()
YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")

def get_youtube_trending_videos(topic="AI", region="US"):
    url = "https://www.googleapis.com/youtube/v3/search"
    params = {
        "part": "snippet",
        "q": topic,
        "regionCode": region,
        "type": "video",
        "maxResults": 5,
        "order": "viewCount",
        "key": YOUTUBE_API_KEY
    }

    response = requests.get(url, params=params)
    data = response.json()

    # ✅ Debug: Print raw response
    print("\n✅ RAW RESPONSE:\n", data)

    if "items" in data:
        return [
            {"title": video["snippet"]["title"], "url": f"https://www.youtube.com/watch?v={video['id']['videoId']}"}
            for video in data["items"]
        ]

    return []


