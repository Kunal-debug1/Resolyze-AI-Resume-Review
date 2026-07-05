import ollama
from prompts import PROMPT


def analyze_resume(resume_text):
    """
    Analyze a resume using the Ollama DeepSeek model.

    Args:
        resume_text (str): Extracted text from the uploaded resume.

    Returns:
        str: AI-generated resume analysis or an error message.
    """

    if not resume_text or not resume_text.strip():
        return "❌ No resume text found. Please upload a valid PDF."

    prompt = PROMPT.format(resume=resume_text)

    try:
        response = ollama.chat(
            model="deepseek-r1:1.5b",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are an expert ATS Resume Analyzer and Career Coach. "
                        "Provide clear, professional, and well-formatted responses in Markdown."
                    ),
                },
                {
                    "role": "user",
                    "content": prompt,
                },
            ],
        )

        return response["message"]["content"]

    except Exception as e:
        return f"""
❌ Unable to analyze the resume.

Possible reasons:
- Ollama is not running.
- The model 'deepseek-r1:1.5b' is not installed.
- The Ollama server connection failed.

Error Details:
{e}
"""