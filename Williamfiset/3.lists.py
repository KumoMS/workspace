#lessons 3-5, recreate something from before using what I learnt in these lessons

numbers = [2.134, -10, 8, 16**3, -19, 1]
names = ["Kumo", "Hawke", "Apoc", "Shodan"]
names2 = ["Kuro", "Meli", "Skylar", "Zoe", "Laure"]
print(numbers)
print(names)
del (names[3])
print(names)
print(names[0], names[2])

Nexara = "Welcome to Nexara."
print(Nexara[0], Nexara[11])

alpha = ["a", "b", "c", "d"]
alpha.append("e")
alpha = alpha + ["f"]
print(alpha)

d_index = alpha.index("d")
print("d_index: " + str(d_index))
del alpha[d_index]
print(alpha)

alpha.remove("c")
print(alpha)

names.insert(2, "Sonia")
names.sort()

namelist = names + names2
namelist.sort()
namelist = ', '.join(namelist)

print(namelist)

#add this stuff to the nexara database program

print(min(numbers))
print(max(numbers))
print(sum(numbers))
print(len(numbers))

print(max(names2))
print(len(names))