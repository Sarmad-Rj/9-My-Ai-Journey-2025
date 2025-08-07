import streamlit as st

#------------------------------------------------------Text
st.title('SARMAD')
st.write("# SARMAD")
st.header('SARMAD')
st.write("## SARMAD")
st.subheader("SARMAD")
st.write("### SARMAD")
st.write('Hello, *World!* :sunglasses:')
' testing, *testing,* _testing_, :blue[testing]'

st.markdown('''
    :red[Streamlit] :orange[can] :green[write] :blue[text] :violet[in]
    :gray[pretty] :rainbow[colors] and :blue-background[highlight] text. :balloon:''')

#------------------------------------------------------Data Frame
import pandas as pd

st.write(1234)
st.write(
    pd.DataFrame(
        {
            "first column": [1, 2, 3, 4],
            "second column": [10, 20, 30, 40],
        }
    )
)

#------------------------------------------------------Button
st.link_button("Go to gallery", "https://streamlit.io/gallery")
st.button("Button", type="primary")

#------------------------------------------------------checkbox
agree = st.checkbox("I agree")

if agree:
    st.write("Great!")

#------------------------------------------------------Color Picker
color = st.color_picker("Pick A Color", "#00f900")
st.write("The current color is", color)

#------------------------------------------------------Select Box
option = st.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone"),
)

st.write("You selected:", option)
#------------------------------------------------------Col
col1, col2 = st.columns([1.5, 9]) 
with col1:
    # st.image("icon.png", width=70)
    pass

with col2:
    st.markdown("<h1 style='padding-top: 10px;'> Coin to Currency Converter</h1>", unsafe_allow_html=True)