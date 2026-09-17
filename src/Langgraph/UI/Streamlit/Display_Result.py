from pandas.tseries import frequencies
from langchain_core.messages import AIMessage, HumanMessage, ToolMessage
import json
import streamlit as st
class DisplayResult:
    def __init__(self, Graph, usecase, user_message, frequency, keyword):
        self.Graph = Graph
        self.usecase = usecase
        self.user_message = user_message
        self.frequency = frequency
        self.keyword = keyword

    def display_result_on_ui(self):
        usecase = self.usecase
        user_message = self.user_message
        Graph = self.Graph

        if usecase == 'Basic ChatBot':
            for event in Graph.stream({'messages': ('user',user_message)}):
                for val in event.values():
                    with st.chat_message("user"):
                        st.write(user_message)
                    with st.chat_message("assistant"):
                        st.write(val['messages'].content)

        elif usecase == 'ChatBot with Tool':
            initial_msg = {'messages':[user_message]}
            response = Graph.invoke(initial_msg)

            for msg in response['messages']:
                if type(msg) == HumanMessage:
                    with st.chat_message("user"):
                        st.write(msg.content)
                elif type(msg) == ToolMessage:
                    with st.chat_message("tool"):
                        st.write("Tool Call Start")
                        st.write(msg.content)
                        st.write("Tool Call Finish")
                elif type(msg) == AIMessage:
                    with st.chat_message("assistant"):
                        st.write(msg.content)
                
        elif usecase == "News Summarizer Bot":
            msg = self.user_message

            with st.spinner(f"Fetching and summarizing news on {self.keyword}..."):
                result = Graph.invoke({'messages':[('user',msg)],
                                      'frequency':self.frequency,
                                      'keyword':self.keyword
                                      })
                try:
                    path = f"./Summarized_News/{self.frequency.lower()}_summary.md"
                    with open(path,'r') as f:
                        markdown_content = f.read()
                        st.markdown(markdown_content,unsafe_allow_html=True) 
                except FileNotFoundError:
                    st.error(f"Error: Summary file not found for {self.frequency}")
                except Exception as e:
                    st.error(f"Error: Failed to display news -{str(e)}")







        

