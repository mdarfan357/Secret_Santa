import streamlit as st
import random 



st.set_page_config(
    page_title = "Multipage App",
    page_icon = "🐐"
)
st.write("Hello World")



if "Hello_World" not in st.session_state:
        st.session_state["Hello_World"] = "Hello World!!"



bt = st.button("Update session_state")

if bt:
    st.session_state.Hello_World = "Not Hello World"

bt1 = st.button("Add session_state")

if bt1:
    st.session_state.x = random.randint(1,100)
    


st.write(st.session_state)
