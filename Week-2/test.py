import streamlit as st
import os

uploaded_file = st.file_uploader("Upload audio/video", type=["mp3", "wav", "mp4", "mkv", "mov"])

if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False, suffix=f".{uploaded_file.name.split('.')[-1]}") as tmp:
        tmp.write(uploaded_file.read())
        temp_path = tmp.name

    st.write(f"Temp input path: {temp_path}")
    if not os.path.exists(temp_path):
        st.error("Temporary file not found!")
    else:
        ext = uploaded_file.name.split(".")[-1].lower()
        audio_path = temp_path
        if ext in ["mp4", "mkv", "mov"]:
            audio_path = temp_path + ".wav"
            try:
                (
                    ffmpeg
                    .input(temp_path)
                    .output(audio_path, format="wav", ac=1, ar="16000")
                    .run(quiet=False, overwrite_output=True)  # Show ffmpeg output for debugging
                )
                st.success(f"Converted audio saved at {audio_path}")
            except ffmpeg.Error as e:
                st.error(f"FFmpeg error:\n{e.stderr.decode()}")
