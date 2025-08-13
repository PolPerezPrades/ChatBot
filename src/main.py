import streamlit as st
from backend import get_response, get_paths

COLS_PER_ROW = 3

st.set_page_config(page_title = "Eclipse Chatbot", page_icon=":material/join:")

st.title("Eclipse Chatbot")

# Keep chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
        if msg["role"] == "user" and "images" in msg:
            for i in range(0, len(msg["images"]), COLS_PER_ROW):
                cols = st.columns(COLS_PER_ROW)
                for col, img_url in zip(cols, msg["images"][i:i+COLS_PER_ROW]):
                    col.image(img_url, use_container_width=True)
# User input
if prompt := st.chat_input("Ask me something...", accept_file="multiple", file_type=["png", "jpg", "jpeg"]):
    # Store user message
    with st.chat_message("user"):
        if prompt.text:
            st.markdown(prompt.text)
        if prompt.files:
            for i in range(0, len(prompt.files), COLS_PER_ROW):
                cols = st.columns(COLS_PER_ROW)
                for col, file in zip(cols, prompt.files[i:i+COLS_PER_ROW]):
                    col.image(file, use_container_width=True)

    st.session_state.messages.append({"role": "user", "content": prompt.text, "images": get_paths(prompt.files)})

    # Generate model response
    with st.chat_message("assistant"):
        with st.empty():
            with st.spinner("Thinking..."):
                stream = get_response(messages=st.session_state.messages)
                first_chunk = next(stream, None)
            full_response = ""
            if first_chunk:
                full_response += first_chunk["message"]["content"]
                st.markdown(full_response)

            for chunk in stream:        
                full_response += chunk["message"]["content"]
                st.markdown(full_response)
    # Store assistant message
    st.session_state.messages.append({"role": "assistant", "content": full_response})