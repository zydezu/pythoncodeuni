def hammingDistance(word1, word2):
    count = 0
    if (len(word1) != len(word2)):
        raise ValueError("Strings aren't the same length!")
    else:
        for i in range(0, len(word1)):
            if (word1[i] != word2[i]):
                count += 1
    return count

print(hammingDistance("karolin","kathrin"))
print(hammingDistance("karolin","kerstin"))
print(hammingDistance("1011101","1001001"))

    