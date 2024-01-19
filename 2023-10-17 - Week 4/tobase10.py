def to_base10(binary):
    sum = 0
    power = len(binary)
    for i in range(0,len(binary)):
        power-=1 # power increments from right to left, whilst i go through the numbers left to right
        sum += int(binary[i]) * pow(2,power)
    return sum

print(to_base10(input("Enter a base 2 binary number to convert to base 10 denary > ")))