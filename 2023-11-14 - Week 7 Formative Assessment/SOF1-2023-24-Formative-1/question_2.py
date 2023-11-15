def time_to_seconds(time):
    time_int = 0
    time_segments = time.split(":")

    if (len(time_segments) == 2 or len(time_segments) == 3):
        if (len(time_segments) > 2): # hh:mm:ss
            if (time_segments[0] == "00" or len(time_segments[0]) < 2):
                return None
            if (int(time_segments[-2]) > 59):
                return None
            if (int(time_segments[0]) > 99):
                return None
            time_int += int(time_segments[0]) * 3600
        else: # mm:ss
            if (int(time_segments[0]) > 59):
                return None
        if (int(time_segments[-1]) > 59):
            return None
        time_int += int(time_segments[-2]) * 60
        time_int += int(time_segments[-1])
    else:
        return None
    return time_int