my_tuple = (1, 2, 3, 4, 2, 5, 6, 5)

repeated_items = set()
unique_items = set()

for item in my_tuple:
    if item in unique_items:
        repeated_items.add(item)
    else:
        unique_items.add(item)

print("Repeated items in tuple:", repeated_items)
