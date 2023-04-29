import os
from apikey import apikey

import streamlit as st 
from langchain.memory import ConversationBufferMemory
from langchain.llms import OpenAI
from langchain.prompts import   PromptTemplate
from langchain.chains import LLMChain

apikey = os.environ['OPENAI_API_KEY']

st.title('🤣😂😹..Funny Story Generator')

prompt = st.text_input('...generate a short story about almost anything')

title_template = PromptTemplate(
    input_variables = ['topic'],
    template='write me a funny short story about {topic}'
)#memory


title_memory = ConversationBufferMemory(input_key='topic', memory_key='chat_history')

## LLMS

llm = OpenAI(temperature=0.9)
title_chain = LLMChain(llm=llm, prompt=title_template, verbose=True,output_key='title', memory=title_memory)

## show on screen
if prompt:
    response = title_chain.run(prompt)
    st.write(response)