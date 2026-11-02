# broken_sales.py - trace and diagnose before fixing anything.
sales = [120, 80, 250, 175, 90]

total = 0
for sale in sales:
    total += sale # Was set equal to sale, so it only used the last value instead of adding them up ; hidden error
print(f"Total: ${total}")

count = 0
for sale in sales: # Was missing colon for indentation; SyntaxError
    count += 1
print(f"Count: {count}")

i = 0
while i < len(sales): # Equal sign not needed since 5 is not included in the index ; IndexError
    print(sales[i])
    i += 1

# At first, the terminal helped with identifying bugs like SyntaxError and IndexError, and AI was able to
# provide multiple solutions to them by listing scenarios where one could be applicable to this code.
# However, the "error" with the total outputting the wrong value would have went unnoticed if I haven't looked
# at the code myself, so it's important to still double check your code when using these tools as a resource.