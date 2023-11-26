# introduction to standard types
# ints, floats, doubles, and strings

#this is a string
string = "Hello World"
print(string)
print("")

#this is an integer - a whole number
integer = 123
# integer = -5
# integer = 1231414515
print(integer)
print(type(integer))
#this tells me the class of type
print("")

# this is a float
real_num = 3.1415
print(real_num)
print(type(real_num))
print("")

#float numbers are restricted to a certain number of bytes
#so if i type 3.1111111111111111111111111111 on a certain number of decimales will be returned
#this is a double type?
rl_num = 3.11111111111111111111111111111111111111111111111
print(rl_num)
print(type(rl_num))
(print(""))

# next, how do I convert between types
a = 3.4
b = 3.9
print("This is a variable -", int(a))
# a is converted from a float to an integer
print("This is b variable -", int(b), ". Take note it is casted down from 3.9 to 3")
# b is also converted to a float, but take note it gets rounded DOWN from 3.9 to 3 - this is called casting
print("")

# I can also do the reverse and convert an integer to a float
c = 3
print(float(c))
