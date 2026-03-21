import spacy
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Load models
nlp = spacy.load("en_core_web_sm")
analyzer = SentimentIntensityAnalyzer()


# 🔹 Category Classification
def classify_complaint(text):
    text_lower = text.lower()

    if "garbage" in text_lower or "waste" in text_lower or "trash" in text_lower:
        return "Garbage"
    elif "water" in text_lower or "leak" in text_lower:
        return "Water"
    elif "road" in text_lower or "pothole" in text_lower:
        return "Road"
    elif "electricity" in text_lower or "power" in text_lower:
        return "Electricity"

    return "Other"


# 🔹 Sentiment + Urgency
def analyze_sentiment(text):
    score = analyzer.polarity_scores(text)["compound"]

    if score >= 0.05:
        return "Positive", "Low"
    elif score <= -0.05:
        return "Negative", "High"
    else:
        return "Neutral", "Medium"


# 🔹 Location Extraction (FIXED)
def extract_location(text):
    doc = nlp(text)

    # Try spaCy NER
    locations = [ent.text for ent in doc.ents if ent.label_ in ["GPE", "LOC"]]

    if locations:
        return " ".join(locations)

    # Fallback logic
    keywords = ["nagar", "road", "street", "area", "colony", "layout"]

    words = text.split()
    for i in range(len(words)):
        for key in keywords:
            if key.lower() in words[i].lower():
                if i > 0:
                    return words[i - 1] + " " + words[i]
                return words[i]

    return "Unknown"