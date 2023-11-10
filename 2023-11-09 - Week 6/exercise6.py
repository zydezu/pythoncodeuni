def sum_numbers_in_file(input_file):
    prefix = "2023-11-09\\"
    f = open(prefix+input_file, 'r')
    allLines = f.readlines()
    f.close()

    total = 0

    for line in allLines:
        total += sumThisLine(line)
    
    return total    

def sumThisLine(line):
    localSum = 0
    nums = line.split()
    for num in nums:
        localSum += int(num)
    return localSum

print(sum_numbers_in_file("numsum.txt"))