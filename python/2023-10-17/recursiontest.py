def factorial(n):
    if n==0:
        return 1
    return n*factorial(n-1)

print(factorial(5))


def print_n(s, n): 
    if n <= 0: 
        return 
    print(s) 
    print_n(s, n-1)

print_n("hello",5)