basefine = 100
extrapermph = 5

def calculateFine(speed, limit):
    if (not speed > limit): return 0
    total = basefine + ((speed - limit) * extrapermph)
    if (speed >= 90):
        total += 200
    return total

print(calculateFine(60,50))
print(calculateFine(90,70))
print(calculateFine(70,70))
