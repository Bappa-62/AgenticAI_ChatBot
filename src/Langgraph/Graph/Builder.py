from langgraph.prebuilt import tool_node
from langgraph.prebuilt import tools_condition, ToolNode
from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import MemorySaver
from src.Langgraph.State.State import State
from src.Langgraph.Nodes.ChatBot_Node import ChatBotNode
from src.Langgraph.Tool.Search import get_tools, create_tool_node
from src.Langgraph.Nodes.ChatBot_With_Tool import ChatBotWithToolNode
from src.Langgraph.Nodes.News_Summarize_Node import NewsNode


class GraphBuilder:
    def __init__(self,model):
        self.llm = model
        self.graph = StateGraph(State)

    def basic_ChatBot(self):
        """
            Builds a basic ChatBot graph using LangGraph.
            Initialising ChatBotNode and adds it to the graph using the ChatBotNode class.
            Adds edges from START to ChatBot and from ChatBot to END.
        """
        self.chatbot_node = ChatBotNode(self.llm)
        self.graph.add_node("ChatBot",self.chatbot_node.process)
        self.graph.add_edge(START,'ChatBot')
        self.graph.add_edge("ChatBot",END)

    def ChatBot_with_Tool(self):
        """
            Builds a ChatBot with Tool graph using LangGraph.
            Initialising ChatBotNode and adds it to the graph using the ChatBotNode class.
            Adds edges from START to ChatBot and from ChatBot to END.
        """
        Tools = get_tools()
        tool_node = create_tool_node(Tools)
        chatbot_with_tool_node = ChatBotWithToolNode(self.llm)
        self.graph.add_node("ChatBot",chatbot_with_tool_node.create_chatbot(Tools))
        self.graph.add_node("tools",tool_node)
        self.graph.add_edge(START,'ChatBot')
        self.graph.add_conditional_edges(
            "ChatBot",
            tools_condition
        )
        self.graph.add_edge("tools","ChatBot")
    
    def News_Summarize(self):
        """
          News Summarizer with Tavily search and provide response in a more constructive ways.
        """
    ## Adding Nodes    
        news_node = NewsNode(self.llm)
        self.graph.add_node("fetch_news",news_node.fetch_news)
        self.graph.add_node("summarize",news_node.summarize)
        self.graph.add_node("save_results",news_node.save_results)

    ## Adding Edge
        self.graph.set_entry_point("fetch_news")
        self.graph.add_edge("fetch_news","summarize")
        self.graph.add_edge("summarize","save_results")
        self.graph.add_edge("save_results",END)

    def setUpGraph(self,usecase):
        """ SetUp for the graph for the specific uase cases """
        if usecase == 'Basic ChatBot':
            self.basic_ChatBot()
        elif usecase == 'ChatBot with Tool':
            self.ChatBot_with_Tool()
        elif usecase == "News Summarizer Bot":
            self.News_Summarize()
        return self.graph.compile()




