import os

import streamlit as st
from google import genai
from prompts import PROMPT


def analyze_resume(resume_text):
    """
    Analyze a resume using Google's Gemini model.

    Args:
        resume_text (str): Extracted text from the uploaded resume.

    Returns:
        str: AI-generated resume analysis or an error message.
    """

    if not resume_text or not resume_text.strip():
        return "❌ No resume text found. Please upload a valid PDF."

    try:
        # Streamlit Cloud
        api_key = st.secrets.get("GEMINI_API_KEY")

        # Local fallback
        if not api_key:
            api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            return (
                "❌ Gemini API key not found.\n\n"
                "Add GEMINI_API_KEY to Streamlit Secrets or your environment variables."
            )

        client = genai.Client(api_key=api_key)

        prompt = PROMPT.format(resume=resume_text)

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )

        return response.text

    except Exception as e:
        return f"""❌ Unable to analyze the resume.

Error Details:
{e}
"""
