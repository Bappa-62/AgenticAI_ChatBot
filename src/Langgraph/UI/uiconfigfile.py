from configparser import ConfigParser
import os
class Config:
    def __init__(self):
        self.config = ConfigParser()
        config_file = os.path.join(os.path.dirname(__file__),'uiconfigfile.ini') 
        self.config.read(config_file)

        st = self.config.read(config_file)
        print("CONFIG PATH:", config_file)
        print("CONFIG FILE EXISTS:", os.path.exists(config_file))
        print("CONFIG DEFAULTS:", dict(self.config.defaults()))

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
    