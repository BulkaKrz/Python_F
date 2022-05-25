
a1 = 0
a2 = 1
a3 = 0
fibonacciIterations=20
for finobacci in range(0,fibonacciIterations+1): 
    
    print('%d \t %d' % (finobacci,a3))
    a1=a2
    a2=a3
    a3=a1+a2
print('---------------------------------')

fibonacciIterations = 20
a1 = 0
a2 = 1
a3 = 0
for i in range(0,20):
    print('Step',i,'value',a3)
    a1=a2
    a2=a3
    a3=a1+a2
print('-------------------------------------------------')




text = '''
Industrial Light & Magic: In this case, you find Python
used in the production process for scripting complex,
computer graphic-intensive films. Originally, Industrial
Light & Magic relied on Unix shell scripting, but it was
found that this solution just couldn’t do the job. Python
was compared to other languages, such as Tcl and Perl, and
chosen because it’s an easier-to-learn language that the
organization can implement incrementally. In addition, Python
can be embedded within a larger software system as a scripting
language, even if the system is written in a language such as
C/C++. It turns out that Python can successfully interact with
these other languages in situations in which some languages can’t.
'''
listOfWords = text.replace("\n"," ").split(" ")
for words in listOfWords:
    if "p" in words.lower():
        print(words)



dictionary={'A':'80%-100%','B':'60%-80%','C':'50-60%','D':'less then 50%'}
for words in dictionary:
   # print(words," - ",dictionary[words])
    print('%s - %s' % (words,dictionary[words]))



wordDictionary={}
for word in listOfWords:
    if word in wordDictionary.keys():
        wordDictionary[word] = wordDictionary[word]+1
    else:
        wordDictionary.setdefault(word,1)
        
print(wordDictionary)












