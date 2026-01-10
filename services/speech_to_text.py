import whisper
import os

model = whisper.load_model("base")


def transcribe_audio(file_path):
    if not os.path.exists(file_path):
        return "❌ Error: Audio file not found."

    try:
        result = model.transcribe(file_path)

        text = result.get("text", "").strip()

        if not text:
            return "⚠️ No speech detected in the audio."

        return text

    except Exception as e:
        return f"❌ Transcription failed: {str(e)}"
