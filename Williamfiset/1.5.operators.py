# Basic arithmetic operators -, +, *, **, /, //, %

# simple addition
print(2+4)
#subtraction
print(3-5)
# subtract of a minus number - 2 minus -5 turns into 2 + 5 making the answer 7(I really have forgotten my maths)
print(2--5)
# multiplication
print(3*8)
# Power multiplier
print(2**4)
# division giving a decimal
print(7 / 3)
# here even with the 7.0 we get the float
print(7.0 / 3)
# force integer division
print (7 // 3)

# below I make code to print 7 / 3 but format it to 1 decimal
# the "1f" means float AKA decimal.
sum = 7 / 3
print("{one_dec:.1f}".format(one_dec=sum))