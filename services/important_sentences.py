import re
from collections import Counter

def extract_important_sentences(text, top_n=5):
    # Split into sentences
    sentences = re.split(r'(?<=[.!?]) +', text)
    sentences = [s.strip() for s in sentences if len(s.strip()) > 40]

    # Basic stopwords
    stopwords = set([
        "the","is","are","was","were","and","or","of","to","in","on","for","with","as",
        "by","an","a","at","from","that","this","it","be","has","have","had","not",
        "but","they","you","we","he","she","them","his","her","their","our"
    ])

    # Word frequency
    words = re.findall(r'\w+', text.lower())
    words = [w for w in words if w not in stopwords and len(w) > 2]
    freq = Counter(words)

    sentence_scores = {}
    for sentence in sentences:
        score = 0
        for word in re.findall(r'\w+', sentence.lower()):
            score += freq.get(word, 0)
        sentence_scores[sentence] = score

    # Sort by score
    ranked = sorted(sentence_scores.items(), key=lambda x: x[1], reverse=True)

    return [s[0] for s in ranked[:top_n]]
