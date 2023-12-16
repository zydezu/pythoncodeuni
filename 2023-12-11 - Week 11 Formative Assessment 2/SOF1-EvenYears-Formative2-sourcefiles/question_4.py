def check_level(level):
    """Check if a given level is possible to complete.

    Args:
        level (list): a list of non-negative ints, representing
        the level, the starting point being the first index and
        the exit on the last index. 0s represent traps, and
        numbers represent the power up of the springboard.

    Returns:
        bool: Whether the level is possible
    """
    if not level or level[len(level) - 1] == 0 or level[0] == 0:
        return False

    if len(level) == 1:
        return True

    currentitem = level[0]
    if (currentitem > 2):
        return (check_level(level[currentitem-2:]) or
                check_level(level[currentitem-1:]) or
                check_level(level[currentitem:]))
    if (currentitem > 1):
        return (check_level(level[currentitem-1:]) or
                check_level(level[currentitem:]))
    return check_level(level[currentitem:])
