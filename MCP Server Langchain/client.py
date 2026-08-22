from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.agents import create_agent
from langchain_groq import ChatGroq

from dotenv import load_dotenv
load_dotenv()

import asyncio

async def main():
    client=MultiServerMCPClient(
        {
            "math":{
                "command":"python",
                "args":["mathserver.py"], # ensure absolute path
                "transport":"stdio",
            },
            "weather":{
                "url":"http://127.0.0.1:8000/mcp",
                "transport":"streamable_http"
            },
        }
    )
    import os
    os.environ["GROQ_API_KEY"]= os.getenv("GROQ_API_KEY")
    tools= await client.get_tools()
    model=ChatGroq(model="openai/gpt-oss-20b")
    agent=create_agent(
        model,tools
    )

    math_response= await agent.ainvoke(
        {"messages": [{"role":"user","content":"what is (20 + 20) * 98"}]}
    )
    print("Math response: ", math_response["messages"][-1].content)

    weather_response= await agent.ainvoke(
        {"messages": [{"role":"user","content":"what is the weather of karachi"}]}
    )
    print("Weather response: ", weather_response["messages"][-1].content)

asyncio.run(main())