import pandas as pd
import nltk
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download necessary NLTK data
nltk.download('stopwords')
nltk.download('punkt')

# Load CSV file
df = pd.read_csv('twitter_training.csv', header=None, names=['id', 'game', 'sentiment', 'text'])

# Stopwords and Punctuation List
stop_words = set(stopwords.words('english'))
punctuation_chars = set(string.punctuation)

# Function (Remove stopwords & punctuation)
def clean_text(text):
    words = word_tokenize(str(text))
    filtered_words = [word for word in words if word.lower() not in stop_words and word not in punctuation_chars]
    return ' '.join(filtered_words)

# Apply cleaning function
df['cleaned_text'] = df['text'].apply(clean_text)

# Save cleaned data
df.to_csv('Final_twitter_training.csv')
print("Stop words and punctuation removed successfully!")
