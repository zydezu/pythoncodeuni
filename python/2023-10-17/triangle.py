flip = 1
rows = int(input("Input number of rows: "))

for i in range(1, rows+1):
    builder = ""
    for j in range(0, i):
        builder += str(flip)
        flip = 1 - flip
    print(builder)