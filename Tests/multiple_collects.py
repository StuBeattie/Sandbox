"""Multiple collects"""

name = "Bobby McAardvark"

count = 0
for letter in name:
    if letter.lower() in "aeiou":
        count += 1
# print("Out of {} letters, {} has {} vowels".format(len(name), name, count))

capitals = [c for c in name if c.isupper()]
vowels = [c for c in name if c.lower() in "aeiou"]
new_name = "".join([c for c in name if c.lower() not in "aeiou"])
print(new_name)

# print(capitals)
#print(vowels)
