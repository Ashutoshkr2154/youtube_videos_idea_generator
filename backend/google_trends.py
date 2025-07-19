import requests
import os
from dotenv import load_dotenv
# from google_trends import get_trending_keywords  # <-- Remove this line
# Load API Key
load_dotenv()
SERPAPI_KEY = os.getenv("SERPAPI_KEY")

def get_trending_keywords(topic="artificial intelligence"):
    url = "https://serpapi.com/search"
    params = {
        "engine": "google_trends",
        "q": topic,
        "hl": "en",
        "date": "today 12-m",
        "tz": "420",
        "data_type": "RELATED_QUERIES",
        "api_key": SERPAPI_KEY
    }

    response = requests.get(url, params=params)
    data = response.json()

    # ✅ Debug: Print raw response
    print("\n✅ RAW RESPONSE:\n", data)

    if "related_queries" in data:
        # ✅ Filter only AI-related keywords
        keywords = [
            item["query"] for item in data["related_queries"]["top"][:10]
            if "ai" in item["query"].lower() or "artificial intelligence" in item["query"].lower()
        ]
        return keywords

    return []