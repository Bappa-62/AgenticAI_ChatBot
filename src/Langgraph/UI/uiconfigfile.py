from configparser import ConfigParser
class Config:
    def __init__(self, config_file='/Users/bappa_62/Documents/Agentic AI Projects/src/Langgraph/UI/uiconfigfile.ini'):
        self.config = ConfigParser()
        self.config.read(config_file)

    def get_llm_model(self):
        return self.config['DEFAULT']['LLM_OPTIONS'].split(', ')

    def get_page_title(self):
        return self.config['DEFAULT']['PAGE_TITLE']

    def get_usecase(self):
        return self.config['DEFAULT']['USECASE'].split(', ')

    def get_groq_models(self):
        return self.config['DEFAULT']['GROQ_MODELS'].split(', ')

    def get_openai_models(self):
        return self.config['DEFAULT']['OPENAI_MODELS'].split(', ')
    



