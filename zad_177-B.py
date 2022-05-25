import os
isfileexist = False
webadress=[]
polweb=[]
wweb=[]
while isfileexist == False:
    filename = input("Podaj ścieżkę dostępu do pliku: ")
    
    if os.path.isfile(filename) == False:
        print("Wskazany plik nie istnieje")
        isfileexist = False
        
    else:
        
        with open(filename,'r') as file:
            for line in file:
                webadress.append(line.replace("\n",""))
                
                

        isfileexist = True
        
for line in webadress:
    if line.endswith(".pl"):
        polweb.append(line)
    else:
        wweb.append(line)


fileDir = os.path.dirname(filename)
filewebs_pl = os.path.join(fileDir,'webs_pl.txt')
filewebs_other = os.path.join(fileDir,'webs_other.txt')

file = open(filewebs_pl,"w")
for web in polweb:
    file.write(web +"\n")
file.close()


file = open(filewebs_other,"w")
for web in wweb:
    file.write(web +"\n")
file.close()

print("polskie: ",polweb)
print("nie polskie: ",wweb)
    

