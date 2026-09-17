from src.Langgraph.State.State import State

class ChatBotWithToolNode:
    """
     ChatBot with Tool Integration.
    """
    def __init__(self,model):
        self.llm = model
    
## If there is no explicit tool Integration
    def process(self,state:State) -> dict:
        """
        Process the input and generate the output with tool integration.
        """
        user_input = state['messages'][-1] if state['messages'] else ''
        llm_response = self.llm.invoke([{"role":"user","content":user_input}])
        tools_response = f"Tool integration for : {user_input}"
        return {"messages":[llm_response,tools_response]}

## If we are binding the tools
    def create_chatbot(self, tools):
        """
         Returns a ChatBot node function.
        """
        llm_with_tools = self.llm.bind_tools(tools)
        def chatbot_node(state:State):
            """
            ChatBot logic for processing the request with tool integration.
            """
            response = llm_with_tools.invoke(state['messages'])
            return {'messages':response}
        return chatbot_node


        
    