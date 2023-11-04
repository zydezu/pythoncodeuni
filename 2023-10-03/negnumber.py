number_sum = 0
number_count = 0
even_number_count = 0
while True:
    user_input = int(input("Input a number > "))
    if (user_input < 0): # negative
        break
    number_sum = user_input + number_sum
    number_count+=1 # increment count by one
    if (user_input%2==0):
        even_number_count+=1

print("Sum of all numbers:",number_sum)
print("Average of all numbers:",number_sum/number_count)
print("Amount of even numbers:",even_number_count)