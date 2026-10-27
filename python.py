import json

with open("products.json", "r") as file:
    products = json.load(file)

total_value_all = 0

for item in products:
    name = item["Products"]
    total_price = item["Quantity"] * item["Price"]
    total_value_all += total_price
    print(f"{name}: {total_price}")

print(f"\nTotal Value of All Products:{total_value_all}")