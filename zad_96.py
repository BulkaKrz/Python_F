'''for x in range(1,6):
    for y in range(1,6):
        print(x,'*',y,'=',x*y)
        

print('--------------')

for x in range(1,6):
    line = str(x)
    for y in range(1,6):
        line += '\t%3d'%(x*y)
    print(line)
    '''

w=1
for i in range(1,11):
    s=str()
    w=w*i
    for j in range(1,i+1):
        s += str(j)+'*'
        mesage='%2d! = %s = %d' % (i,s[0:len(s)-1],w)
    #print(i,'! = ',s[0:len(s)-1],'=',w)
    print(mesage)

'''
print('---------------')
i = 10
result = 1
 
for j in range(1,i+1):
    result *= j
 
print(i, result)
 
print('------------')
x = 10
 
for i in range(1,x+1):
 
    result = 1
    
    for j in range(1,i+1):
        result *= j
 
    print(i, result)
''' 
 
print('-----------------------------------------')

list_noun = ['dog', 'potato', 'meal', 'icecream', 'car']
list_adj = ['dirty', 'big', 'hot', 'colorful', 'fast']

for i in range(0,len(list_noun)):
    noun = list_noun[i]
    
    for j in range(0,len(list_adj)):
        adj = list_adj[j]
        print('%-15s %s' % (adj,noun))

print('-----------------------------------------')







