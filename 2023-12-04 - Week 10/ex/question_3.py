def getWordsIndices(filename):
    results = dict()
    index = 0
    for word in open(filename ,'r').readline().split(): # zero error check =)
        word = word.lower()
        index += 1
        results.setdefault(word, []).append(index) # remember this stupid

    return results

print(getWordsIndices('2023-12-04 - Week 10\\ex\\sampleText.txt'))