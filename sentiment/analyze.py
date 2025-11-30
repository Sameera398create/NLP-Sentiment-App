from textblob import TextBlob

def analyze_sentiment(text: str):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    if polarity > 0:
        mood = "Positive 😊"
    elif polarity < 0:
        mood = "Negative 😡"
    else:
        mood = "Neutral 😐"

    return {"polarity": polarity, "mood": mood}
