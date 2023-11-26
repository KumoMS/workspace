code_name = str(input("Please enter code name: ".upper()))

code_name = code_name.upper()


welcome = "Welcome to the {ParaName} Database: ".format(
ParaName = "Nexara"
	)

print(welcome.upper().strip(), code_name.strip())
passcode = str(input("Please enter Passcode: ".upper()))

print("Incorrect credentials entered.".upper()) 
print("System has been compromised. ".upper())
print("A system warning has been sent to Supreme Commander Kuro".upper())

'''astr = welcome
astr = astr.replace("Nexara", "Archangel")
print(astr.upper())'''

#After code_name is entered it will ask for the passcode related to the code_name

#Here make it so if, for example,
#The code name shodan was entered it would enter the Archangel database