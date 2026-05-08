import streamlit as st
from agent import generate_research_summary
from fpdf import FPDF
import requests

# --- Page Setup ---
st.set_page_config(page_title="AI Research Assistant", page_icon="🔬")
st.title("🔬 AI Research Assistant")
st.write("Enter any research topic and get a structured summary powered by AI.")

# --- Input Section ---
topic = st.text_input("Enter your research topic:", placeholder="e.g. Black Holes, Diabetes, Climate Change")

def get_wikipedia_content(topic: str) -> str:
    try:
        search_url = "https://en.wikipedia.org/w/api.php"
        params = {
            "action": "query",
            "list": "search",
            "srsearch": topic,
            "format": "json",
            "srlimit": 1
        }
        response = requests.get(search_url, params=params, timeout=10)
        data = response.json()
        results = data.get("query", {}).get("search", [])
        if not results:
            return f"No Wikipedia results found for '{topic}'"
        page_title = results[0]["title"]
        summary_resp = requests.get(
            f"https://en.wikipedia.org/api/rest_v1/page/summary/{page_title.replace(' ', '_')}",
            timeout=10
        )
        return summary_resp.json().get("extract", "No content found.")
    except Exception as e:
        return f"Search error: {str(e)}"

# --- Generate Button ---
if st.button("Generate Research Summary"):

    # Check if user typed something
    if not topic.strip():
        st.error("⚠️ Please enter a research topic before clicking Generate.")
    
    else:
        # Show a loading spinner while generating
        with st.spinner("Researching and generating summary... please wait ⏳"):
            try:
                # Call the agent to get the summary
                wiki_context = get_wikipedia_content(topic)
                summary = generate_research_summary(topic)

                # Display the summary on screen
                st.success("✅ Summary Generated!")
                st.markdown(summary)

                # --- Export as TXT ---
                st.download_button(
                    label="⬇️ Download as .txt",
                    data=summary,
                    file_name=f"{topic}_research.txt",
                    mime="text/plain"
                )

                # --- Export as PDF ---
                pdf = FPDF()
                pdf.add_page()
                pdf.set_font("Arial", size=12)
                # Clean special characters that fpdf can't handle
                clean_summary = summary.encode("latin-1", errors="replace").decode("latin-1")
                pdf.multi_cell(0, 10, clean_summary)
                pdf_output = bytes(pdf.output())

                st.download_button(
                    label="⬇️ Download as .pdf",
                    data=pdf_output,
                    file_name=f"{topic}_research.pdf",
                    mime="application/pdf"
                )

            except Exception as e:
                st.error(f"❌ Something went wrong: {str(e)}")