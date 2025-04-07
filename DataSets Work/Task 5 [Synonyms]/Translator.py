from googletrans import Translator

text1 = "Muzammal Ikhlaq"
text2 = "Qamar Ikhlaq"
text3 = "Baba Guru Nanak University Nankana Sahib"

translator = Translator()

# Language Detection
print("Language of text1:", translator.detect(text1))
print("Language of text2:", translator.detect(text2))
print("Language of text3:", translator.detect(text3))

# English to Urdu Translation
translated_text = translator.translate(text3, src='en', dest='ur')
print("Translate English into Urdu:", translated_text.text)
