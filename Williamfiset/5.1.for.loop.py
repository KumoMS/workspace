#! 5.1.for.loop.py
# 'in' Keyword, for loop with list and for loop using indexing

s = "hello world"
a = [4, 6 , 9]
#this is a conditional check, 5 is not in a and therefore the program comes back with False
print( 5 in a )
# 4 is in a and therefore comes back with True
print( 4 in a )
# we can also do this with the string, the sub string 'ello' is in 'hello world' so we get True
print( "ello" in s )

#this is an example of a for loop using the in keyword for the list
for even_number in [2, 4, 6, 8, 10]:
    print(even_number)
    # add more code here..

odds = [1, 3, 5, 7, 9, 11]
for odd_numbers in odds:
    print(odd_numbers)

#indexing with range statement
print(range(len(odds)))
for index in range(len(odds)):
    print("Index: {:d}, odd number: {:d}".format(index, odds[index]))