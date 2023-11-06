def numpairs(input, target):
    pairs = []
    numbers_set = []
    
    for number in input:
        complement = target - number
        if complement in numbers_set:
            pairs.append((complement))
        numbers_set.append(number)

        return pairs

print(numpairs([-1,1,2,4,8],7))




def findpairs(input, target):
    pairs = []

    for i in range(len(input)):
        for j in range(len(input)):
            if input[i] + input[j] == target:
                if (input[j],input[i]) not in pairs: # how disgusting ... 
                    pairs.append((input[i], input[j]))

    return pairs

print(findpairs([-1,1,2,4,8],7))
