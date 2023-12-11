# make this code line better so only enter key works! This is similar to the next challenge!
'''I = input("Please hit the Enter key")'''
#Below is tom's way using -1 instead of 0 because we do print after the increment 
c = -1
while c != 5:
    c = c+1
    print(c)
while c != 0:
    c = c-1
    print(c)
    #This way works better with the count 01234543210 vs the way below that is scuffed

# this is my way, printing before the increment allow the variable to be set as 0
# the way we want it printed
'''c2 = 0
while c2 != 6:
    print(c2)
    c2 = c2+1
while c2 != 0:
    print(c2)
    c2 = c2-1'''
# this is just scuffed though as it counts 5 twice going 012345543210 which is okay if we want that.
    

'''for num in range(6):
    print(num)'''
# this is the for loop
# it doesn't need a variable as python will fill it in.
# Here I am able to count up to 5 using range(6),
# but I am unsure how to count down to 0 again with this method

