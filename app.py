import streamlit as st
from dotenv import load_dotenv
from io import BytesIO
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

from services.speech_to_text import transcribe_audio
from services.summarizer import generate_summary_and_points
from services.keywords import extract_keywords
from services.sentences import extract_important_sentences
from utils.file_handler import save_uploaded_file

load_dotenv()

st.set_page_config(page_title="AI Lecture Notes Generator", layout="wide")

# ---------- UI HEADER ----------
st.markdown("<h1 style='text-align:center;'>🎧 AI Lecture Voice-to-Notes Generator</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;color:gray;'>Upload lecture audio and get transcript, summary, key points, keywords and important sentences</p>", unsafe_allow_html=True)
st.markdown("---")

# ---------- FILE UPLOADER (label fixed) ----------
uploaded_file = st.file_uploader("Upload your lecture audio (MP3/WAV)", type=["mp3", "wav"])

# ---------- MAIN LOGIC ----------
if uploaded_file:

    if "file_path" not in st.session_state:
        st.session_state.file_path = save_uploaded_file(uploaded_file)

    # ----- TRANSCRIPTION -----
    if "transcript" not in st.session_state:
        with st.spinner("🎙️ Transcribing audio..."):
            st.session_state.transcript = transcribe_audio(st.session_state.file_path)

    transcript = st.session_state.transcript
    st.success("Transcription completed")

    # ----- SUMMARY + KEY POINTS -----
    if "summary_data" not in st.session_state:
        with st.spinner("📝 Generating summary and key points..."):
            summary, key_points = generate_summary_and_points(transcript)
            st.session_state.summary_data = (summary, key_points)

    summary, key_points = st.session_state.summary_data
    st.success("Summary and key points generated")

    # ----- KEYWORDS -----
    if "keywords" not in st.session_state:
        with st.spinner("🏷️ Extracting keywords..."):
            st.session_state.keywords = extract_keywords(transcript)

    keywords = st.session_state.keywords
    st.success("Keywords extracted")

    # ----- IMPORTANT SENTENCES -----
    if "important_sentences" not in st.session_state:
        with st.spinner("⭐ Extracting important sentences..."):
            st.session_state.important_sentences = extract_important_sentences(transcript)

    important_sentences = st.session_state.important_sentences
    st.success("Important sentences extracted")

    # ---------- DISPLAY OUTPUT ----------
    st.markdown("## 📄 Transcript")
    st.write(transcript)

    st.markdown("## 📝 Summary")
    st.write(summary)

    st.markdown("## 🔑 Key Points")
    for point in key_points:
        st.markdown(f"- {point}")

    st.markdown("## 🏷️ Keywords")
    st.write(", ".join(keywords))

    st.markdown("## ⭐ Important Sentences")
    for idx, sent in enumerate(important_sentences, 1):
        st.markdown(f"{idx}. {sent}")

    # ---------- PDF GENERATION (NO RE-RUN ISSUE) ----------
    def generate_pdf():
        buffer = BytesIO()
        styles = getSampleStyleSheet()
        doc = SimpleDocTemplate(buffer)
        story = []

        story.append(Paragraph("<b>AI Lecture Notes</b>", styles["Title"]))
        story.append(Spacer(1, 12))

        story.append(Paragraph("<b>Transcript</b>", styles["Heading2"]))
        story.append(Paragraph(transcript, styles["Normal"]))
        story.append(Spacer(1, 12))

        story.append(Paragraph("<b>Summary</b>", styles["Heading2"]))
        story.append(Paragraph(summary, styles["Normal"]))
        story.append(Spacer(1, 12))

        story.append(Paragraph("<b>Key Points</b>", styles["Heading2"]))
        for point in key_points:
            story.append(Paragraph(f"- {point}", styles["Normal"]))
        story.append(Spacer(1, 12))

        story.append(Paragraph("<b>Keywords</b>", styles["Heading2"]))
        story.append(Paragraph(", ".join(keywords), styles["Normal"]))
        story.append(Spacer(1, 12))

        story.append(Paragraph("<b>Important Sentences</b>", styles["Heading2"]))
        for sent in important_sentences:
            story.append(Paragraph(sent, styles["Normal"]))

        doc.build(story)
        buffer.seek(0)
        return buffer

    # ---------- DOWNLOAD BUTTON ----------
    st.markdown("---")
    pdf_bytes = generate_pdf()

    st.download_button(
        label="📥 Download Notes as PDF",
        data=pdf_bytes,
        file_name="AI_Lecture_Notes.pdf",
        mime="application/pdf"
    )
