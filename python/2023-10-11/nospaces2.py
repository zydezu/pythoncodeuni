sentence = input("Enter a sentence in CamelCase > ")

newSentence = []
wordBuilder = ""
for i in range(len(sentence)):
    if (sentence[i].isupper() and i>0):
        newSentence.append(wordBuilder)
        wordBuilder = ""
    wordBuilder+=sentence[i]
    if (i+1 == len(sentence)):
        newSentence.append(wordBuilder)

print(newSentence)