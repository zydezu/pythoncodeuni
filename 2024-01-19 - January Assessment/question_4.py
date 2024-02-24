def longest_palindromic_numbers(number):
    """Returns a set of the largest palindromic numbers contained
    in a string (of numbers), '0's that are contained at the start
    of a string are removed (as '0110' is not a number, '110' is)

    Args:
        number (string): the string of numbers, of which the longest
        palindromic numbers contained in it will be returned

    Returns:
        set(): returns the set of the longest palindromic numbers
    """

    def check_palindrome(to_check, all_numbers):
        if len(to_check) < 2:
            if all_numbers:
                if len(to_check) >= len(max(all_numbers, key=len)):
                    all_numbers.add(to_check)
            else:
                    all_numbers.add(to_check)
        elif to_check == to_check[::-1]:
            if all_numbers:
                if len(to_check) >= len(max(all_numbers, key=len)):
                    all_numbers.add(to_check)
            else:
                all_numbers.add(to_check)
        else:
            check_palindrome(to_check[:-1], all_numbers)
            check_palindrome(to_check[1:], all_numbers)

    all_numbers = set()
    number = str(int(number))
    if (number == number[::-1]):
        all_numbers.add(number)
    else:
        check_palindrome(number, all_numbers)
    return all_numbers