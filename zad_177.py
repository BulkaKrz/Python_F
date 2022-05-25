import os
webaddresses = []
line = input('Enter web address like "www.python.org" or press ENTER to stop: ')
while line != "":
    webaddresses.append(line)
    line = input("Please inserw www address or press ENTER to stop: ")

dirname = os.getcwd()
filename = input("insert filename: ")
filepath = os.path.join(dirname,filename)

file = open(filepath, "w")
#file.writelines(webaddresses)
for web in webaddresses:
    file.write(web+"\n")
file.close()

    

