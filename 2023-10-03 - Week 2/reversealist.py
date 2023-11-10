stringofnumbers = "1,2,3,4,5,good,morning,USA"
list1 = stringofnumbers.split(',')
new_list = [0] * len(list1) # generates empty array

j = len(list1)
for i in range(len(list1)):
    j = j-1
    new_list[j] = list1[i]
    
print(new_list)