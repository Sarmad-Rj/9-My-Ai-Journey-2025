import streamlit as st

st.set_page_config(
    page_title="C2C Converter",
    page_icon="madrix.png"
)

# CSS Styling for scrollable chat
st.markdown(
    """
    <style>
    .chat-container {
        max-width: 700px;
        margin: auto;
        height: 400px; /* Fixed height for scrolling */
        overflow-y: auto;
        display: flex;
        flex-direction: column;
    }
    .user-msg {
        background-color: #DCF8C6;
        padding: 10px;
        border-radius: 10px;
        margin-bottom: 5px;
        text-align: right;
    }
    .bot-msg {
        background-color: #F1F0F0;
        padding: 10px;
        border-radius: 10px;
        margin-bottom: 5px;
        text-align: left;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title
st.markdown(
    """
    <h1 style='text-align: center;'>🤖 Madrix </h1>
    <h5 style='text-align: center;'>Sarmad's Personal AI</h5>
    """,
    unsafe_allow_html=True
)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        ("user", "Hey Madrix, you there?"),
        ("bot", "Always here, Sarmad. How can I help?"),
        ("user", "Test message to check auto-scroll."),
        ("bot", "Looks like it’s working perfectly."),
    ]

# Display chat
st.markdown('<div class="chat-container" id="chat-box">', unsafe_allow_html=True)
for sender, msg in st.session_state.messages:
    if sender == "user":
        st.markdown(f'<div class="user-msg">{msg}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="bot-msg">{msg}</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# JavaScript to scroll to bottom
st.markdown(
    """
    <script>
    var chatBox = document.getElementById('chat-box');
    chatBox.scrollTop = chatBox.scrollHeight;
    </script>
    """,
    unsafe_allow_html=True
)

# Input box
user_input = st.chat_input("Type your message to Madrix...")

if user_input:
    st.session_state.messages.append(("user", user_input))
    bot_reply = f"Madrix here! You said: {user_input}"
    st.session_state.messages.append(("bot", bot_reply))
    st.experimental_rerun()
