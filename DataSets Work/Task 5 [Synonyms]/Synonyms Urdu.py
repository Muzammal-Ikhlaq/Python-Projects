import nltk
from nltk.corpus import wordnet
from deep_translator import GoogleTranslator

# Download NLTK data if not already downloaded
nltk.download('wordnet')

# Take input in Urdu
urdu_input = input("Enter your Urdu text: ")

# Translate Urdu to English
translator = GoogleTranslator(source='ur', target='en')
english_text = translator.translate(urdu_input)
print(f"Translated to English: {english_text}")

# Find synonyms using WordNet
synonyms = []
for synset in wordnet.synsets(english_text):
    for lemma in synset.lemmas():
        synonyms.append(lemma.name())

# Remove duplicates
synonyms = list(set(synonyms))

# Translate synonyms back to Urdu
urdu_synonyms = [GoogleTranslator(source='en', target='ur').translate(word) for word in synonyms]

print("Synonyms in Urdu:", urdu_synonyms)
