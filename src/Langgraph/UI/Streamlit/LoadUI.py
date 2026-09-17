import streamlit as st
import os
from src.Langgraph.UI.uiconfigfile import Config

class LoadStreamLitUI:
    def __init__(self):
        self.config = Config()
        self.user_controls={}

    def load_streamlit_ui(self):
        st.set_page_config(page_title="🧠 "+self.config.get_page_title(), layout="wide")
        st.header("🧠 "+self.config.get_page_title())
        st.session_state.keyword = ""

        with st.sidebar:
            ## Get options from config
            llm_options = self.config.get_llm_model()
            usecase_options = self.config.get_usecase()
        
            ## LLM Selection
            self.user_controls['selected_llm'] = st.selectbox("Select LLM", llm_options)

            if self.user_controls['selected_llm'] == 'Groq':
                model_options = self.config.get_groq_models()
                self.user_controls['selected_groq_model'] = st.selectbox('Select Model', model_options)
                self.user_controls["GROQ_API_KEY"] = st.session_state['GROQ_API_KEY'] = st.text_input('API_KEY', type='password')
                if not self.user_controls['GROQ_API_KEY']:
                    st.warning("🚫 Please enter your GROQ API key.You can create it by referring: https://console.groq.com/keys")

            elif self.user_controls['selected_llm'] == 'OpenAI':
                model_options = self.config.get_openai_models()
                self.user_controls['selected_openai_model'] = st.selectbox('Select Model', model_options)
                self.user_controls["OPENAI_API_KEY"] = st.session_state['OPENAI_API_KEY'] = st.text_input('API_KEY', type='password')
                if not self.user_controls['OPENAI_API_KEY']:
                    st.warning("🚫 Please enter your OPENAI API key.You can create it by referring: https://platform.openai.com/api-keys")
            ## Usecase Selection
            self.user_controls['selected_usecase'] = st.selectbox("Select Usecases", usecase_options)

            ## if self.user_controls['selected_usecase'] == 'Basic ChatBot':
            self.user_controls['selected_basic_chatbot_model'] = st.selectbox('Select Model', ['qwen/qwen3.8-27b', 'meta-llama/llama-prompt-guard-2-22m', 'gpt-3.5-turbo', 'gpt-4o', 'gpt-4o-mini'])  
            if self.user_controls['selected_usecase'] == 'ChatBot with Tool' or self.user_controls['selected_usecase'] == 'News Summarizer Bot':
                ## self.user_controls['selected_chatbot_with_tool_model'] = st.selectbox('Select Model', ['qwen/qwen3.8-27b', 'meta-llama/llama-prompt-guard-2-22m', 'gpt-3.5-turbo', 'gpt-4o', 'gpt-4o-mini'])
                os.environ["TAVILY_API_KEY"] = self.user_controls["TAVILY_API_KEY"] = st.session_state['TAVILY_API_KEY'] = st.text_input('TAVILY_API_KEY', type='password')
                if not self.user_controls['TAVILY_API_KEY']:
                    st.warning("🚫 Please enter your TAVILY API key.You can create it by referring: https://app.tavily.com/home")
            
            if self.user_controls['selected_usecase'] == 'News Summarizer Bot':
                st.sidebar.write("🗞️ News Summarizer Bot")
                with st.sidebar:
                    time = st.selectbox("🗓️ Select Time Duration", 
                                        ['Daily','Weekly', 'Monthly', 'Yearly'],
                                        index=0
                                        )
                    self.user_controls['frequency'] = time
                    keyword = st.selectbox("🌎 Enter the topic",
                                         ['AI & Generative AI 🤖',
                                           'Technology 💻',
                                           'Cybersecurity 🔐',
                                           'Cloud Computing ☁️',
                                           'Business & Finance 📈',
                                           'Sports🏏',
                                           'Movies & TV 🎬',
                                           'Gaming 🎮',
                                           'Music🎵'
                                           ])
                    self.user_controls['keyword'] = keyword
                    fetch_button = st.button(f"🌐 Fetch Latest News on {self.user_controls['keyword']} topic.",use_container_width=True)
                    if fetch_button:
                        self.user_controls['fetch_button'] = fetch_button
                        st.session_state.frequency = self.user_controls['frequency']
                        st.session_state.keyword = self.user_controls['keyword']

        return self.user_controls













