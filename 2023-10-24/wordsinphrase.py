sample_text = ("hello hello hello one two THREE four one one one one BYE!")

dictofwords = dict()
for word in sample_text.strip().lower().split():
    dictofwords[word] = dictofwords.get(word, 0) + 1

for key in sorted(dictofwords.keys()):
    print(key,dictofwords[key])

def reverse_lookup(dico, value):
    for key in dico:
        if dico[key] == value:
            return key
    return None

print(reverse_lookup(dictofwords,5))

def invert_dict(dico): 
    inverted = dict()
    for key in dico:
        value = dico[key]
        inverted.setdefault(value,[]).append(key) # saves us 2 lines - if list doesn't exist - use default of [] then append a value
    return inverted

print(list(invert_dict(dictofwords).items()))

dictofwords.update({'f':3,'g':7})
print(dictofwords)

for key, val  in dictofwords.items(): #this is because .items() products a tuple
    print(key, val)

squared_dict = {x: x**2 for x in range(5)}
print(squared_dict)