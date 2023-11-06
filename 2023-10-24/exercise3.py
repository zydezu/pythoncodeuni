def map_list(keys, values):
    newdict = dict()
    for i in range(len(keys)):
        if keys[i] in newdict:
            print("ERROR: keys has duplicates")
            return None
        newdict.update({keys[i]: values[i]})
    return newdict

print(map_list(['un', 'two', 'three'], [1,2,3]))
