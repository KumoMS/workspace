# 2.3 advanced string manipulations

prefix = "python is an "
suffix = "awesome language"
# we want to combine these two strings, or "glue" them together

astr = prefix + suffix
print(astr)

# now I want to change the suffix to something else

#below we change the word language with the word snake
astr = astr.replace("language", "snake")
print(astr)

astr = astr * 2
# this prints it two times
# and then the , 1 below makes it only do the .replace function once out of the 2 prints
astr = astr.replace("snake", "language", 1)
print(astr)

#this lets us count how many times something shows up in the string
print(astr.count("an"))