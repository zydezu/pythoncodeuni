age = int(input("Please enter your age > "))
heartrate = int(input("Please enter your heartrate > "))
maximum_heartrate = 208 - (0.7 * age)

if heartrate >= 0.9 * maximum_heartrate:
    result = "Interval training"
elif 0.7 * maximum_heartrate <= heartrate < 0.9 * maximum_heartrate:
    result = "Threshold training"
elif 0.5 * maximum_heartrate <= heartrate < 0.7 * maximum_heartrate:
    result = "Aerobic training"
elif heartrate < 0.5 * maximum_heartrate:
    result = "Couch potato"



print(result)
