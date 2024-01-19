# age = int(input("Please enter your age > ")) #convert to int

print(pow(2,5)) # power

new_list = [0] * 6 # generates empty array

# f strings
# print(f"Square {i+1} - {incrementor} grains, increase of {incrementor*30}mg")


set1 = {1,2,3,4,5}
set2 = {3,4,5,6,7,8}

print(set1.symmetric_difference(set2))

print({x**2 for x in ([0,1,1,1,1,1,2,3,4,5,6])}) #set comprehension

eng2fr = dict()
eng2fr = {'one': 'un', 'two': 'deux', 'three': 'trois'}
print(eng2fr['two'])

values = eng2fr.values()
print('deux' in values)

for xxx in eng2fr:
    print(xxx) #outputs keys



monthsOfYear = dict(zip(range(1,13), ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]))
print(monthsOfYear)

roman = dict()
roman.update({100000:'T', 1000:'M', 500:'D', 100:'K', 50:'L', 10:'X', 5:'V', 1:'I'})

roman.update({100:'C'})
del roman[100000]

print(roman)

def display_dico(dico):
    for key, item in dico.items():
        print(f'{key} --> {item}')

display_dico({"un":1, "deux":2, "trois":3})


sample_text = ("hello hello hello one two THREE four one one one one BYE!")

dictofwords = dict()
for word in sample_text.strip().lower().split():
    dictofwords[word] = dictofwords.get(word, 0) + 1 # consise way of counting words

for key in sorted(dictofwords.keys()):
    print(key,dictofwords[key])

def invert_dict(dico): 
    inverted = dict()
    for key in dico:
        value = dico[key]
        inverted.setdefault(value,[]).append(key) # saves us 2 lines - if list doesn't exist - use default of [] then append a value
    return inverted

print(list(invert_dict(dictofwords).items()))

squared_dict = {x: x**2 for x in range(1,6)}
print(squared_dict)

