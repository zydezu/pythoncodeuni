
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

def split_text(text, delimiters = " "):
    """
    Splits a string with the given delimiters
    
    args:
        text (str): the text the split
        delimiters (list): the specific characters the text is split at
        
    returns:
        list: all the splits of the text
    """
    
    splits = []
    stringbuilder = ""
    for char in text:
        if (char in delimiters): # if current character is delimiter
            if (stringbuilder): # if current split is not empty
                splits.append(stringbuilder) # add split to list
                stringbuilder = ""
        else:
            stringbuilder += char
    if (stringbuilder): # end of function, append rest of stringbuilder to list
        splits.append(stringbuilder)
    
    return splits
            
print(split_text(sample_text, ", '."))