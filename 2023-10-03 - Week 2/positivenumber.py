pos_int = int(input("Enter a positive integer > "))
    
factorial = pos_int
j = pos_int
for i in range(1,pos_int):
    j-=1
    factorial = factorial * j
    
print(factorial)