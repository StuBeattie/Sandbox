"""loop through list"""

# numbers = [1, 2, 8, -3, 12, 50, 0]

# for number in numbers:
# print('checking...')
# if number < 0:
# print('yes!')
# break  # if you dont use the break statement the for loop will keep iterating the the list until completed.
from typing import List


def main():
    """Using a function"""
    numbers = [1, 2, 8, 3, 12, 50, 0]
    print(is_negative_here(numbers))


def is_negative_here(numbers):
    for number in numbers:
        print('checking...')
        if number >= 0:
            continue
        return True
    return False


main()
