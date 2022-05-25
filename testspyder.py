# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#w tym zadaniu liczymy pole koła
WartoćPI=3.14
PromienOkregu=5
PoleKola=WartoćPI*PromienOkregu**2
print(PoleKola)

#zadanie na obwód koła
print('Liczymy Pole Koła')
r1=int(input('podaj promień koła: '))
ObwodOkregu=2*WartoćPI*r1
print('Obwód okręgu = ',round(ObwodOkregu,2))
print()
print()

#zadanie Pole Prostokąta
print('Liczymy pole prostokąta')
a1=int(input('podaj 1 bok prostąkąta: a = '))
b1=int(input('podaj 1 bok prostąkąta: b = '))
PoleProstokata=a1*b1
print()
print('Pole prostokąta = ',round(PoleProstokata,2))
print()
print()

# zadanie pole trapezu
print('Liczymy pole trapezu')
a2=int(input('podaj długoć podstawy: a= '))
b2=int(input('podaj długoć podstawy: b= '))
h2=int(input('podaj wysokoć trapezu: h= '))
STrapezu=((a2+b2)/2)*h2
print()
print('Pole trapezu  = ', round(STrapezu,2))
print('>>>>> Incorrect directory/file: {}'.format(exc_val)) 