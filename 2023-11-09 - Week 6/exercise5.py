def to_upper_case(input_file, output_file):
    prefix = "2023-11-09\\"
    f = open(prefix+input_file, 'r')
    originalLines = f.readlines()
    f.close()
    
    newLinesToWrite = []
    for line in originalLines:
        newLinesToWrite.append(line.upper())
    
    f = open(prefix+output_file, 'w')
    f.writelines(newLinesToWrite)

to_upper_case("ex2.txt", "ex5.txt")