def rodCutting(prices, length):
    if 0 > length:
        raise ValueError("Length is a negative integer")

    if length == 0:
        return 0
    
    for key, value in prices.items():
        if (key < 0):
            raise ValueError("Key is a negative integer")
        if (value < 0):
            raise ValueError("Value is a negative integer")
        
    q = 0
    for i in range(0, length + 1):
        if (i in prices.keys()):
            q = max(q, prices[i] + rodCutting(prices, length - i, cuts))
    

    return q



prices = {2:5, 3:8, 6:16}
print(rodCutting(prices, 9))