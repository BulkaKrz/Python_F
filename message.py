
helloMessage="Hello %s!"
print(helloMessage % ('Kate'))
print(helloMessage % ('Chris'))

helloMessage2="Hello {0:s}!"
print(helloMessage2.format('Kate'))

helloMessage3="%s has %d %s"
print(helloMessage3 % ('Kate',1,'animal'))
print(helloMessage3 % ('Chris',10000,'$'))

helloMessage4="{0:s} has {1:d} {2:s}"
print(helloMessage4.format('Kate',1,'animal'))
print(helloMessage4.format('Chriss',10000,'$'))

line="%20s cost %6d €"
print(line % ('ICE CREAM',3))
print(line % ('TRIP TO VENICE',119))
print(line % ('PIZZA HAVAI',6))
print()
line="%-20s cost %6d €"
print(line % ('ICE CREAM',3))
print(line % ('TRIP TO VENICE',119))
print(line % ('PIZZA HAVAI',6))
print()
line2='{0:20s} cost {1:6d} €'
print(line2.format('ICE CREAM',3))
print(line2.format('TRIP TO VENICE',119))
print(line2.format('PIZZA HAVAI',6))
print()
line3='{0:1s}  {1:1d}'
print(line3.format('ICE CREAM',3))
print(line3.format('TRIP TO VENICE',119))
print(line3.format('PIZZA HAVAI',6))
