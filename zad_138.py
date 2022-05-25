colors = ['Hearts','Diamonds','Clubs','Spades']
figures = [
    {'Figure':'Ace',  'Power':14},
    {'Figure':'King', 'Power':13},
    {'Figure':'Queen','Power':12},
    {'Figure':'Jack', 'Power':11},
    {'Figure':'10',   'Power':10},
    {'Figure':'9',    'Power':9}]

allCards = []
allColor = []
for color in colors:
    for figure in figures:
        aCard=figure.copy()
        aCard['Color']=color
        allCards.append(aCard)
    

import random
random.shuffle(allCards)
#for i in range(0,len(allCards)):
#    print(i,allCards[i])

player1 = allCards[:12]
player2 = allCards[12:]

print('-------PLAYER 1--------')
print(player1)
 
print('-------PLAYER 2--------')
print(player2)    

p1 = len(player1)
p2 = len(player2)

while p1>0 and p2>0:
    card1=player1.pop(0)
    card2=player2.pop(0)
    S1=card1['Power']
    S2=card2['Power']
    if S1 == S2:
        player1.append(card1)
        player2.append(card2)
        print(S1,' - ',S2,' remis')
    elif S1 > S2:
        player1.append(card1)
        player1.append(card2)
        print(S1,' > ',S2,' zbiera Player 1')
    else:
        player2.append(card1)
        player2.append(card2)
        print(S1,' < ',S2,' zbiera Player 2')
      
    p1 = len(player1)
    p2 = len(player2)
    print('Player_1 %s kart Player_2 %s kart' %(p1,p2))
print('KONIEC')
if p1 > 0:
    print('wygrywa Player 1')
else:
    print('wygrywa Player 2')
