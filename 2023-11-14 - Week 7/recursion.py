import string

##--EX1--###########################

def ispalindrome(word):
    """Determines if a string is a palindrome, excluding spaces and punctuation

    Args:
        word (str): the string you want to check

    Returns:
        bool: returns True or False
    """
    word = word.translate(str.maketrans('', '', string.punctuation+" "))
    if (len(word) < 2):
        return True
    if (word[0] == word[-1]):
        return ispalindrome(word[1:-1])
    else:
        return False
        
print(ispalindrome("race.,,,, car"))

##--EX2--###########################

def rec_sum(numbers):
    if (len(numbers) == 0):
        return 0
    else:
        return numbers[0] + rec_sum(numbers[1:]) # splice
    
print(rec_sum([1, 2, 3, 4]))

##--EX3--#############################

def sum_digits(number): #cant convert into string so here use /10 or %10 to manipulate number
    if (number == 0):
        return 0
    else:
        return sum_digits(number // 10) + number % 10
    
print(sum_digits(1234))

##--EX4--#############################

def flatten(mlist):    
    if (mlist == []):
        return []
    if isinstance(mlist, int):
        return [mlist]
    else:
        return flatten(mlist[0]) + flatten(mlist[1:])
            
print(flatten([1,[2,[3,[4]]]]))

##--EX5--#############################

def merge(sorted_listA, sorted_listB):    
    if (sorted_listA == []):
        return ([sorted_listB[0]] 
                + merge([], sorted_listB[1:])) if len(sorted_listA) > 1 else [sorted_listB[0]]
    elif (sorted_listB == []):
        return ([sorted_listA[0]] 
                + merge(sorted_listA[1:], [])) if len(sorted_listB) > 1 else [sorted_listA[0]]
            
    if (sorted_listA[0] > sorted_listB[0]):
        return [sorted_listB[0]] + merge(sorted_listA, sorted_listB[1:])
    else:
        return [sorted_listA[0]] + merge(sorted_listA[1:], sorted_listB)
        
print(merge([1,5,8],[2,6,10]))

##--EX6--#############################

def iselfish(word):
    if len(word) == 0 or word == None:
        return False
    else:
        if 'e' == word[0]:
            return "e" + iselfish(word[1:])
        elif 'l' == word[0]:
            return "l" + iselfish(word[1:])
        elif 'f' == word[0]:
            return "f" + iselfish(word[1:])
        
        if 'e' in word and 'l' in word and 'f' in word: # eh~?
            return True
        else:
            return iselfish(word[1:])
        
    
print(iselfish("g"))

##--EX7--#############################

def is_power(a, b): # recursive
    if(a < b):
        return False
    if (a/b == b):
        return True
    else:
        return is_power(a/b, b)
    
print(is_power(2541865828329,3))

def is_power_iterative(a, b): # iterative
    while (a > b):
        if (a/b == b):
            return True
        else:
            a = a/b
    return False

print(is_power_iterative(9,3))