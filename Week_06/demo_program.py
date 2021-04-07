"""This would have been good to have seen before doing the assignment."""


# make CSV from list of lists
# with open("products.csv", "w") as output_file:
#    for product in products:
#        sale_status = "y" if product[2] else "n"
#        print("{},{},{}".format(product[0], product[1], sale_status)

PRODUCTS_FILE = "products.csv"
MENU_STRING = ">>>"

def main():
    print(MENU_STRING)
    choice = input(">".upper())
    while choice != "Q":
        if choice == "L":
            print("list")
        elif choice == "S":
            print("swap")
        else:
            print("invalid")
        print(MENU_STRING)
        choice = input(">").upper()
    print("Finished")


main()
