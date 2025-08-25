 
# 🔍 AI Research Assistant

An agentic AI system that automatically searches, summarizes, and saves research insights.

## 🚀 Features

- **Autonomous Research**: AI searches the web and processes results automatically
- **Intelligent Summarization**: Extracts key insights using advanced LLMs
- **Auto-Save Notes**: Automatically stores research in local database
- **Multiple Interfaces**: Web UI (Streamlit) and CLI options
- **Free & Local**: Works with free APIs and runs locally

## 🛠️ Tech Stack

- **Backend**: Python, LangChain
- **AI Models**: OpenAI GPT-3.5 or Ollama Llama-3
- **Search**: DuckDuckGo (free) or SerpAPI
- **Storage**: SQLite database
- **Frontend**: Streamlit web app
- **Deployment**: Local or GitHub Codespaces

## 📦 Quick Start

### Option 1: GitHub Codespaces (Easiest)
1. Click the "Code" button above
2. Select "Codespaces" → "Create codespace"
3. Wait for environment to load
4. Run: `pip install -r requirements.txt`
5. Start the app: `streamlit run ui/streamlit_app.py`

### Option 2: Local Development
```bash
git clone https://github.com/yourusername/ai-research-assistant.git
cd ai-research-assistant
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
streamlit run ui/streamlit_app.py
