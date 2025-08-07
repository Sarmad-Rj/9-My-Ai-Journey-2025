import streamlit as st
import base64


st.set_page_config(
    page_title="C2C Converter",
    page_icon="💱",  # 🪙 💲
    # layout="wide",
    # layout="centered"
)




def set_bg_with_overlay(image_file):
    with open(image_file, "rb") as image:
        encoded = base64.b64encode(image.read()).decode()

    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: linear-gradient(rgba(255, 255, 255, .75), rgba(0, 0, 0, 0.55)), 
                              url("data:image/png;base64,{encoded}");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
            background-position: center;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

set_bg_with_overlay("bg.jpg")



# Main page content
st.title("💱 Welcome to C2C Converter")

st.markdown("""
- 🔸 **Coin to Currency** – Convert cryptocurrency price to local currency price.
- 🔸 **Currency to Currency** – Convert between fiat currencies.
- 🎮 **Game** – Number Guessing game.
""")






