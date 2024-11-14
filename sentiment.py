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


# Function to run the sentiment analysis bot
def run_bot():
    print('Bot : Enter some text and I will perform a sentiment analysis on it.')
    while True:
        user_input: str = input('you: ')
        mood: Mood = get_mood(user_input, sensitivity=0.3)
        print(f'Bot : {mood.emoji} ({mood.sentiment})')


# Entry point to start the bot
if __name__ == '__main__':
    run_bot()  # Start the bot when the script is executed