import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv

st.set_page_config(page_title="Jarvis", page_icon="🤖")
st.title("🤖 Jarvis")
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key)

with st.sidebar:
    st.write("💬 GPT-3.5 Turbo")
    if st.button("🗑️ مسح"):
        st.session_state.msgs = []
        st.rerun()

if "msgs" not in st.session_state:
    st.session_state.msgs = [{"role": "assistant", "content": "أهلاً بك! 👋"}]

for msg in st.session_state.msgs:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    st.session_state.msgs.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    
    res = client.chat.completions.create(model="gpt-3.5-turbo", messages=st.session_state.msgs)
    reply = res.choices[0].message.content
    
    st.chat_message("assistant").write(reply)
    st.session_state.msgs.append({"role": "assistant", "content": reply})
