def sum_lists(list_2D):
    output = []
    for list in list_2D:
        sum = 0
        for innerlist in list:
            sum+=innerlist
        output.append(sum)
    return output
            
data = [[1,2,3], [2], [1, 2, 3, 4]]
print(sum_lists(data))