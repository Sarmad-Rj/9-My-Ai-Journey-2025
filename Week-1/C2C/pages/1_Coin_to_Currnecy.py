# ------------------------------------Imports---------------------------------------
import streamlit as st
from utils.shared_data import currency_codes
import requests
from bs4 import BeautifulSoup
from PIL import Image
import socket

# -----------------------------------INTERNET---------------------------------------

def is_connected():
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=3)
        return True
    except OSError:
        return False


# -----------------------------------Front End---------------------------------------
st.set_page_config(
    page_title="Crypto Converter",
    page_icon="🪙",  
    # layout="wide"
)

col1, col2 = st.columns([1.5, 9]) 

with col1:
    # st.image("icon.png", width=70)
    pass

with col2:
    st.markdown("<h1 style='padding-top: 10px;'> Coin to Currency Converter</h1>", unsafe_allow_html=True)

# --------------------------------------Back End---------------------------------------
if is_connected():

    # Remove USD from currency list
    # currency_codes = [x for x in currency_codes if x != "USD"]

    # 1. Get CoinMarketCap page
    cmc = requests.get('https://coinmarketcap.com/')
    content = cmc.text

    # Parse HTML
    soup1 = BeautifulSoup(content, 'html.parser')

    # Extract coins symbols, names, price
    coin_names_tags = soup1.find_all('p', class_='sc-65e7f566-0 iPbTJf coin-item-name')
    coin_symbols_tags = soup1.find_all(class_='sc-65e7f566-0 byYAWx coin-item-symbol')
    coin_price_tags = soup1.find_all(class_='sc-142c02c-0 lmjbLF')

    coin_names = [name.get_text().upper() for name in coin_names_tags]
    coin_symbols = [tag.get_text() for tag in coin_symbols_tags]
    coin_price = [tag.get_text() for tag in coin_price_tags]

    # Dropdown UI
    selected_coin = st.selectbox("Choose a Cryptocurrency", coin_names)
    selected_currency = st.selectbox("Select Currency", currency_codes, index=145)
    quantity = st.number_input("Quantity", value=1, min_value=1)

    # 2. Get USD to selected currency rate
    if selected_currency != "USD":
        usd_to_all = requests.get(f"https://www.google.com/finance/quote/USD-{selected_currency}")
        content_pg = usd_to_all.text
    
        soup2 = BeautifulSoup(content_pg, 'html.parser')
        currency_price_tags = soup2.find_all(class_='YMlKec fxKbKc')
        currency_price = float(currency_price_tags[0].get_text().replace("$", "").replace(",", "").strip())

    # Price of selected coin in dollar
    index = coin_names.index(selected_coin)
    price_in_dollar = float(coin_price[index].replace('$', '').replace(',', ''))
    
    # Define convert function
    def convert(selected_coin, selected_currency):
        price_in_selected_coin = price_in_dollar * currency_price
        return price_in_selected_coin

    # Show results
    button_pressed = False
    if st.button("Convert", type="primary"):
        button_pressed = True
        if selected_currency == "USD":
            if quantity == 1:
                st.markdown(f"### Price of {selected_coin.upper()} in USD: :blue[{price_in_dollar:.2f}$]")
            elif quantity > 1:
                quantity_price = price_in_dollar * quantity
                st.markdown(f"### Price of {selected_coin.upper()} in USD: :blue[{quantity_price:.2f}]$")
        else: 
            converted_price = convert(selected_coin, selected_currency)
            if quantity == 1:
                st.markdown(f"### Price of {selected_coin.upper()} in {selected_currency.upper()}: :blue[{converted_price:.2f}]")
                st.markdown(f"    Price of {selected_coin.upper()} in USD: :blue[{price_in_dollar:.2f}$]")
            elif quantity > 1:
                quantity_price = converted_price * quantity
                st.markdown(f"### Price of {selected_coin.upper()} in {selected_currency.upper()}: :blue[{quantity_price:.2f}]")
                st.markdown(f"    Price of 1 {selected_coin.upper()} in {selected_currency.upper()}: :blue[{converted_price:.2f}]")

    if not button_pressed:
        st.markdown(f"### Price of {selected_coin.upper()} in USD: :blue[{price_in_dollar:.2f}$]")


else:
    st.error("❌  Internet connection is required to fetch crypto and currency prices. Please check your network and refresh the page.")