# Overview

This repository provides an MCP server that utilizes the PubMed API to perform query searches and retrieve efetch XML results. This README is intended for Mac/Linux users. For Windows users, please refer to the following link for more details:

- [For Server Developers - Model Context Protocol](https://github.com/modelcontext/modelcontextprotocol)

Cursor is used as the MCP client.

# Prerequisites

- Recommended: Python 3.12 or higher (lower versions may work but are untested)
- uv (Python package manager)
- Git

# Installation

Set up your environment by running the following commands:

```
git clone https://github.com/masaki39/pubmed-mcp
cd pubmed-mcp
uv venv
source .venv/bin/activate
uv pip install -r pyproject.toml
```

# How to Start the Server

Example `mcpServers` configuration (replace `path/to/pubmed-mcp` with your actual cloned directory):

```
{
  "mcpServers": {
    "pubmed-mcp": {
      "command": "uv",
      "args": ["--directory", "path/to/pubmed-mcp", "run", "pubmed-mcp.py"]
    }
  }
}
```

# Provided Commands

- `pubmed_search`: Search PubMed with a query and return efetch XML

# Command Details

- `pubmed_search`: Searches PubMed using the specified `query` parameter and returns efetch XML (returns up to 10 results per call, supports offset via `retstart`).

# License

This repository is licensed under the MIT License. See the LICENSE file for details.
