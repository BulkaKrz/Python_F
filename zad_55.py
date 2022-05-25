# q="THE EYES"
# print(q[0],q[1],q[2],q[5],q[3],q[7],q[4],q[6])
# q="a gentleman"
# print(q[3],q[6],q[7],q[2],q[0],q[4],q[5],q[1],q[8:])
# q="THE MORSE CODE"
# print(q[1:3],q[6],q[2],q[3],q[10:12],q[4],q[8],q[9],q[12],q[11],q[0],q[7])

#HERE COME DOTS
q = "THE MORSE CODE"
print(q[1:3],q[6],q[8],q[3],q[10:12],q[4],q[13],q[9],q[12],q[5],q[0],q[7])

print(q[1:3]+q[6]+q[8]+q[3]+q[10:12]+q[4]+q[13]+q[9]+q[12]+q[5]+q[0]+q[7])

print()

line="'Program \"Kropka nad i\" nadamy o: 22:00'"
time=(line[line.find(':')+2:line.find("'",2)])
print(line)
tmp =(line[line.find('\"'):])
title=(tmp[:tmp.find('\"',2)+1])
print(title,time)
print()
line="'Program \"Pytanie na śniadanie\" nadamy o: 6:00'"
time=(line[line.find(':')+2:line.find("'",2)])
print(line)
tmp =(line[line.find('\"'):])
title =(tmp[:tmp.find('\"',2)+1])
print(title,time)

print()
print()

line = 'Program "Kropka nad i" nadamy o: 22:00'
time = line[ line.find(':')+2 : ]
print(time)
tmp = line[ line.find('"')+1: ]
title = tmp [ : tmp.find('"')]
print(title, time)


