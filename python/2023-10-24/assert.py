set1 = {1,2,3,4,5}
set2 = {3,4,5,6,7,8}

print(set1.symmetric_difference(set2))

print({x**2 for x in ([0,1,1,1,1,1,2,3,4,5,6])}) #set comprehension

eng2fr = dict()
eng2fr = {'one': 'un', 'two': 'deux', 'three': 'trois'}
print(eng2fr['two'])

values = eng2fr.values()
print('deux' in values)

for dict in eng2fr:
    print(dict) #outputs keys