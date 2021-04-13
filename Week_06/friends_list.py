"""Display list of friends details"""

from Week_06.friends import FriendsInformation


def main():
    """Get users friends details and display them in a sorted list."""

    friends = []

    first_name = input("Friends first name: ")
    while first_name != "":
        last_name = input("Friends last name: ")
        age = int(input("Friends age: "))
        add_input_to_friends = FriendsInformation(first_name, last_name, age)
        friends.append(add_input_to_friends)
        first_name = input("Friends first name: ")
    print()

    # Display friends details in a list
    friends.sort()
    for friend in friends:
        print("{}".format(friend))


main()
