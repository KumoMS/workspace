names = ["Kumo", "Kuro", "Sonia", "Meli", "Skylar", "Shodan", "Hawke", "Apoc", "Toad", "Ufo"]

name_requested = input("Please enter your codename: ")

for name in names:
    if name.lower() == name_requested.lower():
        print("Welcome to Nexara Database " + name)
        exit()
print("Sorry the codename " + name_requested + " is not a part of our Database")
