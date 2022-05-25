'''Pharma A, Vitamin C,100
Drugstore XYZ,Penicilin, 20, pills
Drugstore ABC,Aspirin,60
Pharma X,Montelukast,10'''
 

''' 
 
with open(file_path,"r") as file:
 
    for line in file:
 
        line = line.replace('\n','')
        order = line.split(',')
 
        if len(order) == 3:
            print('Order from drugstore "%s", item "%s", amount %s' %
                  (order[0],order[1],order[2]))
        else:
            print("Line %s malformed!!!" % line)
 
print("Processing finished")

'''

import sys

file_path = r'D:\Test2\orders.csv'

with open(file_path,"r") as file:
     
    for line in file:
 
        line = line.replace('\n','')
        order = line.split(',')
        try:
               
            pharmacy_name = order[0]
            item = order[1]
            amount = int(order[2])
            print('Order from drugstore "%s", item "%s", amount %d' % (pharmacy_name,item,amount))
        except ValueError as e:
            print("Problem z linijką %s - spowodowany niewłasciwą daną nie da się skonwertować - " % line)
        except IndexError as e:
            print("Problem z linijką %s - zaało informacji - " % line)
        except:
            print("Problem with line %s" % line)
            print(sys.exc_info()[0])

                  
print("Processing finished")













