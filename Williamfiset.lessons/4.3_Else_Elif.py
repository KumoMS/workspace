# Else and elif operators
import sys 
#Name is Kuro so all following if and elifs will print the else statements
#If I change Kuro to Meli, Skylar, Kumo or Shodan it will return the name to me

#when i add
print("please enter name: ")
name = str(input())
if name == "Meli":
    print("Name is Meli")
    sys.exit()
else:
    print("Name was not Meli")
#Elif puts all the if statements together
if name == "Skylar":
    print("Name is Skylar")
elif name == "Kumo":
    print("name is Kumo".capitalize())
elif name == "Shodan":
    print("Shodan")
else:
    print("not Skylar, not Kumo, and not Shodan")
#without the elif these if statements become independant
if name == "Skylar":
    print("Name is Skylar")
if name == "Kumo":
    print("Name is Kumo")
if name == "Shodan":
    print("Name is Shodan")
    sys.exit()
#using numbers - changing the number according to the if and elif statements will return the respected statement
n = 70
if n < 20:
    print("n < 20")
elif n < 40:
    print("n < 40")
elif n < 60:
    print("n < 60")
elif n > 60:
    print("n > 60")