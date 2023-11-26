#! 5.2.while.loop.py

index = 0
names = ["Josh", "Harry", "leah", "Micah"]

while index < len(names):

    name = names[index]
    print(name)
    index = index + 1

# 1 - 10
total = 0
v = 1
while v <= 10:
    total = total + v
    v = v + 1
print(total)

print("Please make sure a + b = 20")
while True:

    a, b = int(input("a: ")), int(input("b: "))
    if a + b == 20:
        print("stopping loop")
        break
    else:
        print("Please make sure a + b = 20")