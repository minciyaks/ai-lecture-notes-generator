# 🎧 AI Lecture Voice-to-Notes Generator

An intelligent Python + Streamlit application that converts lecture audio into structured study notes including transcript, summary, key points, keywords, important sentences, and a downloadable PDF.

This project is designed to help students quickly convert recorded lectures into clean, readable notes using AI.

📌 **This project was developed as part of a 1-month AI/ML Internship program under Edunet Foundation.**

---

## 🚀 Features

- 🎙️ **Speech-to-Text Transcription** using OpenAI Whisper  
- 📝 **Automatic Summary Generation**  
- 🔑 **Key Points Extraction**  
- 🏷️ **Keyword Detection**  
- ⭐ **Important Sentence Highlighting**  
- 📄 **PDF Export of Notes**  
- 🖥️ Clean and simple **Streamlit UI**

---

## 🛠️ Tech Stack

- **Python 3.11**
- **Streamlit** – Web interface
- **OpenAI Whisper** – Speech recognition
- **NLTK** – Sentence processing
- **Transformers** – Text summarization
- **ReportLab** – PDF generation

---

## 📁 Project Structure

```bash
ai-lecture-notes-generator/
│
├── app.py
│
├── services/
│   ├── __init__.py
│   ├── speech_to_text.py
│   ├── summarizer.py
│   ├── keywords.py
│   ├── sentences.py
│   └── important_sentences.py
│
├── utils/
│   ├── __init__.py
│   ├── file_handler.py
│   └── pdf_generator.py
│
├── audio/
│   └── sample audio files
│
├── lecture_notes.pdf
└── README.md
```

---

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/minciyaks/ai-lecture-notes-generator.git
```

### 2. Navigate into the project folder

```bash
cd ai-lecture-notes-generator
```
### 3. Create and activate virtual environment

```bash
python -m venv venv
venv\Scripts\activate
```
### 4. Install dependencies

```bash
pip install -r requirements.txt
```
### 5. Run the application

```bash
streamlit run app.py
```
---

## 📄 Sample Output

A sample generated PDF (lecture_notes.pdf) is included in this repository for demonstration and verification of output quality.

---
## 📌 Use Cases

- Students converting recorded lectures into notes

- Self-study and exam revision

- Online course learners

- Internship / academic project demonstration


---

## 👩‍💻 Author

Minciya K S |
BCA Student 

---



