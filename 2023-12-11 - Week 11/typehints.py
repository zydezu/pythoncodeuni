from typing import Union, Optional, List, Dict, Tuple







def add(a: int, b: int) -> int:
    return a + b





def sum_digits(number: Union[str, int]) -> int:
    digits = [int(x) for x in str(number)]
    return sum(digits)

print(sum_digits("1234"))
print(sum_digits(1234))





# print(sum_digits(1234.0)) # would result in a type error during static analysis



def greet(name: Optional[str]="Stranger") -> str:
    return f"Hello, {name}!"
    
print(greet("Alice"))
print(greet())

print(greet(42)) # invalid in type checking

