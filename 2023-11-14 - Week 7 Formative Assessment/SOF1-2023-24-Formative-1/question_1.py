def seconds_to_time(time):
    """Converts an integer seconds, to a string representing time 
    in hours minutes and seconds, or just minutes and seconds

    Args:
        time (int): the time in solely seconds

    Returns:
        string: time represented in a hh:mm:ss or mm:ss format
        None: if the format is invalid
    """
    minutes = time // 60
    seconds = time % 60
    hours = minutes // 60 #Split minutes in hours
    minutes = minutes % 60 #Leave rest of minutes
    if (time < 0 or 
        (time > 359999)): #Terminate if above 99:59:59
        return None
    if (hours > 0): #Determine format
        return f"{hours:02}:{minutes:02}:{seconds:02}"
    else:
        return f"{minutes:02}:{seconds:02}"