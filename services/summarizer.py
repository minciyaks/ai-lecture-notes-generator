from transformers import pipeline

# Load summarization pipeline
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")


def generate_summary_and_points(text):
    # Limit text length to avoid model crash
    text = text[:3000]

    summary_output = summarizer(text, max_length=200, min_length=80, do_sample=False)
    summary = summary_output[0]["summary_text"]

    # Simple key point extraction from summary
    key_points = [line.strip() for line in summary.split(". ") if line.strip()]
    key_points = key_points[:5]

    return summary, key_points
