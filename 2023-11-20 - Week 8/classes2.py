import copy
import math 

class Time(object): 
    """represents the time of day. 
    attributes: hour, minute, second"""

    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second
   
    def __str__(self):
       return ('%.2d:%.2d:%.2d' % (self.hour,self.minute,self.second))

    def __add__(self, other): # operator overloading
        if isinstance(other, Time):
            return int_to_time(self.time_to_int() + other.time_to_int())
        elif (isinstance(other, int) 
              and not isinstance(other, bool)):
            return self.increment(other)
        else:
            raise TypeError("can't add Time with " +
                            type(other).__qualname__)
        
    def __radd__(self, other):
        return self.__add__(other)

    def time_to_int(self): 
        minutes = self.hour * 60 + self.minute 
        seconds = minutes * 60 + self.second 
        return seconds 

    def increment(self, seconds):
        seconds += self.time_to_int()
        return int_to_time(seconds)
    
    def is_after(self, other):
        return self.time_to_int() > other.time_to_int()
    
def int_to_time(seconds): 
    time = Time() 
    minutes, time.second = divmod(seconds, 60) # (quotient, remainder) tuple
    time.hour, time.minute = divmod(minutes, 60) 
    return time

start = Time(9,45,0)
print(start)
print(start.time_to_int())

end = start.increment(1337)
print(end)

print(end.is_after(start))

print(start + end)
print(start + 42002)
print(start.__dict__)

print("===========================")

class Circle:
    def __init__(self, centre, radius):
        self.centre = centre
        self.radius = radius

    def getArea(self):
        return math.pi * self.radius * self.radius
    
    def getPerimeter(self):
        return math.pi * self.radius * 2
    
    @property
    def radiusset(self):
        return self.radius
    
    @radiusset.setter
    def radiusset(self, r):
        self.radius = r


circle1 = Circle((8,5), 5.2)
print(circle1.getArea())
print(circle1.getPerimeter())
print(circle1.__dict__)
print(circle1.radiusset)

class Triangle:
    def __init__(self, vertices):
        self.vertices = vertices

    def __str__(self):
        return f"Points: {self.vertices}"
    
    def getArea(self):
        a = self.vertices[0]
        b = self.vertices[1]
        c = self.vertices[2]
        area = abs(
            (a[0] * (b[1] - c[0]) 
            + b[0] * (c[1] - a[1]) 
            + c[0] * (a[1] - b[1]))
            / 2
        )
        return area
    
    def getPerimeter(self):
        a = self.vertices[0]
        b = self.vertices[1]
        c = self.vertices[2]
        perimeter = (pow(pow(abs(a[0]-b[0]),2) + pow(abs(a[1]-b[1]),2), 0.5) 
                     + pow(pow(abs(a[0]-c[0]),2) + pow(abs(a[1]-c[1]),2), 0.5) 
                     + pow(pow(abs(b[0]-c[0]),2) + pow(abs(b[1]-c[1]),2), 0.5))
        return perimeter
    
    def getInscribedCircle(self):
        a = self.vertices[0]
        b = self.vertices[1]
        c = self.vertices[2]
        la = pow(pow(abs(a[0]-b[0]),2) + pow(abs(a[1]-b[1]),2), 0.5) 
        lb = pow(pow(abs(a[0]-c[0]),2) + pow(abs(a[1]-c[1]),2), 0.5)
        lc = pow(pow(abs(b[0]-c[0]),2) + pow(abs(b[1]-c[1]),2), 0.5)
                
        point = ((la*a[0] + lb*b[0] + lc*c[0])/(la+lb+lc)
                 ,(la*a[1] + lb*b[1] + lc*c[1])/(la+lb+lc))

        s = 0.5 * (la + lb + lc)
        radius = pow(((s-la)*(s-lb)*(s-lc) / s), 0.5)

        return Circle((point), radius)

    def getCircumscribedCircle(self):
        a = self.vertices[0]
        b = self.vertices[1]
        c = self.vertices[2]
        la = pow(pow(abs(a[0]-b[0]),2) + pow(abs(a[1]-b[1]),2), 0.5) 
        lb = pow(pow(abs(a[0]-c[0]),2) + pow(abs(a[1]-c[1]),2), 0.5)
        lc = pow(pow(abs(b[0]-c[0]),2) + pow(abs(b[1]-c[1]),2), 0.5)

        point = (0,0)

        s = 0.5 * (la + lb + lc)
        radius = ((la*lb*lc) 
                  / 4 * pow((s * (s - la) * (s - lb) * (s - lc)), 0.5))


        return Circle((point), radius)




tri1 = Triangle([(0,0),(5,0),(0,7)])
print(tri1)
print(tri1.getArea())
print(tri1.getPerimeter())
print(tri1.getInscribedCircle().__dict__)
print(tri1.getCircumscribedCircle().__dict__)