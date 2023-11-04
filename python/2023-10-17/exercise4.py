def caesar_encrypt(text, shift):
    newString = ""
    for i in range(len(text)): 
        newString += alphabet[(alphabet.index(text[i].lower()) + shift) % 26]
    return newString

def caesar_decrypt(encrypted_text, shift):
    newString = ""
    for i in range(len(encrypted_text)):
        if (encrypted_text[i].isalpha()):
            index = (alphabet.index(encrypted_text[i].lower()) - shift)
            if index < 0:
                index = 26 + index
            newString += alphabet[index]
        else:
            newString += encrypted_text[i]
    return newString

alphabet = "abcdefghijklmnopqrstuvwxyz"
shift = 3

print(caesar_encrypt(input("Enter a string to shift with caesar cipher > "), shift))
print(caesar_decrypt(input("Enter a string to decrypt with caesar cipher > "), shift))

cracktext = input()
shift = 0

for i in range(26):
    shift+=1
    print(caesar_decrypt(cracktext, shift)) # iterate through the alphabet

# the good news about computers is that they do what you tell them to do.
# the bad news is that they do what you tell them to do.