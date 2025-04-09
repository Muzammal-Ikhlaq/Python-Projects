import spacy

# English sentence
sentence = "I am going to university"

# Initialize Spacy for English
nlp = spacy.load('en_core_web_sm')

# Process the sentence
doc = nlp(sentence)

# Print words with POS tags
for token in doc:
    print(f"{token.text} --> {token.pos_}")