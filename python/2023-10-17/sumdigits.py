def sum_digits(number):
    numstring = number #casting to stop errors
    sum = 0
    for num in numstring:
        sum+=int(num) #casting AGAIN
    return sum

print(sum_digits(input("Enter digits to sum > "))) # c# would hate this