📚 AI Lecture Voice-to-Notes Generator

An AI-powered web application that converts lecture audio into structured study notes.
It automatically transcribes audio, generates a summary, extracts key points, highlights important sentences, and identifies keywords – all in one place.

🚀 Features

🎙️ Speech to Text – Converts lecture audio (mp3/wav) into text using OpenAI Whisper

📝 Automatic Summary – Generates concise lecture summary

🔑 Key Points Extraction – Lists main points for quick revision

⭐ Important Sentences – Highlights critical sentences from the lecture

🏷️ Keyword Extraction – Identifies important keywords

📄 Download as PDF – Export generated notes as a PDF file

🖥️ User-Friendly UI – Built with Streamlit for easy interaction

🛠️ Tech Stack

Python 3.11

Streamlit – Frontend UI

OpenAI Whisper – Speech-to-text

HuggingFace Transformers – Summarization

NLTK – Sentence processing

ReportLab – PDF generation

📁 Project Structure
internship/
│
├── app.py
├── services/
│   ├── speech_to_text.py
│   ├── summarizer.py
│   ├── keywords.py
│   ├── sentences.py
│
├── utils/
│   ├── file_handler.py
│   ├── pdf_generator.py
│
├── requirements.txt
├── README.md

⚙️ Installation & Setup

Clone the repository

git clone https://github.com/USERNAME/ai-lecture-notes-generator.git
cd ai-lecture-notes-generator


Create virtual environment

python -m venv venv
venv\Scripts\activate


Install dependencies

pip install -r requirements.txt


Run the app

streamlit run app.py

📌 Usage

Upload lecture audio file (mp3/wav)

Wait for transcription and processing

View transcript, summary, key points, keywords and important sentences

Click Download as PDF to save notes

🎯 Purpose of the Project

This project was developed as part of an internship / academic project to demonstrate the practical application of AI in education, helping students convert audio lectures into organized study material efficiently.

📸 Sample Output

Transcript of lecture

Generated summary

Bullet-point key concepts

Highlighted important sentences

Extracted keywords

Downloadable PDF notes

👩‍💻 Author

Minciya K S
BCA Student | AI & Python Enthusiast

⚠️ Note

This project runs locally and is not hosted online.
It is intended for educational and demonstration purposes.