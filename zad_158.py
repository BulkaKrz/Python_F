def DoAction(action,parametr):
    print('action:',action)
    print('parametr:',parametr)
    return
print('----------DoAction-------------')
DoAction('buy','shoes')

def DoAction2(action,*parametr):
    print('action:',action)
    print('parametr:',parametr)
    for element in parametr:
        print('element is:',element)
    return
print('---------DoAction2--------------')
DoAction2('buy','shoes','socks')
DoAction2('buy','shoes','socks','t-shirt')

def DoAction3(action,what,**parameter):
    print('action:',action)
    print('what:',what)
    print('parametr:',parameter)
    for element in parameter:
        print(element,'=',parameter[element])
    return
print('----------DoAction3-------------')
DoAction3('buy','shoes',size=45,color='brown',type='sport')
