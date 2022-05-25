def PrintAnimal(*animals):
    # this function prints a cat, bear or bat ascii-art
    txt_cat = r'''
|\---/|
| o_o |
 \_^_/'''
    txt_bear = r'''
/  \.-"""-./  \
\    -   -    /
 |   o   o   |
 \  .-'"'-.  /
  '-\__Y__/-'
     `---`'''
    txt_bat = r'''
   /\                 /\
  / \'._   (\_/)   _.'/ \
 /_.''._'--('.')--'_.''._\
 | \_ / `;=/ " \=;` \ _/ |
  \/ `\__|`\___/`|__/`  \/
          \(/|\)/  
     '''


    for animal in animals:
        if animal == 'cat':
            print(txt_cat)
            print('---------------')
        elif animal == 'bear':
            print(txt_bear)
            print('---------------')
        elif animal == 'bat':
            print(txt_bat)
            print('---------------')
        else:
            print("Cannot print '%s'. Correct values for the parameter are: cat, bear, bat" % animal)
            print('---------------')
        
    
    return 
 
''' 
if PrintAnimal():
    print('The parameter was correct')
else:
    print('The parameter was INCORRECT')
 
 
if PrintAnimal('dog'):
    print('The parameter was correct')
else:
    print('The parameter was INCORRECT')
 
 
if PrintAnimal('bat'):
    print('The parameter was correct')
else:
    print('The parameter was INCORRECT')
'''

PrintAnimal('cat','bear','wolf','bat')
