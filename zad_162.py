import math

def GiveGeomSeqElement(a1 = 2, factor =2, index =2):
    #wylicza awartość ciągu geometrycznego
    value = a1*math.pow(factor,index-1)
    return value

a1=3
factor = 2
maxindex =10

for index in range(1,maxindex):
    print('Term',index,'=',int(GiveGeomSeqElement(a1,factor,index)))



