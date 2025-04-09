# ----------- First Method ----------------- #

# from textblob import TextBlob
# import nltk
# nltk.download('brown')  # Used for spell-checking
#
# text = input("Enter Text: \n")
# text = text.split(" ")
# correctText = " "
#
# for i in text:
#     correctWord = TextBlob(i)
#     correctText += str(correctWord.correct()) + " "
#
# print("Correct Spelling is: ")
# print(correctText)

# ----------- Second Method ----------------- #

from spellchecker import SpellChecker

spell = SpellChecker()
text = input("Enter Text: \n").split(" ")
correctText = ""

for word in text:
    corrected = spell.correction(word)
    correctText += (corrected if corrected else word) + " "

print("Correct Spelling is: ")
print(correctText.strip())