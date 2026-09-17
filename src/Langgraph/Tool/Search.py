from openai import max_retries
from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.prebuilt import ToolNode

def get_tools():
    """
      Return the list of tools used by the chatbot for specific tasks.
      In this case, we are using TavilySearchResults tool for web search.
    """
    tools = [TavilySearchResults(max_results =2)]
    return tools

def create_tool_node(tools):
    """
     Creates and return a tool node for the graph.
    """
    return ToolNode(tools)
    