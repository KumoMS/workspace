#temperatures lesson 4.2

tmp = '''
[-inf , -30] REALLY COLD!
[-30 , 0]  Cold
[0]        Zero
[0, 20]    Perfect
[20, 40]   Hot
[40, inf]  REALLY HOT!'''
print(tmp)
#this doesn't work with """ for some reason but works fine with '''

t = int(input("Please enter temperature: "))

if (t <= -30):
    print("REALLY COLD!")
if (t < 0):
    if (t > -30):
        print("Cold")
if (t == 0):
    print("Zero")
if (t > 0):
    if (t < 20):
        print("Perfect")
if (t >=20):
    if (t < 40):
        print("Hot")
if (t >= 40):
    print("REALLY HOT!")