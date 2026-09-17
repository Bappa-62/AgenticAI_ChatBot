from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.prompts import ChatPromptTemplate
from src.Langgraph.State.State import State

class NewsNode:
    def __init__(self,llm):
        """
        Initialize the NewsNode with API Key for Tavily and LLM Model.
        """
        self.tavily = TavilySearchResults()
        self.llm = llm
        ## self.state = {}
    def fetch_news(self,state: State) -> dict:
        """
          Fetch news for the given topic.
        Args: 
             state(dict) : The state dictionary containing frequency.

        Returns: 
             dict : Updated state with relavant News.
        """
        freq = state['frequency'].lower()
        keyword = state['keyword'].lower()
        time_range_map = {"daily":"d","weekly":"w","monthly":"m","yearly":"y"}
        days_map = {'daily':1,'weekly':7,'monthly':30,'yearly':365}
        
        result = self.tavily.invoke({
            "query": f"News about {keyword}"
        })

        ## Installed TavilySearchResults is returning a list directly.
        state['news_data'] = result #.get('results',[])
        ## self.state['news_data'] = state['news_data']
        return state
        
    def summarize(self,state : State) -> dict:
        """
          Summrize the news data.
        Args: 
             state(dict) : The state dictionary containing news data.

        Returns: 
             dict : Updated state with summrized news.
        """
        news_data = state['news_data']
        prompt = ChatPromptTemplate.from_messages([
            ("system",""" Summarize the search news into markdown format. For each item include:
            - Date in **YYYY-MM-DD** format in IST timezone
            - Concise sentences summary from latest news
            - Sort news by date wise(latest first)
            - Source URL as link
            Use format:
            ### [Date]
            - [Summary of the news in one sentence](URL)"""),
                     ('user',"{content}")
            ])
        
        content_data = "\n\n".join([
            f"Content: {item.get('content','')}\nURL: {item.get('url','')}\nDate:{item.get('published_date','')}"
            for item in news_data
        ])
        
        result = self.llm.invoke(prompt.format(content=content_data))
        state['summary'] = result.content
        return state


    def save_results(self,state: State) -> dict:
        freq = state['frequency'].lower()
        summary = state['summary']
        filename = f"./Summarized_News/{freq}_summary.md"
        with open(filename,"w")as f:
            f.write(f"**{freq.capitalize()} News Summary**\n\n")
            f.write(summary) 
        return state 









        




