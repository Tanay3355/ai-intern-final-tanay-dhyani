# 🔬 AI Research Assistant

An AI-powered research tool that generates structured summaries on any topic using **Google Gemini AI** and **Wikipedia**. Built with Python and Streamlit.
Link - https://ai-research-assistant-by-tanay.streamlit.app
***

## 🚀 Features

- 🔍 **Real-time Wikipedia search** — fetches up-to-date content on any topic
- 🤖 **Gemini AI summarization** — generates well-structured research summaries
- 📄 **Export options** — download your summary as `.txt` or `.pdf`
- ⚡ **Simple UI** — clean Streamlit interface, no setup needed for users

***

## 📋 Output Format

Every generated summary includes:
1. **Overview** — What the topic is
2. **Key Facts** — Important data points
3. **Current Research / Developments** — Latest findings
4. **Conclusion** — Summary and takeaways

***

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core language |
| Streamlit | Web UI |
| Google Gemini API (`gemini-2.5-flash`) | AI summarization |
| Wikipedia REST API | Real-time research data |
| fpdf2 | PDF export |
| MCP (Model Context Protocol) | AI tool integration architecture |

***

## ⚙️ Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/AI-Research-Assistant.git
cd AI-Research-Assistant
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Set up your API key

Create a `.env` file in the root folder:
```
GEMINI_API_KEY=your_gemini_api_key_here
```

Get your free API key at: [aistudio.google.com](https://aistudio.google.com)

### 4. Run the app
```bash
python -m streamlit run app.py
```

Open your browser at `http://localhost:8501`

***

## 🔐 Environment Variables

| Variable | Description |
|---|---|
| `GEMINI_API_KEY` | Your Google Gemini API key |


***

## 📦 Requirements

- Python 3.9+
- Internet connection (for Wikipedia and Gemini API)

***
