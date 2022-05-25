import random
'''
print(random.randint(1,100))
list = ["a","b","c","d","e","f","g"]
print(random.choice(list))
print(random.randrange(1,100))
print(list)
random.shuffle(list)
print(list)
print(random.random())

print('----------')  

i=1
imax = 10
list = []

while i <= imax :
    r = int(random.randint(1,100))
    print(r)
    i+=1
    list.append(r)
print(list)

print('----------')  

number1 = random.randint(1,100)
print("The first generated number is %d" %(number1))
counter = 1
number2 = random.randint(1,100)
while number1 != number2 :
    number2 = random.randint(1,100)
    print(counter,'\t',number2)
    counter+=1
print("I needed %d attempts to generate %d again" % (counter, number1))
 
print('----------')   
'''

countries = [
    'Uruguay',
    'Russia',
    'Saudi Arabia',
    'Egypt',
    'Spain',
    'Portugal',
    'Iran',
    'Morocco',
    'France',
    'Denmark',
    'Peru',
    'Australia',
    'Croatia',
    'Argentina',
    'Nigeria',
    'Iceland',
    'Brazil',
    'Switzerland',
    'Serbia',
    'Costa Rica',
    'Sweden',
    'Mexico',
    'Korea Republic',
    'Germany',
    'Belgium',
    'England',
    'Tunisia',
    'Panama',
    'Colombia',
    'Japan',
    'Senegal',
    'Poland'
    ]

print(countries)
print()
random.shuffle(countries)
print(countries)

groupNumber =0

for i in range(len(countries)):
    
    if i % 4 == 0:
        groupNumber+=1
        print("----Grupa %d----" % (groupNumber))

    print(countries[i])
   





