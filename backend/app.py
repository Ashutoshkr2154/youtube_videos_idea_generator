import streamlit as st
import requests
# Backend API URL
API_URL = "http://127.0.0.1:8000/generate_ideas/"
st.title("🎬 AI-Powered YouTube Idea Generator")
# Input fields
topic = st.text_input("Enter a topic:", "Artificial Intelligence")
audience = st.selectbox("Target Audience:", ["Beginners", "Intermediate", "Experts"])
region = st.text_input("YouTube Region (e.g., US, IN, UK):", "US")
# Submit button
if st.button("Generate Video Ideas"):
    params = {"topic": topic, "audience": audience, "region": region}
    response = requests.get(API_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        # ✅ Trending Keywords
        st.subheader("🔥 Trending Keywords")
        if data["trending_keywords"]:
            st.write(", ".join(data["trending_keywords"]))
        else:
            st.write("No trending keywords found.")
        # ✅ Trending YouTube Videos
        st.subheader("🎥 Trending YouTube Videos")
        for video in data["trending_videos"]:
            st.markdown(f"📌 [{video['title']}]({video['url']})")
        # ✅ AI-Generated Video Ideas
        st.subheader("✨ AI-Generated Video Ideas")
        if "❌ OpenAI API Error" in data["ideas"]:
            st.error("OpenAI API Error: Please check your API key.")
        else:
            st.success(data["ideas"])
    else:
        st.error("❌ API request failed. Please check backend logs.")

