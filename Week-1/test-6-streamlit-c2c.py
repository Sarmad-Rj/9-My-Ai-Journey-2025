import streamlit as st
from bs4 import BeautifulSoup
import requests

response = requests.get('https://coinmarketcap.com/')

content = response.text

soup = BeautifulSoup(content, 'html.parser')

coin_logos = soup.find_all(class_="coin-logo")

logo_urls = []

for logo in coin_logos:
    img_tag = logo.find("img")
    if img_tag and img_tag.get("src"):
        logo_urls.append(img_tag["src"])

st.title("Coin Logos")

for url in logo_urls:
    st.image(url, width=50)  
    print(11)
