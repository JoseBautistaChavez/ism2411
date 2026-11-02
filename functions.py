# Self-Assessment Questions
# 1. The first bug I spotted was the IndexError, as I ran the code and noticed the red squiggly line placed
#    to indicate where a colon should've been. I found it after running the print statement in the terminal.
#    When debugging, it's important to look through each line of code since the actual first error may
#    not be as obvious to find.
# 2. The function takes a price (float) and rate (string) and calculates the appropriate discount rate using
#    those inputs, resulting in a final price. A colleague can understand it since the inputs are labeled.
# 3. While I was able to find the errors of broken_sales.py myself, I used AI to look up other scenarios in
#    which those errors would appear so that I can build my understanding.

# --- Exercise 1 ---
def calculate_tax(price, rate): 
    return price * rate
tax1 = calculate_tax(100, 0.07)
tax2 = calculate_tax(250, 0.08)
print(f"Tax on $100 at 7%: ${tax1:.2f}")
print(f"Tax on $250 at 8%: ${tax2:.2f}")

# --- Exercise 2 ---
def apply_discount(price, tier):
    if tier == "gold":
        return price * 0.85
    elif tier == "silver":
        return price * 0.90
    elif tier == "bronze":
        return price * 0.95
    else:
        return price
original_price = 200
for tier in ["gold", "silver", "bronze", "none"]:
    print(f"{tier}: ${apply_discount(original_price, tier):.2f}")

# --- Exercise 3 ---
def final_price(price, tax_rate, discount_tier):
    discounted_price = apply_discount(price, discount_tier)
    tax = calculate_tax(discounted_price, tax_rate)
    return discounted_price + tax
print(f"After gold discount: ${apply_discount(200, 'gold'):.2f}")
print(f"After tax: ${final_price(200, 0.07, 'gold'):.2f}")
print(f"final_price(200, 0.07, 'gold') = ${final_price(200, 0.07, 'gold'):.2f}")

# --- Exercise 4 ---
orders = [(200, "gold"), (150, "silver"), (80, "bronze"), (500, "none")]
rate = 0.07
for price, tier in orders:
    total = final_price(price, rate, tier)
    print(f"Price: ${price} | Tier: {tier} | Final: ${total:.2f}")

# --- Exercise 5 ---
# broken_sales.py

# --- Exercise 6 ---
x = 100   # global variable

def double_it():
    x = 999   # local variable — different from global x!
    return x * 2

print(x)           # what prints here? 100
print(double_it()) # what prints here? 1998
print(x)           # has x changed? No, it remains as 100. Local variables that run inside a function
                   # are different than global variables, so they remain unaffected.