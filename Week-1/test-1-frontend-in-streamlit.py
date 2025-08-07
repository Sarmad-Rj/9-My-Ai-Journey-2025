import streamlit as st
# st.title('First Web Page')
# # st.write('Testing!')

# num1 = st.number_input("Enter no 1")
# num2 = st.number_input("Enter no 2")

# sum = num1 = num2
# if st.button('sum'):
#     st.write(sum)
#     st.snow()

# slider = st.slider('Select range', min_value = 100, max_value = 1000, value = (300, 400), step = 10)

# if st.button('Show selected range'):
#     st.write(slider[0], slider [1])

#-----------------------------------------IMAGE-------------------------------------------
from PIL import Image 

st.title('Browse and Display Picture')

picture = st.file_uploader("Choose an image...", type = ["jpeg", "jpg", "png"])

if picture is not None:
    img = Image.open(picture)
    st.image(img, caption =  "Uploaded Image")