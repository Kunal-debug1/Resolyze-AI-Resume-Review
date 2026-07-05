import streamlit as st

from analyzer import analyze_resume
from pdf_reader import extract_text


APP_NAME = "Resolyze"

st.set_page_config(
    page_title=f"{APP_NAME} | AI Resume Review",
    page_icon="R",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Manrope:wght@600;700;800&display=swap');

    :root {
        --ink: #102a2b;
        --muted: #637475;
        --line: #dce5e3;
        --paper: #f7faf9;
        --white: #ffffff;
        --accent: #0f8f7c;
        --accent-dark: #087465;
        --accent-soft: #e3f4f0;
    }

    html, body, [class*="css"] {
        font-family: "DM Sans", sans-serif;
    }

    .stApp {
        background:
            radial-gradient(circle at 92% 5%, rgba(15, 143, 124, .09), transparent 25rem),
            var(--paper);
        color: var(--ink);
    }

    [data-testid="stHeader"] {
        background: transparent;
    }

    [data-testid="stToolbar"], #MainMenu, footer {
        visibility: hidden;
    }

    .block-container {
        max-width: 1120px;
        padding: 1.4rem 2rem 3rem;
    }

    .site-nav {
        display: flex;
        align-items: center;
        justify-content: space-between;
        min-height: 54px;
        border-bottom: 1px solid var(--line);
        animation: reveal .55s ease both;
    }

    .brand {
        display: flex;
        align-items: center;
        gap: .7rem;
        font-family: "Manrope", sans-serif;
        font-size: 1.08rem;
        font-weight: 800;
        letter-spacing: -.03em;
    }

    .brand-mark {
        display: grid;
        width: 31px;
        height: 31px;
        place-items: center;
        border-radius: 9px;
        color: white;
        background: var(--ink);
        font-size: .9rem;
    }

    .nav-note {
        color: var(--muted);
        font-size: .8rem;
        font-weight: 600;
        letter-spacing: .05em;
        text-transform: uppercase;
    }

    .hero {
        max-width: 850px;
        padding: 5.7rem 0 3.2rem;
        animation: reveal .7s .08s ease both;
    }

    .kicker {
        display: flex;
        align-items: center;
        gap: .55rem;
        margin-bottom: 1.15rem;
        color: var(--accent-dark);
        font-size: .76rem;
        font-weight: 700;
        letter-spacing: .1em;
        text-transform: uppercase;
    }

    .kicker::before {
        content: "";
        width: 28px;
        height: 2px;
        background: var(--accent);
    }

    .hero h1 {
        max-width: 780px;
        margin: 0;
        color: var(--ink);
        font-family: "Manrope", sans-serif;
        font-size: clamp(3rem, 6.2vw, 5.5rem);
        font-weight: 800;
        letter-spacing: -.065em;
        line-height: .98;
    }

    .hero h1 span {
        color: var(--accent);
    }

    .hero p {
        max-width: 590px;
        margin: 1.5rem 0 0;
        color: var(--muted);
        font-size: 1.12rem;
        line-height: 1.65;
    }

    .workspace-label {
        display: flex;
        align-items: end;
        justify-content: space-between;
        gap: 2rem;
        margin: .6rem 0 1rem;
        animation: reveal .65s .15s ease both;
    }

    .workspace-label h2 {
        margin: 0;
        color: var(--ink);
        font-family: "Manrope", sans-serif;
        font-size: 1.25rem;
        letter-spacing: -.035em;
    }

    .workspace-label p {
        margin: .3rem 0 0;
        color: var(--muted);
        font-size: .9rem;
    }

    .format-note {
        flex: none;
        color: var(--muted);
        font-size: .78rem;
    }

    [data-testid="stFileUploader"] {
        max-width: 100%;
        animation: reveal .65s .2s ease both;
    }

    [data-testid="stFileUploaderDropzone"] {
        min-height: 82px;
        padding: .85rem 1.15rem !important;
        border: 1.5px dashed #a9bfba !important;
        border-radius: 13px !important;
        background: rgba(255,255,255,.76) !important;
        transition: border-color .2s ease, background .2s ease, transform .2s ease;
    }

    [data-testid="stFileUploaderDropzone"] > div {
        min-height: 50px;
        align-items: center;
    }

    [data-testid="stFileUploaderDropzoneInstructions"] {
        padding: 0 !important;
    }

    [data-testid="stFileUploaderDropzoneInstructions"] > div > span {
        font-size: .9rem;
    }

    [data-testid="stFileUploaderDropzoneInstructions"] small {
        font-size: .76rem;
    }

    [data-testid="stFileUploaderDropzone"]:hover {
        border-color: var(--accent) !important;
        background: var(--white) !important;
        transform: translateY(-2px);
    }

    [data-testid="stFileUploaderDropzone"] button {
        border: 1px solid var(--ink) !important;
        border-radius: 9px !important;
        background: var(--ink) !important;
        color: white !important;
        font-weight: 600 !important;
    }

    .process {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        margin: 2rem 0 4rem;
        border-top: 1px solid var(--line);
        animation: reveal .65s .28s ease both;
    }

    .process-item {
        padding: 1.25rem 2rem 0 0;
    }

    .process-item span {
        color: var(--accent);
        font-size: .72rem;
        font-weight: 700;
    }

    .process-item strong {
        display: block;
        margin-top: .25rem;
        color: var(--ink);
        font-family: "Manrope", sans-serif;
        font-size: .93rem;
    }

    .process-item p {
        margin: .3rem 0 0;
        color: var(--muted);
        font-size: .82rem;
        line-height: 1.5;
    }

    .section-title {
        margin: 2.4rem 0 1rem;
        color: var(--ink);
        font-family: "Manrope", sans-serif;
        font-size: 1.25rem;
        letter-spacing: -.03em;
    }

    div[data-testid="stAlert"] {
        border: 1px solid var(--line);
        border-radius: 12px;
        background: white;
    }

    details {
        border: 1px solid var(--line) !important;
        border-radius: 12px !important;
        background: white !important;
    }

    .stButton > button, .stDownloadButton > button {
        min-height: 49px;
        border: 0;
        border-radius: 10px;
        background: var(--accent);
        color: white;
        font-weight: 700;
        box-shadow: 0 8px 24px rgba(15,143,124,.16);
        transition: background .2s ease, transform .2s ease, box-shadow .2s ease;
    }

    .stButton > button:hover, .stDownloadButton > button:hover {
        background: var(--accent-dark);
        color: white;
        transform: translateY(-2px);
        box-shadow: 0 12px 28px rgba(15,143,124,.22);
    }

    .report-shell {
        margin-top: 1rem;
        padding: 1.5rem 1.8rem .6rem;
        border-top: 3px solid var(--accent);
        background: white;
        box-shadow: 0 16px 50px rgba(16,42,43,.07);
    }

    .footer {
        display: flex;
        justify-content: space-between;
        gap: 1rem;
        margin-top: 4rem;
        padding-top: 1.25rem;
        border-top: 1px solid var(--line);
        color: #849291;
        font-size: .78rem;
    }

    @keyframes reveal {
        from { opacity: 0; transform: translateY(12px); }
        to { opacity: 1; transform: translateY(0); }
    }

    @media (prefers-reduced-motion: reduce) {
        *, *::before, *::after { animation: none !important; transition: none !important; }
    }

    @media (max-width: 700px) {
        .block-container { padding: 1rem 1.1rem 2rem; }
        .nav-note, .format-note { display: none; }
        .hero { padding: 3.7rem 0 2.5rem; }
        .hero h1 { font-size: 3.15rem; }
        .hero p { font-size: 1rem; }
        .process { grid-template-columns: 1fr; }
        .process-item { padding-right: 0; }
        .footer { flex-direction: column; }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    f"""
    <nav class="site-nav">
        <div class="brand"><span class="brand-mark">R</span>{APP_NAME}</div>
        <div class="nav-note">AI resume intelligence</div>
    </nav>
    <section class="hero">
        <div class="kicker">Resume analysis, made useful</div>
        <h1>Make your resume <span>work harder.</span></h1>
        <p>Upload your PDF for a focused review of ATS compatibility, skills,
        experience, and the changes that can strengthen your next application.</p>
    </section>
    <div class="workspace-label">
        <div>
            <h2>Start your review</h2>
            <p>Your analysis begins as soon as you choose a resume.</p>
        </div>
        <span class="format-note">PDF · MAX 200 MB</span>
    </div>
    """,
    unsafe_allow_html=True,
)

uploaded_file = st.file_uploader(
    "Upload your resume",
    type=["pdf"],
    label_visibility="collapsed",
    help="Upload one PDF resume, up to 200 MB.",
)

st.markdown(
    """
    <div class="process">
        <div class="process-item">
            <span>01</span><strong>Upload</strong>
            <p>Add your current resume as a PDF.</p>
        </div>
        <div class="process-item">
            <span>02</span><strong>Analyze</strong>
            <p>Review ATS fit, keywords, strengths, and gaps.</p>
        </div>
        <div class="process-item">
            <span>03</span><strong>Improve</strong>
            <p>Leave with clear, prioritized recommendations.</p>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

if uploaded_file is not None:
    with st.spinner("Extracting your resume…"):
        resume = extract_text(uploaded_file)

    if resume and resume.strip():
        st.success(f"{uploaded_file.name} is ready for review.")
        st.markdown('<h2 class="section-title">Extracted content</h2>', unsafe_allow_html=True)

        with st.expander("Preview resume text"):
            st.text(resume[:4000])

        if st.button("Analyze resume", use_container_width=True, type="primary"):
            with st.spinner("Reviewing your resume…"):
                result = analyze_resume(resume)

            st.markdown('<h2 class="section-title">Your resume review</h2>', unsafe_allow_html=True)
            st.markdown('<div class="report-shell">', unsafe_allow_html=True)
            st.markdown(result)
            st.markdown("</div>", unsafe_allow_html=True)

            st.download_button(
                "Download report",
                data=result,
                file_name=f"{APP_NAME}_resume_review.md",
                mime="text/markdown",
                use_container_width=True,
            )
    else:
        st.error("We could not read text from this PDF. Try exporting it as a text-based PDF and upload it again.")

st.markdown(
    f"""
    <div class="footer">
        <span>© 2026 {APP_NAME}</span>
        <span>Your file is processed only for this analysis.</span>
    </div>
    """,
    unsafe_allow_html=True,
)
