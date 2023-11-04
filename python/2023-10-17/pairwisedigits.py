def pairwise_digits(number_a, number_b):
    binaryresult = [0] * max(len(number_a), len(number_b)) # generate array length of longest number
    for i in range(0, len(number_a)):
        if (i>len(number_b)-1): # stop Out of Range error
            break
        if (number_a[i] == number_b[i]):
            binaryresult[i] = 1 # modify array of [0]'s
    return binaryresult

num1 = input("Enter the first number > ")
num2 = input("Enter the second number > ")
print(pairwise_digits(num1, num2))