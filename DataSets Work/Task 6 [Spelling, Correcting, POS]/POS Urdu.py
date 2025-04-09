import stanza

# Urdu sentence
sentence = "میں یونیورسٹی جا رہا ہوں"

# Initialize Stanza for Urdu
stanza.download('ur')
nlp = stanza.Pipeline('ur')

# Process the sentence
doc = nlp(sentence)

# Print words with POS tags
for sentence in doc.sentences:
    for word in sentence.words:
        print(word.text,word.upos)