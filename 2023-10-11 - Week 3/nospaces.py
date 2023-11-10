sentence = input("Enter a sentence > ")
splitSentence = sentence.split(" ")

newSentence = ""
for element in splitSentence:
    newSentence += element.capitalize()

print(newSentence) 