def seconds_to_time(time):
    minutes = time // 60
    seconds = time % 60
    hours = minutes // 60
    minutes = minutes % 60
    if (time < 0 or 
        (time > 359999)):
        return None
    if (hours > 0):
        return f"{hours:02}:{minutes:02}:{seconds:02}"
    else:
        return f"{minutes:02}:{seconds:02}"

print(seconds_to_time(85))