def sumall(*nums):
    total = 0
    for num in nums:
        total+=num
    return total

print(sumall(1,2,3,3,4,5))