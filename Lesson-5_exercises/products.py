# Products
product_1 = "Wireless Mouse"
product_2 = "Gaming Keyboard"
product_3 = "USB-C Adapter"

# Prices
price_1 = "$25"
price_2 = "$8"
price_3 = "$10"

# Availability 
in_stock_1 = True
in_stock_2 = False
in_stock_3 = True

cart_summary = "Your cart items: \n"
cart_summary += "-" + product_1 + ":" + price_1 + ( "(In stock)" if in_stock_1 else "(Out of stock)") + "\n"
cart_summary += "-" + product_2 + ":" + price_2 + ( "(In stock)" if in_stock_2 else "(Out of stock)") + "\n"
cart_summary += "-" + product_3 + ":" + price_3 + ( "(In stock)" if in_stock_3 else "(Out of stock)") + "\n"

print(cart_summary)

