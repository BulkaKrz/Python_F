'''
file = open("d:\\Test2\\joke.txt","r")
content = file.read()
print(content)
file.close()

with open("d:\\Test2\\joke.txt","r") as file:
    content = file.read()
    print(content)



with open("d:\\Test2\\joke.txt","r") as file:
    for line in file:
        print(line)
'''
file = open("d:\\Test2\\joke.txt","r")
fragment = file.read(10)
while fragment:
    print(file.tell(),fragment)
    fragment = file.read(10)

file.close()
