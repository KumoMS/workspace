XO = "{XO} C'est la vie".format(
	XO = "XO!!!".upper()
	)

print(XO.upper())

amor_fati = XO
astr = amor_fati.replace("C'est la vie", "amor fati")

first_name = str(input("Please enter your first name: "))
last_name = str(input("Please enter your last name: "))

first_name = first_name.capitalize()
last_name = last_name.capitalize()

name_format = "{first} {last}"
print("Welcome", name_format.format(first=first_name, last=last_name),
	"to the XO servers.")

State_of_business = str(input("Please state your business: "))

print("I am sorry, I cannot help you with that.")
print("If you have any more enquiries please contact CEO Kuro via her email: Kuro.Kaede@XO.com")
print(astr.upper())
