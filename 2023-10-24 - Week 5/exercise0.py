monthsOfYear = dict(zip(range(1,13), ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]))
print(monthsOfYear)

roman = dict()
roman.update({100000:'T', 1000:'M', 500:'D', 100:'K', 50:'L', 10:'X', 5:'V', 1:'I'})

roman.update({100:'C'})
del roman[100000]

print(roman)