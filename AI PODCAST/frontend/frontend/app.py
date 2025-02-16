import streamlit as st
import requests

# Backend API URL (Update when deployed)
API_URL = "http://127.0.0.1:5000/generate"  

st.set_page_config(page_title="VatsGenixAI - AI Podcast Generator", layout="wide")

# 🎤 App Branding
st.title("🎙️ VatsGenixAI - AI-Powered Podcast Generator")
st.write("Generate high-quality podcasts using AI. Powered by OpenAI, 11 Labs, and Hygen.")

# 📝 User Input
prompt = st.text_area("Enter your podcast topic:", placeholder="Type here...")

if st.button("Generate Podcast"):
    if prompt:
        with st.spinner("Generating your podcast... 🎧"):
            response = requests.post(API_URL, json={"prompt": prompt})

            if response.status_code == 200:
                data = response.json()
                st.subheader("📜 Generated Podcast Script")
                st.write(data["generated_text"])

                st.subheader("🔍 Podcast Summary")
                st.write(data["summary"])

                st.subheader("🎧 Listen to Your AI-Generated Podcast")
                st.audio(data["audio_url"])
            else:
                st.error("Error generating podcast! Please try again.")
    else:
        st.warning("⚠️ Please enter a prompt!")

# Sidebar with branding
st.sidebar.header("ℹ️ About VatsGenixAI")
st.sidebar.write("VatsGenixAI helps you create AI-powered podcasts instantly using cutting-edge technology.")
st.sidebar.write("Made with ❤️ by Anurag.")

st.sidebar.markdown("### Connect with Us:")
st.sidebar.markdown("[GitHub](https://github.com/yourgithub) | [LinkedIn](https://linkedin.com/in/yourprofile)")

