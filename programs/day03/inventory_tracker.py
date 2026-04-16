old_stock = {"Apple", "Mango", "Orange", "Banana"}
new_stock = {"Apple", "Grapes", "Pineapple", "Mango"}

total_inventory = old_stock | new_stock
out_of_stock = old_stock - new_stock

newly_added = new_stock - old_stock

print ("--- 🛒 Inventory Report ---")
print (f"total unique items: {total_inventory}")
print (f"Out of stock: {out_of_stock}")
print (f"newly Added: {newly_added}")

stock_levels = {"Apple" : 50, "Banana": 60, "mango" : 7}

print("\n--- 🚨 Low Stock Alerts ---")
for item, quantity in stock_levels.items():
    if quantity < 10:
        print(f"Low Stock Alert: {item} sirf {quantity} reh gaye hain! ⚠️")