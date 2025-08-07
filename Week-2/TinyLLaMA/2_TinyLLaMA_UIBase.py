import streamlit as st
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# Load TinyLLaMA
model_id = "TinyLLaMA/TinyLLaMA-1.1B-Chat-v1.0"
tokenizer = AutoTokenizer.from_pretrained(model_id) 
model = AutoModelForCausalLM.from_pretrained(model_id)

# Chat generation function
def generate_response(prompt):
    formatted = f"<|system|>You are a helpful assistant.<|end|>\n<|user|>{prompt}<|end|>\n<|assistant|>"
    inputs = tokenizer(formatted, return_tensors="pt")
    with torch.no_grad():
        outputs = model.generate(**inputs, max_new_tokens=200)
    return tokenizer.decode(outputs[0], skip_special_tokens=True).split("<|assistant|>")[-1]

# Streamlit UI
st.set_page_config(page_title="TinyLLaMA Chatbot")
st.title("🧠 TinyLLaMA Chatbot")

user_input = st.text_input("You:", "")

if st.button("Send"):
    if user_input:
        response = generate_response(user_input)
        st.markdown(f"**Assistant:** {response}")
