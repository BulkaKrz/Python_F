'''
persons=['Elizabeth','Steven','Sebastian','Margaret','Swetlana','Raphael']

domain = 'mycompany.com'

for person in  persons:
    email = person + "@" + domain
    print('Email for\t',person,'\tis\t',email)
else:
    print('---------- end of the list --------------')


data = ['Error:File cannot be open',
        'Error:No free space on disk',
        'Error:File missing',
        'Warning:Internet connection lost',
        'Error:Access denied']
for message in data:
    print(message.upper())
    elements = (message.split(':'))
    print(elements[0].upper(),elements[1])
print()
print()
for message in data:
    elements = (message.split(':'))
    if elements[0] == "Error":
        print(elements[1].upper())
    else:
        print(elements[1])

   
for number in range(1,21):
    if number %2 == 0:
        print('Number %2d is %s' % (number,'even'))
    else:
        print('Number %2d is %s' % (number,'odd'))
   # print(number)


 '''  

string_A = '+---+---+---+---+'
string_B = '|   |   |   |   |'

for plot in range(10):
    print(string_A)

print()
print()
for plot in range(9):
    if plot %2 == 0:
        print(string_A)
    else:
        print(string_B)


print()
print()
for plot in range(1,10):
    print("x"*plot)



print()
print()
for plot in range(1,10):
    if plot %2 == 0:
        print("x"*plot)
    else:
        print("o"*plot)








