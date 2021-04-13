"""
0. Pattern-based programming
1. Name based on the problem domain
2. Function at the same level of abstraction (main should "loop")

Menu-driven product program
load products
- L_ist products
- S_wap sale status (get product number with error checking)
- Q_uit (save file)
"""

# make CSV from list of lists
# with open("products.csv", "w") as output_file:
#    for product in products:
#        sale_status = "y" if product[2] else "n"
#        print("{},{},{}".format(product[0], product[1], sale_status)

PRODUCTS_FILE = "products.csv"
MENU_STRING = ">>>"


def main():
    """Sales program."""
    products = load_products()
    print(products)
    print(MENU_STRING)
    choice = input(">".upper())
    while choice != "Q":
        if choice == "L":
            list_products(products)
        elif choice == "S":
            swap_sale_status(products)
        else:
            print("invalid")
        print(MENU_STRING)
        choice = input(">").upper()
    save_products(products)
    print("Finished")


def load_products():
    """Load product information."""
    print("loading")
    products = [["phone", 340, False], ["PC", 1420.95, True], ["Plant", 24.5, True]]
    return products


def list_products(products):
    """List all products."""
    print("list")
    for product in products:
        print(product)


def swap_sale_status(products):
    """Change sales states on items chosen by user."""
    list_products(products)
    is_valid_input = False
    while not is_valid_input:
        try:
            number = int(input("? "))
            if number < 0:
                print("Product must be >= 0")
            else:
                is_valid_input = True
        except ValueError:
            print("Invalid (not an integer)")
    print(products[number])


def save_products(products):
    """Save updated products list to file."""
    pass


main()
