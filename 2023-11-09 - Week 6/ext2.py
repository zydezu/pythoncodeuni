import string

sample_text = (" As Python s creator, I'd like to say a few words about its "+
              "origins adding a bit of personal philosophy. "+
              "Over six years ago in December I was looking for a "+
              "hobby programming project that would keep me occupied "+
              "during the week around Christmas. My office, "+
              "a government run research lab in Amsterdam would be closed "+
              "but I had a home computer and not much else on my hands "+
              " I decided to write an interpreter for the new scripting "+
              "language  I had been thinking about lately a descendant of ABC "+
              "that would appeal to UnixC hackers I chose Python as a "+
              "working title for   the project being in a slightly irreverent "+
              "mood and a big fan of Monty Python s Flying Circus.  ")

######################### EXERCISE 1 ##########################################

def get_words_frequencies(text):
    """
    Counts the frequencies of words in a given text
    
    args:
        text (str): the text the split
        
    returns:
        dict: the words, and their corresponding frequencies
    """
    
    delimiters = string.punctuation + " "
    word_counts = dict()
    stringbuilder = ""
    for char in text:
        if (char in delimiters):
            if (stringbuilder):
                word_counts[stringbuilder] = word_counts.get(stringbuilder, 0) + 1 #Default value if that word hasn't been counted yet
                stringbuilder = ""
        else:
            stringbuilder += char.lower() # Case insensitivity
    
    return word_counts
            
print(get_words_frequencies(sample_text))