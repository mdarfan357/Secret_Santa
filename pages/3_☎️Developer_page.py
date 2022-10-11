import streamlit as st
import random 

st.set_page_config(
    page_title = "Multipage App",
    page_icon = "🐐"
)

password = st.text_input("Enter Key",type = "password")

if password == st.secrets.DEV_KEY:
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





    if "Hello_World" not in st.session_state:
            st.session_state["Hello_World"] = "Hello World!!"



    bt = st.button("Update session_state")

    if bt:
        st.session_state.Hello_World = "Not Hello World"

    bt1 = st.button("Add session_state")

    if bt1:
        st.session_state.x = random.randint(1,100)



    st.write(st.session_state)
