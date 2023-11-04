banana_price = 3.00
postage = 4.99
order_quantity = int(input("How many kilos of bananas are you ordering? > "))
base_price = banana_price * order_quantity
if (base_price > 50.00):
    postage = 3.49
order_price = base_price + postage
print("The cost of this order is £",order_price)