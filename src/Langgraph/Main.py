from langchain_core import output_parsers
import streamlit as st
from src.Langgraph.UI.Streamlit.LoadUI import LoadStreamLitUI 
from src.Langgraph.LLMs.groqLLM import GroqLLM
from src.Langgraph.LLMs.openAILLM import OpenAI_LLM
from src.Langgraph.Graph.Builder import GraphBuilder
from src.Langgraph.UI.Streamlit.Display_Result import DisplayResult
def load_langgraph_app():
    """
      Load and runs the Langgraph AgenticAI application with streamlit UI.
      This function initializes the UI, handles user input, configures the LLM model,
      sets up the graph based on the selected use case, and displays the output while
      implementing exception handling for robustness.
    """
    ### Load UI
    ui = LoadStreamLitUI()
    user_input = ui.load_streamlit_ui()
    if not user_input:
        st.error("Error: Failed to load user input from the UI.")
        return
    selected_llm = user_input.get('selected_llm')
    use_case = user_input.get('selected_usecase')
    if use_case == 'News Summarizer Bot':
        value = user_input.get('fetch_button')
    elif use_case == 'ChatBot with Tool' or use_case == 'Basic ChatBot':
        user_message = st.chat_input("Ask a Question!")
        value = user_message

    if value:
        try:
            ### Get LLM Model
            if(selected_llm == 'Groq'):
                llm_model = GroqLLM(user_input).get_model()
            elif(selected_llm=='OpenAI'):
                llm_model = OpenAI_LLM(user_input).get_model()
            else:
                st.error("❌ Unsupported LLM Model")
                return
            if not llm_model:
                st.error("Error: Failed to get LLM model.")
                return
            usecase = user_input.get('selected_usecase') 
            if usecase == None:
                st.error("Error: Failed to get usecase.")
                return
            frequency = user_input.get('frequency') 
            keyword = user_input.get('keyword')
            ## Graph Builder
            graph = GraphBuilder(llm_model)  
            try:
                Graph = graph.setUpGraph(usecase)
                if use_case == 'News Summarizer Bot':
                    DisplayResult(Graph,usecase,"",frequency,keyword).display_result_on_ui()
                elif use_case == 'ChatBot with Tool' or use_case == 'Basic ChatBot':
                    DisplayResult(Graph,usecase,user_message,frequency,keyword).display_result_on_ui()
            except Exception as e:
                st.error(f"Error: Failed to build graph-{e}.")
                return 
        except Exception as e:
            st.error(f"Error: Failed to build the graph-{e}")
            return
        

            
    
    
    
    