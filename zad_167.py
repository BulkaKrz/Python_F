import os
import time
'''
print("Current directory is:",os.getcwd())
currentDir = os.getcwd()
filename = 'results.txt'
fullpath = os.path.join(currentDir,filename)
print("/n The constructed filepath is:",fullpath)
'''
dir=input("podaj ścieżkę dostępu do katalogu: ")
if not os.path.isdir(dir):
    print('%s is must be a directory' % (dir))
else:
    file = input('podaj nazwę pliku: ')
    path = os.path.join(dir,file)
    if not os.path.isfile(path):
        print('File %s doesn\'t egzist' %(path))
    else:
        print('information about flie %s' %(path))
        print("last modified time:",time.localtime(os.path.getmtime(path)))
        print("size in kB", os.path.getsize(path)/1024)
        print("current path" , os.getcwd())
        print("relative path :", os.path.relpath(path))
        print("path split :", os.path.split(path)[0])
        print("relative path split :", os.path.split(path)[1])
