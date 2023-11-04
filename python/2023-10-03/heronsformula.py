length_a = float(input("Input the size of length a > "))
length_b = float(input("Input the size of length b > "))
length_c = float(input("Input the size of length c > "))

s = (length_a+length_b+length_c)/2
area = pow(s*(s-length_a)*(s-length_b)*(s-length_c),0.5)
print("The area of the triangle is",area)