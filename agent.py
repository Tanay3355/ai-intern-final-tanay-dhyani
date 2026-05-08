# agent.py
import os
import requests
from dotenv import load_dotenv
from google import genai
import streamlit as st
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY") or st.secrets.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)


def get_wikipedia_content(topic: str) -> str:
    try:
        headers = {
            "User-Agent": "AI-Research-Assistant/1.0 (educational project; tanay@example.com)"
        }
        
        search_url = "https://en.wikipedia.org/w/api.php"
        params = {
            "action": "query",
            "list": "search",
            "srsearch": topic,
            "format": "json",
            "srlimit": 1
        }
        response = requests.get(search_url, params=params, headers=headers, timeout=10)
        data = response.json()
        results = data.get("query", {}).get("search", [])
        if not results:
            return f"No Wikipedia results found for '{topic}'"
        page_title = results[0]["title"]
        summary_resp = requests.get(
            f"https://en.wikipedia.org/api/rest_v1/page/summary/{page_title.replace(' ', '_')}",
            headers=headers,
            timeout=10
        )
        return summary_resp.json().get("extract", "No content found.")
    except Exception as e:
        return f"Search error: {str(e)}"


def generate_research_summary(topic: str) -> str:
    """
    Fetches Wikipedia context directly,
    then asks Gemini to generate a structured research summary.
    """

    # Step 1 — Fetch real Wikipedia data
    wiki_context = get_wikipedia_content(topic)

    # Step 2 — Build prompt for Gemini
    prompt = f"""
    You are an expert research assistant. Using the context below, 
    generate a well-structured research summary on the topic: "{topic}"

    Wikipedia Context:
    {wiki_context}

    Your summary must include these sections:
    1. Overview
    2. Key Facts
    3. Current Research / Developments
    4. Conclusion

    Write clearly and in detail. Use simple language.
    """

    # Step 3 — Send to Gemini and get response
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    # Step 4 — Return text
    return response.text