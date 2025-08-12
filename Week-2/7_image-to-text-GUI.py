import streamlit as st
from PIL import Image
from transformers import pipeline
import io

load_vqa_pipeline = pipeline("visual-question-answering")

st.title("Image Question Answering App")
st.write("Upload an image, ask a question, and get an AI-generated answer.")

col1, col2 = st.columns([1, 1])

with col1:
    st.header("Upload Your Image")

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png", "gif"])

    if uploaded_file is not None:
        # st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)

        image = Image.open(uploaded_file)
        st.session_state['uploaded_image'] = image
    else:
        st.session_state['uploaded_image'] = None 


with col2:
    st.header("Ask Your Question")

    question = st.text_input(
        "Enter your question about the image:",
        placeholder="e.g., What is the main object?",
        key="vqa_question"
    )

    if st.session_state.get('uploaded_image') is not None and question:
        vqa_pipeline = load_vqa_pipeline

        st.write("Generating answer...")
        with st.spinner("AI is thinking..."):
            # Perform VQA
            result = vqa_pipeline(image=st.session_state['uploaded_image'], question=question, top_k=1)
            output = result[0]["answer"]
            st.subheader("AI's Answer:")
            st.write(f"**{output}**")
    elif st.session_state.get('uploaded_image') is None:
        st.write("Upload an image in the left column to ask a question.")
    elif not question:
        st.write("Enter a question about the image above.")
