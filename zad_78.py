'''

i = 0
imax = 10

while i <= imax :
    print(i,'I like PYTHON')
    i+=2
else :
    print("Now i =",i)
'''
'''
1. Tym razem pracujesz w LOT i masz za zadanie rozpocząć programowanie rozkładu miejsc w samolocie. (Patrz https://www.lot.com/pl/pl/boeing-737-800-rozklad-miejsc lub ilustracja na końcu tego laboratorium)

Należy wyświetlić napisy:

Row number 1

Row number 2

...

Row number 30

Row number 31

W tym celu:

zadeklaruj zmienną firstRow i przypisz jej wartość 1

zadeklaruj zmienną lastRow i przypisz jej wartość  31

zadeklaruj zmienną currentRow i przypisz jej wartość  firstRow

Dopóki currentRow jest mniejsze równe lastRow:

wyświetlaj napis "Row number...."

po wyświetleniu napisu zwiększaj currentRow o 1
'''

'''
firstRow = 1
lastRow = 31
currentRow = firstRow

while currentRow <= lastRow :
    print("Row number",currentRow)
    currentRow+=1
'''

# 2. Śni Ci się koszmar. Twój nauczyciel matematyki kazał Ci wypisać liczby od 1 do 13 i dla każdej liczby wyliczyć jej kwadrat i sześcian. Ponieważ nauczyciel nie zabronił używać Pythona, napisz pętlę, która dla liczb od 1 do 13 wyświetli kwadrat i sześcian tej liczby

i=1
imax=13
while i <= imax :
  
    print(i," kwadrat =",i**2," sześcian =",i**3)
    i+=1
else :
    print('koniec')

print('---------------')
n=0
nmax = 16
while n <= nmax:
    print('2^'+str(n),'=',2**n)
    n+=1

print('--------------')
i=1
imax=10
while i <= imax :
    print(i*"x",(11-i)*" ",(11-i)*" ",i*"x",20*"x",i*"x")
    i+=1

while i >= 1 :
    print(i*"x",(11-i)*" ",(11-i)*" ",i*"x",20*"x",i*"x")
    i-=1


