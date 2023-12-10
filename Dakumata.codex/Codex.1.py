names = []
with open ('names.txt','r') as file:
    for line in file: #for some reason it doesnt find the file in the directory
        line = line.strip()
        names.append(line)

name_requested = input("Please enter your codename: ")

for name in names:
    if name.lower() == name_requested.lower():
        print("Welcome to Nexara Database " + name)
        exit()
print("Sorry the codename " + name_requested + " is not a part of our Database")
