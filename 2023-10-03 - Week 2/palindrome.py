stringtocheck = input("Enter a string to check if it is a palindrome > ").lower()
ignorepunctuation = [" ", ",", "!", "'"]
for i in range(len(ignorepunctuation)):
    stringtocheck = stringtocheck.replace(ignorepunctuation[i] ,"")

normallist = list(stringtocheck)
reversedlist = [0] * len(normallist) # generates empty array

j = len(normallist)
for i in range(len(normallist)):
    j = j-1
    reversedlist[j] = normallist[i]
    
print(reversedlist)

if(normallist==reversedlist):
    print("PALINDROME!")
else:
    print("No palindrome")