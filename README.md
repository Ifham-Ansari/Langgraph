# LangGraph Examples

Small experiments with LangGraph, LangSmith, LangChain, and the Model Context Protocol (MCP).

## Contents

- `basic chatbot langraph/chatbot.ipynb`: basic LangGraph chatbot notebook.
- `Debugging_Langsmith/agent.py`: tool-calling graph for LangGraph Studio and LangSmith tracing.
- `Debugging_Langsmith/debugging.ipynb`: notebook version of the debugging example.
- `MCP Server Langchain/`: MCP math and weather servers plus a LangChain client.

## Setup

Python 3.11 or newer is required. From the repository root, create and activate a virtual environment, then install the root dependencies:

```powershell
python -m pip install -r requirements.txt
```

Install the additional MCP dependencies before running the MCP demo:

```powershell
python -m pip install -r 'MCP Server Langchain/requirements.txt'
```

Copy the environment template and add your own API keys:

```powershell
Copy-Item .env.example .env
```

Required variables depend on the example:

- `GROQ_API_KEY` for the Groq-backed agents.
- `LANGCHAIN_API_KEY` for LangSmith tracing.
- `TAVILY_API_KEY` for Tavily integrations.

Never commit `.env` or real API keys.

## Run The Examples

### Basic chatbot

Open `basic chatbot langraph/chatbot.ipynb` in VS Code and select the project Python environment. Run the notebook cells in order.

### LangSmith debugging agent

Start LangGraph's local development server from the example directory:

```powershell
Set-Location 'Debugging_Langsmith'
langgraph dev
```

The command prints links for LangGraph Studio and the local API documentation. The graph is configured in `Debugging_Langsmith/langgraph.json`.

### MCP demo

Start the weather MCP server in one terminal:

```powershell
Set-Location 'MCP Server Langchain'
python weather.py
```

Then run the client from a second terminal:

```powershell
Set-Location 'MCP Server Langchain'
python client.py
```

The client starts the math server over stdio and connects to the weather server at `http://127.0.0.1:8000/mcp`.

## Project Structure

```text
basic chatbot langraph/   Basic chatbot notebook
Debugging_Langsmith/      LangGraph Studio and LangSmith example
MCP Server Langchain/     MCP servers and LangChain client
src/langraph/             Python package source
```
