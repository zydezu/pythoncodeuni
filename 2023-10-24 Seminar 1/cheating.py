def numpairs(input, target):
    pairs = []
    numbers_set = {}
    
    for num in input:
        complement = target - num
        if complement in numbers_set:
            pairs.append((complement,num))
        #numbers_set.update(set(complement))

    return pairs

print(numpairs([2,4,5,7],9))




def findpairs(input, target):
    pairs = []

    for i in range(len(input)):
        for j in range(len(input)):
            if input[i] + input[j] == target:
                if (input[j],input[i]) not in pairs: # how disgusting ... 
                    pairs.append((input[i], input[j]))

    return pairs

print(findpairs([2,4,5,7],9))




# thats just f  c     cccccccccccccccccccccccccccccccccccc      fwordf_^_  oough,mhghm  im so min-maxing rightnow

def stupidassminmaxmethod(input, target):
    pairs = []
    min = 0
    max = len(input) - 1

    while max > min:
        if input[min] + input[max] == target:
            pairs.append((input[min], input[max]))
            min+=1
            max-=1
        elif input[min] + input[max] < 0:
            min+=1
        else:
            max+=1

    return pairs

print(stupidassminmaxmethod([2,4,5,7],9))




def merge(listA, listB):
    mergedList = []
    indexA = 0
    indexB = 0

    while indexA < len(listA) and indexB < len(listB):
        if listA[indexA] <= listB[indexB]:
            mergedList.append(listA[indexA])
            indexA+=1
        else:
            mergedList.append(listB[indexB])
            indexB+=1
        
    while indexA < len(listA): #lists and not equal in length
        mergedList.append(listA[indexA])
        indexA+=1

    while indexB < len(listB):
        mergedList.append(listB[indexB])
        indexB+=1

    return mergedList


print(merge([1,3,4,7],[2,3,5]))