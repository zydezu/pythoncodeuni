listofnumbers = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

largestsum = listofnumbers[0]
for i in range(len(listofnumbers)):
    for j in range(i,len(listofnumbers)):
        total = sum(listofnumbers[i:j]) #splice saves lines ???
        if total > largestsum:
            largestsum = total

print(f"The largest sum is {largestsum}")


array2d = [[6, -5, -7, 4, -4],
           [-9, 3, -6, 5, 2],
           [-10, 4, 7, -6, 3],
           [-8, 9, -3, 3, -7]]

largestsum = 0
 
#find num of items
total2ditems = 0
lengthofrow = len(array2d[0])
columnnumbers = len(array2d)
for item in array2d:
    total2ditems += len(item)

for startindex in range(total2ditems):
    sum = 0




for item in range(startindex, total2ditems):
    print(array2d[item//lengthofrow][item%lengthofrow])


# print(f"The largest sum is: {largestsum}")