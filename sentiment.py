# Importing required libraries
from textblob import TextBlob
from dataclasses import dataclass


# Define the Mood class
@dataclass
class Mood:
    emoji: str
    sentiment: float
