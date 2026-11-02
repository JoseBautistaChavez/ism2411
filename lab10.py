print("---Exercise 1: ---")
inventory = ["pen", "notebook", "stapler", "tape", "marker"]
print(inventory)
print(len(inventory))

print("---Exercise 2: Indexing---")
print(inventory[0]) # grabs the first item
print(inventory[-1]) # grabs the last item
middle = len(inventory) // 2
print(inventory[middle]) # grabs the middle item

print("---Exercise 3: List Slicing---")
print(inventory[:3])  # first three items
print(inventory[-2:]) # grab last two items
print(inventory[::2])

print("---Exercise 4: List Methods---")
inventory.append("envelope")
print(inventory)
inventory.remove("tape")
print(inventory)
inventory.sort()
print(inventory)

print("---Exercise 5: Tuple Comparison---")
coords = (40.7128, -74.0060)
try:
    coords[0] = 99
except TypeError as error:
    print(f"TypeError caught: {error}")
    print("Tuples protect coordinates from being changed by accident")
    
print("---Exercise 6: List Average Sales---")
sales = [100, 250, 75, 480, 200]
total = sum(sales)
count = len(sales)
average = total / count
print(f"Total sales: {total}")
print(f"Number of sales: {count}")
print(f"Average sales: {average}")
print(f"Best sale: {max(sales)}")
print(f"Worst sale: {min(sales)}")

best = sales[0]
worst = sales[0]
for amount in sales:
    if amount > best:
        best = amount
    if amount < worst:
        worst = amount
print(f"Best sale (loop): {best}")
print(f"Worst sale (loop): {worst}")

print("---Exercise 7: Accumulator Pattern---")
prices = [9.99, 14.99, 4.99, 24.99, 1.99]
discounted = []
for price in prices:
    discounted.append(round(price * 0.9, 2))
print(prices)
print(discounted)

print("---Exercise 8: Filter---")
sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]
high_sales = []
for amount in sales:
    if amount > 300:
        high_sales.append(amount)
print(high_sales)
print(f"Count: {len(high_sales)}")
print(f"Average: {sum(high_sales) / len(high_sales):.2f}")