#counter challenge number 2 is to count upward until user hits spacebar, then reset counter to 0
from msvcrt import getch
key = ord(getch())

c=-1


while c != -2:
    c=c+1
    print(c)