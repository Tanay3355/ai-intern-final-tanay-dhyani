# mcp_server.py
import requests
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Research Assistant MCP Server")

@mcp.tool()
def search_web(query: str) -> str:
    """Search Wikipedia for information about a given research topic"""
    try:
        # Use Wikipedia's search API first to find the right page
        search_url = "https://en.wikipedia.org/w/api.php"
        params = {
            "action": "query",
            "list": "search",
            "srsearch": query,
            "format": "json",
            "srlimit": 1
        }
        response = requests.get(search_url, params=params, timeout=10)
        data = response.json()
        
        # Get the top result's page title
        results = data.get("query", {}).get("search", [])
        if not results:
            return f"No results found for '{query}'"
        
        page_title = results[0]["title"]
        
        # Now fetch the actual summary
        summary_url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{page_title.replace(' ', '_')}"
        summary_response = requests.get(summary_url, timeout=10)
        summary_data = summary_response.json()
        
        return summary_data.get("extract", "No content found.")
    
    except Exception as e:
        return f"Search error: {str(e)}"

if __name__ == "__main__":
    mcp.run()