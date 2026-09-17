import os
from langchain_groq import ChatGroq

class GroqLLM:
    def __init__(self, user_controls_input):
        self.user_controls_input = user_controls_input
        self.groq_api_key = self.user_controls_input['GROQ_API_KEY']
        self.groq_model = self.user_controls_input['selected_groq_model']
    
    def get_model(self):
        try:
            groq_api_key = self.user_controls_input["GROQ_API_KEY"]
            selected_groq_model = self.user_controls_input['selected_groq_model'] 
            if groq_api_key == '' and os.environ.get("GROQ_API_KEY") == '':
                print("Please Enter the GROQ API KEY")
            llm = ChatGroq(groq_api_key=groq_api_key, model= selected_groq_model)
        except Exception as e:
            raise ValueError(f"Error in GroqLLM: {str(e)}")
        return llm
                