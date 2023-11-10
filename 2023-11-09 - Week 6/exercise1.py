a_word = "hello!"

f = None
try:
    f = open('2023-11-09 - Week 66\\exo1.txt','w')
except:
    raise FileNotFoundError("File not found!")
else:
    f.write(a_word)
finally:
    if f is not None:
        f.close()
    print("ended")