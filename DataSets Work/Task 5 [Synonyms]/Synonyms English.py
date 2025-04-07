import nltk
from nltk.corpus import wordnet

# Download NLTK data
nltk.download('wordnet')

converter = []

for muza in wordnet.synsets("love"):
    for m in muza.lemmas():
        converter.append(m.name())

print(set(converter))