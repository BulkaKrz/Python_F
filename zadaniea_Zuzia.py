import random

a=1
b=1
text=[]

for a in range(2,10):
    for b in range(2,10):
        c=a*b
        if c<=99:
            #text = text+('%d * %d = .......\t' % (a,b))

            text.append('%-2d * %-2d = _______' % (a,b))
#tworzenie listy losowej

random.shuffle(text)

for i in range(0,30):
    print('%d.\t' % (i+1),text[i])
