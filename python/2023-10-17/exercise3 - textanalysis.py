sample_text = (" As Python s creator I d like to say a few words about its "+
              "origins adding a bit of personal philosophy "+
              "Over six years ago in December I was looking for a "+
              "hobby programming project that would keep me occupied "+
              "during the week around Christmas My office "+
              "a government run research lab in Amsterdam would be closed "+
              "but I had a home computer and not much else on my hands "+
              " I decided to write an interpreter for the new scripting "+
              "language  I had been thinking about lately a descendant of ABC "+
              "that would appeal to UnixC hackers I chose Python as a "+
              "working title for   the project being in a slightly irreverent "+
              "mood and a big fan of Monty Python s Flying Circus")

def get_words_starting_with(text, letter):
    finalWords = []
    tempWords = text.split(" ")
    for word in tempWords:
        if (len(word)>0):
            if (word[0].capitalize() == letter.capitalize()):
                if (not word in finalWords):
                    finalWords.append(word)    
    return finalWords

print(get_words_starting_with(sample_text, input("Enter letter > ")))