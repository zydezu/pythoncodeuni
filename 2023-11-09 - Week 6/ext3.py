def flatten(list_2d):
    list_1d = []
    for i in range(len(list_2d)):
        for item in list_2d[i]:
            list_1d.append(item)
    return list_1d

print(flatten([[1,2,3,4,5]]))