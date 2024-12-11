numbers = [1, 2, 3, 4]
names = ["Peter" , "Tim", "Mike", "Tom", "Mike"]

names.append("Tom")
names.insert(1, "Carsten")
names.remove("Tom")
print(names)
names.extend(numbers)
names.reverse()
print(names)

print("pop:", names.pop())
print("Tom idx:", names.index("Tom"))
print("Mike count:", names.count("Mike"))
