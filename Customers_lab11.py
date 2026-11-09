print("---Exercise 1---")
customer = {
    "name": "Alice",
    "Name": "Not-Alice",
    "email": "alice@example.com",
    "tier" : "gold",
    "ytd_spend": 12400,
}

print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])

print("---Exercise 2---")
customer["phone"] = '555-5555'
print(customer)
customer['tier'] = 'platinum'
del customer ['Name']
print (customer)

print(customer.get('ytd_spend', 0))

print("---Exercise 3---")
print(customer.get("email", "no email on file "))

for key, value in customer.items():
    print(f"{key}: {value}")

for something in customer:
    print(something, customer [something])

print("---Exercise 4---")
for key, value in customer.items():
    print(f"{key}: {value}")

for key in customer:
    print(key, customer[key])

print("---Exercise 5---")
tier_discounts = {
    "bronze": 0,
    "silver": .05,
    "gold": .10,
    "platinum": .15
}

discount = tier_discounts.get(customer["tier"], 0)

print = 200
final_price = price - (price * discount)

print("Tier:", customer["tier"])
print("Discount:", discount * 100, "%")
print("Final price:", final_price)

print("---Exercise 6---")
customers = [
    {"name": "Alice", "tier": "platinum"},
    {"name": "Bob", "tier": "silver"},
    {"name": "Charlie", "tier": "gold"},
]

for person in customers:
    discount = tier_discounts.get(person["tier"], 0)
    discount_amount = 300 * discount

    print(person["name"], person["tier"], discount_amount)

print("---Exercise 7---")

catalog = {
    "Widget A": {"price": 9.99, "stock": 150},
    "Gadget C": {"price": 49.99, "stock": 8}
}

for product in catalog:
    if catalog[product]["stock"] < 20:
        print("LOW STOCK:", product)

print("---Exercise 8---")
transactions = [
    {"region": "south", "amount": 300},
    {"region": "North", "amount": 150},
    {"region": "south", "amount": 200},
]

sales_summary = {}

for transaction in transactions:
    region = transaction["region"]
    amount = transaction["amount"]

    sales_summary[region] = sales_summary.get(region, 0) + amount

for region in sorted(sales_summary):
    print(region, sales_summary[region])

    # Reflection Questions:# Reflection 1:
# I would use .get() when a key might be missing because it allows the
# program to return a default value instead of causing an error. I would
# use bracket notation when I know the key exists and need its exact value.
# My rule of thumb is to use .get() for optional information and brackets
# for information that should always be there.

# Reflection 2:
# This pattern reminds me of using SUMIF in Excel because it adds up values
# based on categories, such as sales from different regions. Python can be
# more useful for large datasets because it can automatically process many
# records using loops without having to manually create formulas for each
# category. It also makes it easier to update and reuse the analysis.