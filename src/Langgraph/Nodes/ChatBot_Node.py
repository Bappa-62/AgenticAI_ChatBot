from src.Langgraph.State.State import State

class ChatBotNode:
    """
      Basic ChatBot Node Implementation.
    """
    def __init__(self, model):
        self.llm = model

    def process(self,state:State) -> dict:
        """
         Process the input message and return the response.
        """
        return {"messages":self.llm.invoke(state["messages"])}