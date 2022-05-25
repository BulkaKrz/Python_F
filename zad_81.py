'''
values = [10,43,12,48,12,11,18,98,57,28,19,27,49,19,74]
i=0
max = len(values)-2
while i < max:
    print(i,values[i],values[i+1],values[i+2])
    if values[i]<values[i+1]<values[i+2] :
        print('\tFound: ',values[i],values[i+1],values[i+2])
    i+=1
print('-----------------')

numbers = [8, 18, 2, 4, 16, 5, 25, 4, 22, 3, 3, 5, 3, 9, 81, 11]
i=0
imax = len(numbers)-1

while i<imax :
    print(i,numbers[i],numbers[i+1])
    if numbers[i]*numbers[i] == numbers[i+1]:
        print('\tFound : ',numbers[i],numbers[i+1])
    i+=1

print('-----------------')

numbers = [8, 18, 2, 4, 16, 5, 25, 4, 22, 3, 3, 5, 3, 9, 81, 11]
i=0
imax = len(numbers)-2

while i<imax :
    print(i,"\t",numbers[i],numbers[i+1],numbers[i+2])
    if numbers[i]*numbers[i] == numbers[i+1] and numbers[i+1]*numbers[i+1] == numbers[i+2]:
        print('\tFound : ',numbers[i],numbers[i+1],numbers[i+2])
    i+=1
print('-----------------')

texts = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

n=0
nmax=len(texts)-1
while n<nmax :
    print(n,texts[n],len(texts[n]),texts[n+1],len(texts[n+1]))
    if len(texts[n]) == len(texts[n+1]):
        print('\tFound : ',texts[n],texts[n+1])
    n+=1

# skrypt pakowanie paczek
cargo = [40,20,4,5,30,8,2,7,3,19,32,40,20,35,15,32,9]
cargo.sort()
cargo.reverse()
print('The cargo list is :',cargo)

boxCapacity = 90
box = []
i = 0
while  i < len(cargo) and (boxCapacity - sum(box) >= min(cargo)) :
    if (boxCapacity - sum(box)) >= cargo[i]:
        box.append(cargo[i])
    i+=1

print("The colected items sum is:", sum(box))
print("The elements aer:",box)

print('-----------------')

number = 1
previousNumber = 0
while number <= 50 :
    print(previousNumber,'+',number,'=',previousNumber +number)
    previousNumber = number
    number+=1
'''

print('-----------------')

import random
my_number = random.randint(0,20)
guess = -1
trials = 1
print("Guess my number!")

while my_number != guess :
    print('Your try nmber',trials)
    guess = int(input())
    if my_number == guess:
        print("Congratulations!!! You are right! It was:",my_number,"You needed",trials,"trials.")
    elif  my_number < guess:
        print("Sorry- my number is smaller than your guess, Try again!")
    else :
        print("Sorry- my number is greater than your guess, Try again!")
    trials+=1
    









    
