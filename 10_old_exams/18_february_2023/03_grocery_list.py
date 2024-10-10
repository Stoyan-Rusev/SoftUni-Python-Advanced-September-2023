def shop_from_grocery_list(budget, grocery_list, *product_and_price):
    for current_product, current_price in product_and_price:
        if current_product not in grocery_list:
            continue
        if budget < current_price:
            break
        grocery_list.remove(current_product)
        budget -= current_price
    if not grocery_list:
        return f'Shopping is successful. Remaining budget: {budget:.2f}.'
    return f"You did not buy all the products. Missing products: {', '.join(grocery_list)}."


print(shop_from_grocery_list(
    100,
    ["tomato", "cola"],
    ("cola", 5.8),
    ("tomato", 10.0),
    ("tomato", 20.45),
))
print()
print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat"],
    ("cola", 5.8),
    ("tomato", 10.0),
    ("meat", 22),
))
print()
print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat", "chocolate"],
    ("cola", 15.8),
    ("chocolate", 30),
    ("tomato", 15.85),
    ("chips", 50),
    ("meat", 22.99),
))
