import streamlit as st
from llm.rag_pipeline import get_answer

st.set_page_config(page_title="Ask ChatBot")
st.title("Ask ChatBot!")

if "messages" not in st.session_state:
    st.session_state.messages=[]


for message in st.session_state.messages:
    st.chat_message(message["role"]).markdown(message["content"])


prompt=st.chat_input("Pass your prompt here...")

if prompt:
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    try:
        # response = get_answer(prompt)
        response="Hello from assistant"
        st.chat_message("assistant").markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})
    except Exception as e:
        st.error(f"Error: {str(e)}")
