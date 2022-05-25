
def championCup():
    print("""

      ██████████████████████      
      ██                ░░██      
████████   ZUZIA :-)    ░░████████
██    ██        ▒▒      ░░██    ██
██    ██      ▒▒▒▒      ░░██    ██
████  ██        ▒▒      ░░██  ████
  ██████        ▒▒      ░░██████  
      ██        ▒▒      ░░██      
      ████            ░░████      
        ████        ░░████        
          ████    ░░████          
              ██  ██              
              ██  ██              
              ██  ██              
            ████  ████            
          ██        ░░██          
          ██████████████

    """)


corect_answers_list = ("Doskonale Zuziu tak trzymaj",
                       "Super jesteś Wielka",
                       "Nooo i to jest właściwa odpowiedź",
                       "Zawsze sięgaj gwiazd",
                       "Właśnie TAK :-)",
                       "Widzeze sie postaralas",
                       "B..R..A..W..O.. BRAWO",
                       "Ale fe ale fe Ale fenomenalne fantastyczne i genialne",
                       "Przybyli ułani pod okienko! Przybyli ułani pod okienko! stukają pukają i… wybili szybe!",
                       "Zuziu do dzieła"
                       )
                       
                       
                       
                       




import random
print("""
    To jest gra sprawdzająca twoją znajomość tabliczki mnożenia.
    Twoim zadaniem jest podać poprawną odpowiedź na podaną liczbę pytań.
    Jeśli odpowiesz niepoprawnie pytanie nie będzie uznane.
    Na końcu dowiesz się ile pytań Ci zadałem i na ile poprawnie odpowiedziałaś.

    """)
haw_many_quest = int(input("Zuziu na ile pytań odpowiadasz: "))

quest = 0
quest_ok = 1
quest_score = 0
while quest_ok < haw_many_quest +1:
    quest+=1
    a = random.randint(2,9)
    b = random.randint(2,9)
    print("Oblicz w pamięci wynik możenia {} * {} = ?".format(a,b))
    c = int(input("Podaj ile wynosi wynik : "))
    if a*b == c:
        print(random.sample(corect_answers_list,k=1))
        print("DOBRZE!!!")
        print()
        quest_ok+=1
        quest_score+= 1
        
    else:
        print("Oj Zuziu kraby są zmartwione")
        print("Pytanie nie zostaje uznane. Spróbuj jeszcze raz\n")
print("-----------------------------------------------")       
print("Odpowiedziałaś poprawnie na {} pytania. Huraaaaaaaaaaaa!!" .format(haw_many_quest))
print("ZZadałem Ci łącznie {} pytania punkty które zdobyłaś to {}" .format(quest, quest_score))
print("-----------------------------------------------")
championCup()

