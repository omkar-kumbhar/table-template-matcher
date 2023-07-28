# A bare bones UI for the Open AI Chat Completion used in ChatGPT
# Created by Adam Tomkins, Referenced by Omkar Kumbhar

import os
import openai
import streamlit as st
import pandas as pd
from typing import List,Optional , Union
from langmain import TemplateMatcherPrompts


openai.api_key = st.secrets["openai"]["openai_api_key"]


# Set up Session State
if "messages" not in st.session_state:
    st.session_state["messages"] = []
if "primer" not in st.session_state:
    st.session_state["primer"] = "You are a friendly and helpful assistant."
if "context_length" not in st.session_state:
    st.session_state["context_length"] = 10


def main():

    st.sidebar.header("Settings")

    with st.sidebar:
        # Allow the user to set their prompt
        # Allow Users to reset the memory
        if st.button("Restart"):
            st.session_state.messages = []
            st.info("Chat Memory Cleared")
            st.session_state.test_template = {}
            st.session_state.test_table = {}
            st.info('Uploaded files cleared')
            history = st.container()

        st.info("You can clear the chat memory by clicking the button above.")
        st.info("Reupload the files to start a new conversation.")

    col1, col2 = st.columns(2)
    test_table,test_template = {},{}
    history = st.container()

    # load prompts
    system_prompt = TemplateMatcherPrompts.system_prompt
    template_prompt = TemplateMatcherPrompts.template_prompt


    with col1:
        ## Upload two csv files to streamlit
        st.header('Upload template file')
        uploaded_file1 = st.file_uploader('Upload a template')
        if uploaded_file1 is not None:
            df1 = pd.read_csv(uploaded_file1)
            # st.write(df1.head())
            test_template = df1.to_dict()

    with col2:
        st.header('Upload table file')
        uploaded_file2 = st.file_uploader('Upload a table to match template')
        if uploaded_file2 is not None:
            df2 = pd.read_csv(uploaded_file2)
            # st.write(df2.head())
            test_table = df2.to_dict()

    if test_template != {} and test_table != {}:
        # after uploading the files, set up prompts. 
        
        # first set up system prompt. 
        input = template_prompt.format(test_template_element=test_template,
                                           test_table_element=test_table)

        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": input}]
        
        r = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
        
        
        st.session_state.messages.append(
            {"role": "assistant", "content": r["choices"][0]["message"]["content"]}
        )

    else:
        st.info("Please upload both the files to start template matching service")
    
    with history:
        for i, message in enumerate(st.session_state.messages):
            c1, c2 = st.columns([2, 10])
            with c1:
                st.write(message["role"])
            with c2:
                # Lets initialize the messages that are sent in the state
                if (
                    len(st.session_state.messages) - i
                    < st.session_state.context_length + 1
                ):
                    st.markdown(f'{message["content"]}')
                else:
                    st.markdown(f'{message["content"]}')


st.title("Table <> template matching")
main()

st.info("Demo: Omkar Kumbhar, CSV Understanding Application.")
