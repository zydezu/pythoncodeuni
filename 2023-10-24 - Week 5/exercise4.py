def reverse_dictionary(dico):
    reversedict = dict()
    for key, value in dico.items():
        if value in reversedict:
            print("ERROR: keys has duplicates")
            return None
        reversedict[value] = key
    return reversedict

print(reverse_dictionary({"one":1, "two":2, "three":3}))