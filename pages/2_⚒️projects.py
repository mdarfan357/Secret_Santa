import streamlit as st
st.set_page_config(
    page_title = "Multipage App",
    page_icon = "🐐"
)
st.write("Hello World")

tab_titles = ["Create Apps","Run Visualization charts","Display Outputs","Deploy the apps on the cloud"]

tabs = st.tabs(tab_titles)

with tabs[0]:
    st.write("You are now in the create apps page")


with tabs[1]:
    st.write("You are now in the charts page")
    
with tabs[2]:
    st.write("You are now in the outputs page")

    
with tabs[3]:
    st.write("You are now in the deployment page")