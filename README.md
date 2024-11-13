Sentiment Analysis Bot

A simple sentiment analysis bot built using Python and the TextBlob library. This bot analyzes the sentiment of user-provided text and responds with emojis indicating the mood (positive, negative, or neutral) based on the sentiment score.

Features
Sentiment Analysis: Analyzes the sentiment of user input.
Emoji Response: Provides an emoji based on the sentiment:
😄 for positive sentiment
😤 for negative sentiment
😐 for neutral sentiment
Customizable Sensitivity: The sensitivity parameter allows for adjustment of the threshold for determining positive, neutral, and negative sentiments.
Requirements
Python 3.x
TextBlob library for sentiment analysis
Python's built-in dataclasses module (for Python 3.7+)
Installation
Clone this repository:

git clone https://github.com/Maryam-tli/sentiment_analysis.git
Navigate to the project directory:

cd your-repository-name
Install the required dependencies using pip:

pip install textblob
If you are using Python 3.6 or older, you may need to install the dataclasses module:

pip install dataclasses
Usage
To run the sentiment analysis bot, execute the following command:

python sentiment_bot.py
Once the program is running, the bot will prompt you for text input:

Bot : Enter some text and I will perform a sentiment analysis on it.
Enter some text, and the bot will respond with an emoji and sentiment score:

you: I love this project!
Bot : 😄 (0.8)
Positive sentiment (emoji: 😄) for sentiment score greater than the positive threshold.
Negative sentiment (emoji: 😤) for sentiment score lower than the negative threshold.
Neutral sentiment (emoji: 😐) for sentiment score within the range of the positive and negative thresholds.
Adjust Sensitivity: You can adjust the sensitivity (thresholds for sentiment) by modifying the sensitivity parameter in the get_mood() function. The higher the sensitivity, the more easily the bot will classify emotions as positive or negative.

Contributing
Feel free to contribute to the project by submitting pull requests. You can improve the functionality, add more features, or fix bugs. Please follow the standard GitHub workflow for contributing:

Fork the repository.
Create a new branch for your feature or bug fix.
Open a pull request with a detailed description of the changes.
