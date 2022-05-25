#import datetime
#print(datetime.MINYEAR,datetime.MAXYEAR)

#print(datetime.date.today())
#print(datetime.datetime.now())

inputdata = [0,1,2,3,5,8,13,21,34,55,89]
factortable = [0,0.01,0.02, 0.03,0.05,0.08,0.13,0.21,0.34,0.55,0.89]

import math

print(len(inputdata))
print(len(factortable))

if len(inputdata) == len(factortable):
    for n in range(0,len(inputdata)):
        minvalue = inputdata[n] - factortable[n] * inputdata[n]
        maxvalue = inputdata[n] + factortable[n] * inputdata[n]
        
        
        mininteger = math.floor(minvalue)
        maxinteger = math.ceil(maxvalue)
        
        print(mininteger,'\t', inputdata[n],'\t', maxinteger)    
    
else:
    print("inputdata and factortable need to have equal number of elements")

print('--------------------')

import random

for n in range(0,len(inputdata)):

    randomvalue = random.random()
    minvalue = inputdata[n] - randomvalue * inputdata[n]
    maxvalue = inputdata[n] + randomvalue * inputdata[n]   
    mininteger = math.floor(minvalue)
    maxinteger = math.ceil(maxvalue)
    print(randomvalue)   
    print(mininteger,'\t', inputdata[n],'\t', maxinteger)    
    
import datetime
print(datetime.date.today())
print(datetime.date.today().strftime("%Y.%m.%d"))
