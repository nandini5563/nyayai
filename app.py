import streamlit as st
from PIL import Image
import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

st.set_page_config(page_title="NyayAI", page_icon="⚖️", layout="wide")

st.title("⚖️ NyayAI – Digital Complaint & Evidence Assistant")
st.write("Your AI-powered assistant to help with complaint drafting, evidence checking, and legal clarity.")

option = st.sidebar.selectbox(
    "Choose a Service",
    ["Home", "Draft a Complaint", "Check Evidence", "Generate Legal Advice"]
)

def ai_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message['content']


# HOME PAGE
if option == "Home":
    st.header("Welcome to NyayAI")
    st.write("Select a service from the left menu to begin.")

# COMPLAINT DRAFT
if option == "Draft a Complaint":
    st.header("📝 Complaint Drafting")
    incident = st.text_area("Describe the incident in detail:")
    
    if st.button("Generate Complaint"):
        if incident.strip() == "":
            st.warning("Please type the incident details.")
        else:
            prompt = f"Write a formal police complaint/FIR in simple English based on this incident: {incident}"
            result = ai_response(prompt)
            st.subheader("Generated Complaint")
            st.write(result)

# EVIDENCE CHECKER
if option == "Check Evidence":
    st.header("🔍 Evidence Verification")
    uploaded = st.file_uploader("Upload Image or Document", type=["jpg", "png"])
    
    if uploaded is not None:
        img = Image.open(uploaded)
        st.image(img, caption="Uploaded Evidence", width=300)
        
        if st.button("Analyze Evidence"):
            prompt = "Analyze whether this image might be genuine or manipulated. Provide risk level and justification."
            result = ai_response(prompt)
            st.subheader("AI Evidence Report")
            st.write(result)

# LEGAL ADVICE
if option == "Generate Legal Advice":
    st.header("⚖️ AI Legal Advice")
    question = st.text_area("Ask your legal question:")
    
    if st.button("Get Advice"):
        prompt = f"Give simple legal advice for this issue: {question}"
        result = ai_response(prompt)
        st.subheader("Legal Advice")
        st.write(result)
