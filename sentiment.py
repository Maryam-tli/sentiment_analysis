# Importing required libraries
from textblob import TextBlob
from dataclasses import dataclass


# Define the Mood class
@dataclass
class Mood:
    emoji: str
    sentiment: float


# Function to analyze sentiment and return the appropriate mood
def get_mood(input_text: str, *, sensitivity: float) -> Mood:
    polarity = TextBlob(input_text).sentiment.polarity

    friendly_threshold: float = sensitivity  # Threshold for positive sentiment
    hostile_threshold: float = -sensitivity  # Threshold for negative sentiment

    # Determine mood based on the polarity score
    if polarity >= friendly_threshold:
        return Mood('😄', polarity)
    elif polarity <= hostile_threshold:
        return Mood('😤', polarity)
    else:
        return Mood('😐', polarity)
