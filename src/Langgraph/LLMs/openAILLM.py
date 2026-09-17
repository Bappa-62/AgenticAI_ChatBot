import os
from langchain_openai import ChatOpenAI

class OpenAI_LLM:
    def __init__(self, user_controls_input):
        self.user_controls_input = user_controls_input
        self.openai_api_key = self.user_controls_input['OPENAI_API_KEY']
        self.openai_model = self.user_controls_input['selected_openai_model']
    
    def get_model(self):
        try:
            openai_api_key = self.user_controls_input["OPENAI_API_KEY"]
            selected_openai_model = self.user_controls_input['selected_openai_model'] 
            if openai_api_key == '' and os.environ.get("OPENAI_API_KEY") == '':
                print("Please Enter the OPENAI API KEY")
            llm = ChatOpenAI(openai_api_key=openai_api_key, model=selected_openai_model)
        except Exception as e:
            raise ValueError(f"Error in OpenAI_LLM: {str(e)}")
        return llm
                