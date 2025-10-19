def total_price(cart_items):
    total=sum(cart_items.values())
    return total
cart_items = {'Laptop': 50000, 'Headphones': 2000, 'Mouse': 500, 'Keyboard': 1500}
res=total_price(cart_items)
print("Total Price: ",res)
