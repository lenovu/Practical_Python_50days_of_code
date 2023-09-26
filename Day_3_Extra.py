
names = ["kerry", "dickson", "John", "Mary", "carol", "Rose", "adam"]
names.sort(reverse=True)
names_sorted = []

for char in names:
    if char.islower():
        names_sorted.append(char)

MyTuple = tuple(names_sorted)
print(MyTuple)