'''
import os
fileIsOk = False

while not fileIsOk:
    filename = input('Enter path to results file: ')
    if os.path.isfile(filename):
        fileIsOk = True
    else:
        print('filename is not correct')
  
print('The rezults file is %s' % (filename))

'''

import os


while True:
    filename = input('Enter path to results file: ')
    if os.path.isfile(filename):
        break
    else:
        print('filename is not correct')
  
print('The rezults file is %s' % (filename))
