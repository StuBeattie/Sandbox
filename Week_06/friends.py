"""Friends class"""


class FriendsInformation:
    """Represent friends information gathered from the user."""

    def __init__(self, first_name="", last_name="", age=0):
        """Initialise friends instance."""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        """Display friends details gathered from user."""

        return "Name: {} {}, age: {}".format(self.first_name, self.last_name, self.age)

    def __lt__(self, other):
        """Less than< used for sorting friends by age."""

        return self.age < other.age
