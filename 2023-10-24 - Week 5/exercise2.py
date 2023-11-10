def concat_dico(dico1, dico2):
    newdico = dict()
    for key, value in dico1.items():
        newdico[key] = value
    for key, value in dico2.items():
        if key in newdico:
            tempList = [newdico[key]]
            tempList.append(value)
            newdico[key] = tempList
        else:
            newdico[key] = value
    return newdico

print(concat_dico({"one":1, "two":2, "five":5},{"two": "10", "five":"101"}))
