def common_values(lst1, lst2):
    """Return shared values between the two lists.

    Args:
        lst1 (list): first list of values
        lst2 (list): second list of values

    Returns:
        list: A list with the values seen in both lists
    """
    values = list(set(lst1).intersection(set(lst2)))
    return values
