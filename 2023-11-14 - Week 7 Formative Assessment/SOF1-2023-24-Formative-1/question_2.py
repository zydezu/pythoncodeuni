def time_to_seconds(time):
    """Converts the string- time, to an seconds as an integer

    Args:
        time (string): a string representing time in the format 
        hh:mm:ss or mm:ss (it cannot be 00:50:24 and must be 50:24)

    Returns:
        int: the time inputed, represented solely in seconds
        None: if the format is invalid
    """
    time_int = 0
    time_segments = time.split(":")

    if (len(time_segments) == 2 or len(time_segments) == 3):
        if (len(time_segments) > 2): #hh:mm:ss
            if (time_segments[0] == "00" or len(time_segments[0]) < 2):
                return None
            if (int(time_segments[-2]) > 59): #seconds/minutes
                return None
            if (int(time_segments[0]) > 99):
                return None
            time_int += int(time_segments[0]) * 3600 #Add hours
        else: # mm:ss
            if (int(time_segments[0]) > 59):
                return None
        if (int(time_segments[-1]) > 59):
            return None
        time_int += int(time_segments[-2]) * 60 #Add minutes
        time_int += int(time_segments[-1]) #Add seconds
    else:
        return None
    return time_int