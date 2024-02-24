def longest_palindromic_numbers(number):
    """Returns the set of the longuest palindromic numbers within a number.

    Args:
        number (str): the number from which to extract the longuest 
            palindromic numbers.

    Returns:
        a set of string containing the longuest palindromic number whitin number.
    """
    def rec_call(number):
        # a number composed of a single digit is palindromic It includes the
        # number 0.
        if len(number) <= 1:
            return len(number), {number}
        # at this stage a number starting with a 0 is not a valid number.
        if is_palindrome(number) and not number.startswith("0"):
            return len(number), {number}

        # At this stage number is not palindromic so we need to look at the
        # number without its first digit, and also the number without its last
        # digit.
        without_first_size, without_first_set = rec_call(number[1:])
        without_last_size, without_last_set = rec_call(number[:-1])
        if without_first_size > without_last_size:
            return without_first_size, without_first_set
        if without_first_size == without_last_size:
            return without_last_size, without_first_set | without_last_set

        return without_last_size, without_last_set

    _, palindromes = rec_call(number)
    return palindromes

def is_palindrome(number) -> bool:
    """Returns True if the number is palindromic, False otherwise.

    Args:
        number (str): The number to be checked.

    Returns:
        bool: True if the number is palindromic, False otherwise.
    """
    if len(number) <= 1:
        return True
    if number[0] != number[-1]:
        return False
    return is_palindrome(number[1:-1])
    # Note, for this helper function, return number == number[::-1],
    # or a non recursice function were accepted as well.
