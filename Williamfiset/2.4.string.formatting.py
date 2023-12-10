# 2.4 string formatting 

n = 11
f = 1.2345678
s = "computer"

#format specifications

print("my number is {:d}".format(n)) # this prints 11 normally as it is not a decimal
print("my number is {:b}".format(n)) # this prints our number in binary

# There are many format types such as:
# e - exponents
# b - binary (base 2)
# o - octal (base 8)
# d - decimal (base 10)
# x - hexadecimal (base 16)
# f - floats (decimal numbers)
# s - strings (defaul if none is specified)

print("{:f}".format(f))
#the .3 will make is only print the last 3 digits of my float number and round it
print("{:.3f}".format(f))

#now padding the 11 shows that i want it to print 11 characters
print("{:11.3f}".format(f))
#this pads it with 0s
print("{:011.3f}".format(f))

# this is the advance version of formatting my strings
print("{0} {1} {2}".format(n,f,s))

print("{name} own(s) {amount} of {object}".format(
    name = "marti",
    amount = 5,
    object = "cards"
))

#next look at implimenting user input with the above!