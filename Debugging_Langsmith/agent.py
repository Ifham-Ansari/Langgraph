from typing import Annotated
from typing_extensions import TypedDict
from langgraph.graph import START, END
from langgraph.graph.state import StateGraph
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode, tools_condition
from langchain_core.tools import tool
from langchain_core.messages import BaseMessage
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["GROQ_API_KEY"]= os.getenv("GROQ_API_KEY")
os.environ["LANGCHAIN_API_KEY"]= os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGSMITH_TRACING"]="true"
os.environ["LANGSMITH_PROJECT"]="Test_Langraph_Studio" 


llm=ChatGroq(model="openai/gpt-oss-20b")


class State(TypedDict):
    messages:Annotated[list[BaseMessage],add_messages]


def make_tool_graph(): 

    # graph with tool call
    @tool
    def add(a:float, b:float):
        """Add Two Numbers"""
        return a+b

    tool_node=ToolNode([add])
    tools=[add]
    llm_with_tool=llm.bind_tools([add])

    def call_llm_model(state:State):
        return {"messages":[llm_with_tool.invoke(state["messages"])]}

    builder=StateGraph(State)
    builder.add_node("tool_calling_llm",call_llm_model)
    builder.add_node("tools",ToolNode(tools))

    ## EDGES
    builder.add_edge(START,"tool_calling_llm")
    builder.add_conditional_edges(
        "tool_calling_llm",
        ## decide if need to call tool or directly go to end
        tools_condition
    )
    # builder.add_edge("tools",END) # this directly give the tools output because after tool call it ends
    builder.add_edge("tools","tool_calling_llm")


    ## COMPILE GRAPH
    graph=builder.compile()
    return graph

tool_agent=make_tool_graph()


# all above code we copy pasted from debugging.ipynb we just make complete code under single function name make_tool_graph() and we call it as
# tool_agent. We done this to test it on langgraph studio for that we need library name langgraph-cli[inmem] by using it we can run any local 
# graph in langgraph studio or langsmith cloud for that we also needed one file name langgraph.json inside which we have some configurations 
# like dependencies, graph, calling object in our case tool_agent, also the file name which is agent.py in my case and lastly route to .env
# we run it as langgraph dev and it will use langgraph.json configrations to run, then in cmd than multiple links will be available in cmd when
# we click it will open langgraph studio and there we can see complete graph, test the flow/graph give the input and can see the flow there is 
# also an interrupt option between the flow which can be needed depending on project

# Also it give a complete documentation in http://127.0.0.1:2024/docs when we run and there we can see all the api's we can also convert/generate
# mcp we can test requests see code snipets curl commands like we do in postman

# all this is use for debugging/monitoring and we can debug/monitor both by langraph studio and also by langsmith


