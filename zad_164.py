'''
filename = input("Enter filename: ")
print("The file name is: %s" % (filename))

while True:
    filesizeStr = input('Enter the max file size: ')
    if filesizeStr.isdecimal():
        filesizeInt = int(filesizeStr)
        break
print('The max file size is %d' % (filesizeInt))   
print('The max file size is %d' % (filesizeInt *1024))

'''
def check_int(s):
    if s[0] in ('-', '+'):
        return s[1:].isdigit()
    return s.isdigit()

a_str = input('a=')
b_str = input('b=')
c_str = input('c=')


if not check_int(a_str) and check_int(b_str) and check_int(c_str):
    print('a,b,c = muszą być liczbami całkowitymi')
else:
    
    a=int(a_str)
    b=int(b_str)
    c=int(c_str)
    
    if a == 0:
        print(' to nie jest równanie kwadratowe nie można dzielić przez zero')
     
    else:
        delta = b**2 - 4*a*c
        if delta < 0:
            print('brak rozwiązań')
        elif delta == 0:
            x1= -b/(2*a)
            print('x = %f' %(x1))
        elif delta > 0:
            x1= (-b - delta**0.5)/(2*a)
            x2= (-b + delta**0.5)/(2*a)
            print("there are two solutions: %.2f and %.2f" % (x1,x2))
            

    
