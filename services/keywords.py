import re
from collections import Counter

def extract_keywords(text, top_n=10):
    # Lowercase and remove special characters
    text = text.lower()
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)

    words = text.split()

    # Basic stopwords (we avoid nltk to keep it light)
    stopwords = set([
        "the", "is", "are", "was", "were", "a", "an", "and", "or", "of", "to", "in",
        "that", "this", "it", "for", "on", "with", "as", "by", "at", "from", "be",
        "has", "have", "had", "but", "not", "they", "their", "we", "you", "he", "she"
    ])

    filtered_words = [w for w in words if w not in stopwords and len(w) > 3]

    word_counts = Counter(filtered_words)

    common = word_counts.most_common(top_n)

    keywords = [word for word, count in common]

    return keywords
