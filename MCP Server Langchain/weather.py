from mcp.server.fastmcp import FastMCP

mcp=FastMCP("Weather")

@mcp.tool()
async def get_weather(location:str) -> str:
    """Get the Weather Location"""
    return "it's always heat stroke in karachi" # here we can right any code in respect of api for testing we hard coded but we can use external api call

if __name__=="__main__":
# "streamable-http" it run on api like http:localhost:8000/mcp not cmd itself
    mcp.run(transport="streamable-http")