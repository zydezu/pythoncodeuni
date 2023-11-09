def save_list2file(sentences, filename):
    f = open(f"2023-11-09\\{filename}",'w') # GIT !
    for sentence in sentences:
        f.write(sentence+"\n")

save_list2file(["hello","this","is","urrrffggh","ooougughhhhhhhhhh"],'ex2.txt')