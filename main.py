from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("pubmed-mcp")

# Constants
PUBMED_API_BASE = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"
USER_AGENT = "pubmed-mcp/1.0"

# MCP server
@mcp.tool()
async def pubmed_search(query: str, retstart: int = 0, retmax: int = 10) -> Any:
    """Search PubMed for a given query and return raw efetch XML. To improve search accuracy, you can use the following PubMed search syntax:

    - Keyword Search: Enter words or phrases separated by spaces.
    - Phrase Search: Use double quotes (" ") for exact phrase matching. Example: "heart attack"
    - Field Tags: Search in specific fields (e.g., [TI] Title, [AU] Author, [AB] Abstract, [TA] Journal Title Abbreviation). Example: "cancer[TI]"
    - Boolean Operators: Combine search terms using AND, OR, NOT. AND is applied by default. Examples: "cancer AND therapy", "pain OR ache", "antibiotics NOT penicillin"

    You can also combine multiple syntax elements. Example: "(\"cancer\" OR \"tumor\")[TI] AND \"chemotherapy\"[TIAB]"

    Use the retstart and retmax parameters to control the range of results retrieved.
    """
    # Get ID list via esearch
    url = f"{PUBMED_API_BASE}/esearch.fcgi"
    params = {
        "db": "pubmed",
        "term": query,
        "retmode": "json",
        "retmax": retmax,
        "retstart": retstart,
    }
    headers = {"User-Agent": USER_AGENT}
    async with httpx.AsyncClient() as client:
        response = await client.get(url, params=params, headers=headers)
        response.raise_for_status()
        esearch_result = response.json()
        id_list = esearch_result.get("esearchresult", {}).get("idlist", [])
        if not id_list:
            return ""
        # Get detailed information via efetch
        efetch_url = f"{PUBMED_API_BASE}/efetch.fcgi"
        efetch_params = {
            "db": "pubmed",
            "id": ",".join(id_list),
            "retmode": "xml",
        }
        efetch_response = await client.get(efetch_url, params=efetch_params, headers=headers)
        efetch_response.raise_for_status()
        return efetch_response.text

def main():
    try:
        print("Attempting to start the Pubmed MCP server...")
        mcp.run(transport='stdio')
    except Exception as e:
        print(f"An error occurred during Pubmed MCP server startup or execution: {e}")

if __name__ == "__main__":
    main()