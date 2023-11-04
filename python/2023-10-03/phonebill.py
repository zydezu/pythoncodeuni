def main():
    bill = 20.00
    freeSMS = 100
    freeminutes = 120
    
    SMSsent = int(input("Enter the number of SMS' sent > "))
    minutesused = int(input("Enter the number of minutes used > "))
    
    extraSMS = SMSsent - freeSMS
    extraminutes = minutesused - freeminutes
    if extraSMS < 0:
        extraSMS = 0
    if extraminutes < 0:
        extraminutes = 0
    
    bill = bill + extracharge(extraSMS, extraminutes)
    return bill

def extracharge(SMS, minutes):
    return 0.12 * SMS + 0.08 * minutes

print("Bill: $" + format(main(), ".2f"))