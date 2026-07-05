# 🚀 Resolyze – AI Resume Analyzer

**Resolyze** is an AI-powered Resume Analyzer built with **Python**, **Streamlit**, and **Ollama**. It helps job seekers evaluate their resumes using a local Large Language Model (LLM), providing ATS-friendly feedback, skill analysis, improvement suggestions, and career recommendations.

---

## 📌 Features

* 📄 Upload resumes in PDF format
* 🤖 AI-powered resume analysis using Ollama
* 📊 ATS Compatibility Score
* 📝 Professional Resume Summary
* 💪 Strengths & Weaknesses Analysis
* 🔍 Keyword Analysis
* 🧠 Missing Skills Detection
* 💼 Project & Experience Evaluation
* 📈 Resume Improvement Suggestions
* 🎯 Recommended Job Roles
* 📥 Download the analysis report

---

## 🛠️ Tech Stack

* **Frontend:** Streamlit
* **Backend:** Python
* **AI Model:** Ollama (DeepSeek R1 / Qwen)
* **PDF Processing:** PyPDF2

---

## 📂 Project Structure

```text
Resolyze/
│
├── app.py                 # Streamlit application
├── analyzer.py            # AI resume analyzer
├── pdf_reader.py          # Extracts text from PDF resumes
├── prompts.py             # AI prompt template
├── requirements.txt       # Python dependencies
├── README.md
└── assets/
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/resolyze-ai-resume-analyzer.git
cd resolyze-ai-resume-analyzer
```

### 2. Create a Virtual Environment

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**Linux / macOS**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🤖 Install Ollama

Download and install Ollama from:

https://ollama.com/download

Pull the AI model:

```bash
ollama pull deepseek-r1:1.5b
```

Or use:

```bash
ollama pull qwen2.5:3b
```

Start the Ollama server:

```bash
ollama serve
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

The application will open automatically in your browser.

---

## 📊 Sample Analysis

Resolyze provides:

* ATS Score
* Resume Summary
* Technical Skill Assessment
* Strengths
* Weaknesses
* Missing Keywords
* Project Evaluation
* Experience Review
* Grammar Suggestions
* Resume Formatting Review
* Recommended Skills
* Suitable Job Roles
* Professional Summary
* Actionable Improvement Tips

---

## 📦 Requirements

```text
streamlit
ollama
PyPDF2
```

---

## 🎯 Future Enhancements

* Resume vs Job Description Matching
* AI Cover Letter Generator
* LinkedIn Profile Analyzer
* Resume Rewrite with AI
* PDF Report Generation
* Skill Gap Visualization
* Multi-language Resume Support
* Recruiter Dashboard
* Dark Mode
* Authentication & User Profiles

---

## 👨‍💻 Author

**Kunal Gaikwad**

Python Developer | Django Developer | AI Enthusiast

GitHub: https://github.com/Kunal-debug1

LinkedIn: https://www.linkedin.com/

---

## ⭐ Support

If you found this project helpful:

* ⭐ Star this repository
* 🍴 Fork it
* 🛠️ Contribute with improvements
* 📢 Share it with others

---

## 📄 License

This project is licensed under the **MIT License**.

---

> **Resolyze** empowers job seekers with AI-driven insights to create stronger, ATS-friendly resumes and improve their chances of landing interviews.
