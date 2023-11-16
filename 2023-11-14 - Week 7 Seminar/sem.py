def sum_all(numbers):
    if (numbers == []):
        return 0
    if isinstance(numbers, int):
        return numbers
    else:
        return sum_all(numbers[0]) + sum_all(numbers[1:])
    
print(sum_all([111,[2,[3,4]]]))