from mcp.server.fastmcp import FastMCP

mcp=FastMCP("Math")

@mcp.tool()
def add(a:int, b:int) -> int:
    """_summary_
    Add two numbers
    """
    return a+b

@mcp.tool()
def multiple(a:int, b:int) -> int:
    """_summary_
    Multiply two numbers
    """
    return a*b

# transport="stdio" tell the server to use standard input/output to recieve and response to tool function calls
# means it runs in cmd itself not in any api like http:localhost:8000/mcp
if __name__=="__main__":
    mcp.run(transport="stdio")