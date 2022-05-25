'''
import random
myNumbers =[]
while len(myNumbers) < 7:
    newNumber=random.randint(1,49)
    if newNumber in myNumbers:
        print(newNumber)
        continue
    myNumbers.append(newNumber)
print(myNumbers)
'''

colors = ['Hearts','Diamonds','Clubs','Spades']
figures = ['Ace','King','Queen','Jack','10','9']
allCards = []

for color in colors:
    for figure in figures:
        allCards.append("%s - %s" % (color,figure))
print(allCards)

import random
random.shuffle(allCards)
print('----------------')
print(allCards)

player1=[]
player2=[]

max=len(allCards)
for i in range(0,max-1):
    if i % 2 ==0:
        player1.append(allCards[i])
        
    else:
        player2.append(allCards[i])
        
    
print('----------------------')
print('Player 1 :',player1)
print('----------------------')
print('Player 2 :',player2)
print('----------------------')
print('Player A :',allCards[0:12])
print('----------------------')
print('Player B :',allCards[12:max])

