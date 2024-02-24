def string_pattern(size):
    """Creates a X pattern using + and - symbols.

    Args:
        size (int): The size of the X pattern

    Raises:
        ValueError: If the size provided is smaller or equal to 2.

    Returns:
        str: A X pattern using + and - symbols        
    """
    if size < 3:
        raise ValueError("Invalid size." )
    pattern = ""
    for row in range(size):
        for column in range(size):
            if row == column or column == size -1 - row:
                pattern += "+"
            else:
                pattern += "-"
        pattern += "\n"
    return pattern
