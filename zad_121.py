
'''
import random 
ints = range(33,127)
password = ''

for i in range(16):
    password +=chr(random.choice(ints))

print('pasword is:',password)

import random
min = 1
max = 6

dice = random.randint(min,max)
print(dice)
if dice == 1:
    print("\n o \n")
elif dice == 2:
    print("  o\n   \no  ")
elif dice == 3:
    print("  o\n o \no  ")
elif dice == 4:
    print("o o\n   \no o")
elif dice == 5:
    print("o o\n o \no o")
else:
    print("o o\no o\no o")
print('----------------------')


import random
min = 1
max = 6
i=0
dices=[]
dice = random.randint(min,max)
while i<6:
    dice = random.randint(min,max)
    dices.append(dice)
    i+=1
print(dices)
dices.sort()
print(dices)
'''
import random

a=1
b=1
text=[]

for a in range(1,11):
    for b in range(1,11):
        c=a*b
        if c<=50:
            #text = text+('%d * %d = .......\t' % (a,b))
            text.append('%d * %d = .......' % (a,b))


random.shuffle(text)

for i in range(0,70):
    print(text[i])


#        if a*b<=50:
#            print(a,'*',b,'=',a*b)










