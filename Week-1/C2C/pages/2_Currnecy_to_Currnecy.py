import streamlit as st
from utils.shared_data import currency_codes
import requests
from bs4 import BeautifulSoup

st.set_page_config(
    page_title="C2C Converter",
    page_icon="💱", 
)

# --------------------------------------------0
# def set_shade_only():
#     st.markdown(
#         """
#         <style>
#         .stApp {
#             background-image: linear-gradient(
#                 rgba(255, 127, 127, 1),
#                 rgba(255, 255, 255, 0.75)
                
#             );
#             background-size: cover;
#             background-repeat: no-repeat;
#             background-attachment: fixed;
#             background-position: center;
#         }
#         </style>
#         """,
#         unsafe_allow_html=True
#     )

# set_shade_only()

# --------------------------------------------1
col1, col2 = st.columns([1, 9]) 

with col2:
    st.markdown("## 💱 Currency to Currency Converter")

# --------------------------------------------2
col1, col2 = st.columns([8, 2])
with col1:
    selected_Currency_1 =  st.selectbox("Select 1st Currency", currency_codes, index = 145)

with col2:
    quantity = st.number_input( "Quantity", value=1, min_value=1 )
    
selected_Currency_2 =  st.selectbox("Select 2nd Currency", currency_codes, index = 111)

# --------------------------------------------3
import socket

def is_connected():
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=1)
        return True
    except OSError:
        return False
# --------------------------------------------4
if selected_Currency_1 == selected_Currency_2:
    st.warning("⚠️ Please select two different currencies.")
elif not is_connected():
    st.error("❌ No internet connection. Please check your network.")
else:
    #  Get price conversion page
    con = requests.get(f"https://www.google.com/finance/quote/{selected_Currency_1}-{selected_Currency_2}")
    content_pg = con.text

    # Parse HTML
    soup = BeautifulSoup(content_pg, 'html.parser')

    # Extract currency price
    currency_price_tags = soup.find_all(class_='YMlKec fxKbKc')
    currency_price = float(currency_price_tags[0].get_text())

    # Convert price
    def convert(quantity):
        new_price = currency_price * quantity
        st.markdown(f"## {quantity} {selected_Currency_1} in {selected_Currency_2}: :blue[{new_price:.2f}]")

    if st.button("Convert", type="primary"):
        convert(quantity)
