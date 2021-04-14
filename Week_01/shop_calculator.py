"""Shop calculator"""

TOTAL = 0

number_of_items = int(input("Number of items: "))
while number_of_items <= 0:
    print("Invalid number of items.")
    number_of_items = int(input("Number of items: "))

for number in range(number_of_items):
    price = float(input("Price of item: "))
    TOTAL += price
print("Total price for {} items is ${:.2f}".format(number_of_items, TOTAL))
