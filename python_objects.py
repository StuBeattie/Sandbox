"""
All data in Python program is
 represented by objects(types == classes)."""

things = [1, 0.2, "hi", (1, "a"), {1: 4}]

# e.g of good string formatting.
for thing in things:
    print("{:>8} is: {}".format(repr(thing), type(thing)))
print("{} is: {}".format(repr(things), type(things)))
