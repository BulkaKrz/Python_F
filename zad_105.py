'''
initialCapital = 20000
percent = 0.03
maxTimeYears = 10
year = 0
while year < maxTimeYears:
    capital = initialCapital*percent
    print(year, '\t',round(initialCapital,2),'\t',round(capital,2),'\t',round(initialCapital+capital,2))
    initialCapital = initialCapital+capital
    year+=1
print('-------------------------------------------------------')
 
initialCapital = 20000
percent = 0.03
maxTimeYears = 10
year=0
capital=initialCapital
while year<maxTimeYears:
    year+=1
    capital=round((1+percent)*capital,2)
    print('after this year:', year,  'you will have:',capital)
else:
    print('the total revenue is', capital-initialCapital)
print('-------------------------------------------------------')
 


number = 20730906
zm = number
suma = 0
while zm>0 :
    cyfra=zm % 10
    suma = suma + cyfra
    zm = zm // 10
print(suma)    
'''

text ='''
United Space Alliance: This company provides major support to NASA for
various projects, such as the space shuttle. One of its projects is to
create Workflow Automation System (WAS), an application designed to
manage NASA and other third-party projects. The setup uses a central
Oracle database as a repository for information. Python was chosen over
languages such as Java and C++ because it provides dynamic typing and
pseudo-code–like syntax and it has an interpreter. The result is that
the application is developed faster, and unit testing each piece is easier.
'''
print(text)
number=0
listOfWords = text.replace('\n',' ').split(' ')
shortWords = 0
longWords = 0
while number < len(listOfWords):
    words = listOfWords[number]
    if len(listOfWords[number])> 6:
        longWords+=1
      
    elif len(listOfWords[number])>0 :
        shortWords+=1
       
    number+=1
print('Ilość słów dłuższych niż 6 znaków to:',longWords)
print('Ilość słów krótszych niż 6 znaków to:',shortWords)



text = '''
United Space Alliance: This company provides major support to NASA for
various projects, such as the space shuttle. One of its projects is to
create Workflow Automation System (WAS), an application designed to
manage NASA and other third-party projects. The setup uses a central
Oracle database as a repository for information. Python was chosen over
languages such as Java and C++ because it provides dynamic typing and
pseudo-code–like syntax and it has an interpreter. The result is that
the application is developed faster, and unit testing each piece is easier.
'''
listOfWords = text.replace('\n',' ').split(' ')
wordLength = 6
i=0
shortWords = 0
longWords = 0
while i< len(listOfWords):
    if len(listOfWords[i])>wordLength:
        longWords+=1
    elif len(listOfWords[i])>0:
        shortWords+=1
    
    i+=1
print("Words shorter than ",wordLength,":",shortWords)
print("Words longer than ",wordLength,":",longWords)
   

