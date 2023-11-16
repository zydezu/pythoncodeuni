def wildcard_pattern(input):
    print(input)

    if "?" not in input:
        return input

    solutions = []

    if input[0] == "?":
        solutions.append(wildcard_pattern("0" + input[1:]))
        solutions.append(wildcard_pattern("1" + input[1:]))
    else:
        solutions.append(wildcard_pattern(input[1:]))

    return solutions

print(wildcard_pattern("1?11"))