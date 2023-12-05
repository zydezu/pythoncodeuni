import copy

class Circle:
    "woo"

class Point:
    "woo"

def fakeasscircle():
    circle = Circle()
    circle.x = 100
    circle.y = 200
    circle.point = Point()
    circle.point.x = 12
    circle.point.y = 43
    return circle

def growCircle(circ): # memory alias moment xd
    circ.x += 50
    circ.y += 50

circ = fakeasscircle()
print(f"{circ.point.x} and {circ.point.y}")

circ2 = copy.copy(circ) # shallow copy ( the POINT class will still be aliased )
circ3 = copy.deepcopy(circ) # deep copy ( the POINT class will not be aliased )

circ.point.x += 500
circ.point.y += 600

growCircle(circ)

print(circ.x, circ.y)
print(circ2.x, circ2.y)


print(circ2.point.x, circ2.point.y) # changing Point() in circ will change it in circ2 (shallow copy)
print(circ3.point.x, circ3.point.y) # changing Point() in circ will NOT change it in circ3 (deep copy)

print(type(circ3))
print(type(circ3.point))
print(hasattr(circ3, "point"))





print("=====================")

class Time:
    """represents the time of day. attributes: hour, minute, second"""

time = Time()
time.hour = 11
time.minute = 59
time.second = 30

time2 = Time()
time2.hour = 4
time2.minute = 12
time2.second = 49

def printTime(time):
    print(f"{time.hour:02d}:{time.minute:02d}:{time.second:02d}")

printTime(time)

def isAfter(time1, time2):
    if (f"{time1.hour:02d}:{time1.minute:02d}:{time1.second:02d}" 
        > f"{time2.hour:02d}:{time2.minute:02d}:{time2.second:02d}"):
        return True
    return False

print(isAfter(time, time2))

def add_time(t1, t2): # pure function because it does not modify any of the objects passed to it as arguments 
    sum = Time() 
    sum.hour = t1.hour + t2.hour 
    sum.minute = t1.minute + t2.minute 
    sum.second = t1.second + t2.second 
    if sum.second >= 60:
        sum.second -= 60
        sum.minute += 1
    if sum.minute >= 60:
        sum.minute -= 60
        sum.hour += 1
    return sum

start = Time() 
start.hour = 9 
start.minute = 45 
start.second = 0

duration = Time() 
duration.hour = 1 
duration.minute = 35 
duration.second = 0

done = add_time(start, duration) 
printTime(done)

def increment(time, seconds): 
    time.second += seconds
    if time.second >= 60:
        time.minute += time.second // 60
        time.second = time.second % 60
    if time.minute >= 60:
        time.hour += time.minute // 60
        time.minute = time.minute % 60

def time_to_int(time): # this is a base 60 kinda thing
    minutes = time.hour * 60 + time.minute 
    seconds = minutes * 60 + time.second 
    return seconds

def int_to_time(seconds): 
    time = Time() 
    minutes, time.second = divmod(seconds, 60) # (quotient, remainder) tuple
    time.hour, time.minute = divmod(minutes, 60) 
    return time

sec = time_to_int(time)
print(sec)
printTime(int_to_time(sec))

def add_time_new(t1, t2): 
    seconds = time_to_int(t1) + time_to_int(t2) 
    return int_to_time(seconds) 

def increment_new(time, seconds):
    return int_to_time(time_to_int(time) + seconds)

def time_difference(time1, time2):
    return int_to_time(abs(time_to_int(time1) - time_to_int(time2)))

def valid_time(time): # check for errors, invariants should always be true
    if time.hours < 0 or time.minutes < 0 or time.seconds < 0: 
        return False 
    if time.minutes >= 60 or time.seconds >= 60: 
        return False 
    return True 

def add_time(t1, t2): # use assert to check for errors
    assert valid_time(t1) and valid_time(t2) 
    seconds = time_to_int(t1) + time_to_int(t2) 
    return int_to_time(seconds) 