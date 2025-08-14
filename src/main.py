import streamlit as st

main_page = st.Page("app_pages/main_page.py", title="New Chat", icon=":material/add_2:")
second_page = st.Page("app_pages/second_page.py", title="Title 2", icon=":material/edit:")

pg = st.navigation([main_page, second_page])
st.set_page_config(page_title="Eclise Chatbot", page_icon=":material/edit:")
pg.run()
