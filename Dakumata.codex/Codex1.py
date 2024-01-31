names = []
with open ('d:/A_workspace/Mypython/Dakumata.codex/names.txt','r') as file:
    for line in file:
        line = line.strip()
        names.append(line)

# print(names[0]) # This here shows Kuro is index 0 from the txt file
name_requested = input("Please enter your codename: ")

for name in names:
    if name.lower() == name_requested.lower():
        print("Welcome to Nexara Database " + name)
        exit()
print("Sorry the codename " + name_requested + " is not a part of our Database")

'''file = open("names.txt","a")
file.write(name_requested + "\n")
file.close()''' # this is the code to rewrite the names.txt file perminantly.