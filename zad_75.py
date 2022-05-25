'''
itRains = True

if itRains:
    print('we stay at home')
else :
    print('we go out')
    
print('-------------------')

print('we stay at home' if itRains else 'we go out')

'''
'''
Tym razem pomożemy lekarzom przeprowadzając wstępną analizę: czy pacjent ma grypę, czy tylko przeziębienie (zakładamy, że pacjentowi coś dolega, w tym zadaniu mamy tylko pomóc zdiagnozować czy to jest grypa czy przeziębienie):
'''

musclePain = False
fever = True
weakness = False
isMan = False
if (musclePain and fever and weakness) :
    print('suspicion of influenza')
else:
    print('The flu is unlikely')
print('----------------')

if musclePain and fever and weakness or ( (musclePain or fever or weakness) and isMan):
    print('suspicion of influenza')
elif weakness and not (fever or musclePain):
    print('Just take a rest!')
else :
    print('you may be cold')

print('--------------')


sCheckCompleted = False
print("CHECK IS COMPLETED" if sCheckCompleted else "CHECK NOT DONE YET!")
