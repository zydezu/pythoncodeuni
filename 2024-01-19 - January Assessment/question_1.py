def string_pattern(size):
    """Output an X to the console, of various sizes.

    Args:
        size (int): The amount of lines the console outputted X
        will take up, must be larger than 2.

    Returns:
        string: The outputted X
    """
    if size <= 2: 
        raise ValueError("Size should be larger than 2")

    lines = []
    for i in range(size):
        builder = ["-" for x in range(size)]
        builder[i] = "+"
        builder[size-1-i] = "+"
        builder[-1] = builder[-1] + "\n" # line break at the very end
        lines.append(''.join(builder)) # quickly convert list to string

    return ''.join(lines)