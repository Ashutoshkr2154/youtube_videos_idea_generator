# youtube_videos_idea_generator
## 🚀 How to Run the Project

This is an AI-powered YouTube Video Idea Generator using FastAPI (backend) and Streamlit (frontend). Follow the steps below to run it locally:

### 📦 1. Clone the Repository

```bash
git clone https://github.com/your-username/euron-yt-idea-generator.git
cd euron-yt-idea-generator
```

### 🧪 2. Create and Activate a Virtual Environment

```bash
conda create -n euron_yt_idea_generator python=3.10
conda activate euron_yt_idea_generator
```

### 📁 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 🔐 4. Add Environment Variables

Create a `.env` file in the **root directory** and add your API keys:

```
EURI_API_KEY=your_euri_api_key
YOUTUBE_API_KEY=your_youtube_api_key
SERAPI_KEY=your_serpapi_key
OPENAI_API_KEY=your_openai_api_key
```

> 📝 Make sure the `.env` file is placed **outside the `/backend` folder**, directly inside the root project folder.

---

### ⚙️ 5. Run the Backend (FastAPI)

```bash
uvicorn backend.main:app --reload
```

- The backend will run at: `http://127.0.0.1:8000`
- Swagger Docs available at: `http://127.0.0.1:8000/docs`

---

### 🎯 6. Run the Frontend (Streamlit)

In a **new terminal** (with the same environment activated), run:

```bash
streamlit run app.py
```

- This will open the frontend at: `http://localhost:8501`
- Enter your topic, audience, and region, then click **Generate Video Ideas**

---

### ✅ Example Output

- 🔥 Trending keywords
- 🎥 Top trending YouTube videos
- ✨ AI-generated video ideas (OpenAI)
