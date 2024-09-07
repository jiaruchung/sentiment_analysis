
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Download VADER lexicon (only required once)
nltk.download('vader_lexicon')

# Sample survey responses
survey_responses = [
    "I love the new design, it's so intuitive!",
    "The ads are very annoying and distracting.",
    "The page loads fast and works well for me.",
    "The product crashes all the time, I can't use it."
]

# Initialize the VADER sentiment analyzer
vader = SentimentIntensityAnalyzer()

# Analyze each response
for response in survey_responses:
    sentiment_score = vader.polarity_scores(response)
    print(f"Survey Response: {response}")
    print(f"Sentiment Score: {sentiment_score}\n")