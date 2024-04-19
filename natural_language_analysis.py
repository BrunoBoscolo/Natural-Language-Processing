import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA
#nltk.download('vader_lexicon')
#nltk.download('movie_reviews')
#nltk.download('punkt')

sia = SIA()
sentiment = sia.polarity_scores("I love love love love this kitten")
print(sentiment['compound'])