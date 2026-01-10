import nltk
from nltk.tokenize import sent_tokenize

# Ensure punkt is available (only downloads once, very small)
try:
    nltk.data.find("tokenizers/punkt")
except LookupError:
    nltk.download("punkt")

def extract_important_sentences(text, max_sentences=5):
    sentences = sent_tokenize(text)

    # Simple importance logic: longer + informative sentences
    sentences = sorted(sentences, key=lambda s: len(s), reverse=True)

    return sentences[:max_sentences]
