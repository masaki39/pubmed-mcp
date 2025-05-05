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
    """Search PubMed for a given query and return raw efetch XML (returns a fixed batch of retmax results, supports resuming via retstart offset)"""
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

if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')