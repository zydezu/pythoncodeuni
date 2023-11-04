def caesar(string, shift):
    newString = ""
    for i in range(len(string)): 
        newString += alphabet[(alphabet.index(string[i].lower()) + shift) % 26] # worst code ever
    print(newString)

def decrypt(string, shift):
    newString = ""
    for i in range(len(string)): 
        index = (alphabet.index(string[i].lower()) - shift)
        if index < 0:
            index = 26 + index
        newString += alphabet[index] # worst code ever
    print(newString)

alphabet = "abcdefghijklmnopqrstuvwxyz"
shift = 3

caesar(input("Enter a string to shift with caesar cipher > "), shift)
decrypt(input("Enter a string to decrypt with caesar cipher > "), shift)
