def convertstonespounds():
    stones = int(input("Enter number of stones > "))
    pounds = int(input("Enter number of pounds > "))
    totalpounds = (stones*14) + pounds
    totalkilos = totalpounds * 0.453592
    print(totalkilos,"kilograms")

def convertmilesyards():
    miles = int(input("Enter number of miles > "))
    yards = int(input("Enter number of yards > "))
    totalyards = (miles*1760) + yards
    totalkm = totalyards * 0.0009144
    print(totalkm,"kilometres")


print("ENTER '1' for converting stones and pounds to kilograms, enter '2' for converting miles and yards to kilometres")
if (input("Enter a selection > ") == "1"):
    convertstonespounds()
else:
    convertmilesyards()    



