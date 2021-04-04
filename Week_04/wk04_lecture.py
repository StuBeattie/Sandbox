"""Do this now:
Write a function to get a valid age from a user
Write two lines of main code to show its use.
"""


def main():
    users_age = get_valid_age()
    print(f'you are {users_age} years old!')


def get_valid_age():
    users_age = int(input("Age: "))
    while users_age < 0 or users_age > 100:
        print("Invalid age!")
        users_age = int(input("Age: "))
    return users_age


main()
