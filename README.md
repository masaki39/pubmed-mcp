# Overview

This repository provides an MCP server that utilizes the PubMed API to perform query searches and retrieve efetch XML results. This is created for personal use. I use Cursor as the MCP client.

- [For Server Developers - Model Context Protocol](https://github.com/modelcontext/modelcontextprotocol)

# Prerequisites

- uv (Python package manager)
- Git
- Recommended: Python 3.12 or higher (lower versions may work but are untested)

# Installation

## Quick Start

Confirm this command works on your terminal(macOS/Linux) or command prompt/powershell(Windows).

```bash
uvx git+https://github.com/masaki39/pubmed-mcp
```

Add the following to your `mcpServers` configuration in your MCP client.

```json
{
  "mcpServers": {
    "pubmed-mcp": {
      "command": "uvx",
      "args": ["git+https://github.com/masaki39/pubmed-mcp"]
    }
  }
}
```

## Local Installation

Set up your environment by running the following commands:

```bash
git clone https://github.com/masaki39/pubmed-mcp
cd pubmed-mcp
uv venv
source .venv/bin/activate
uv pip install -r pyproject.toml
```

Example `mcpServers` configuration (replace `path/to/pubmed-mcp` with your actual cloned directory):

```json
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

