print ("""
    ☠  ☠  ☠  ☠
""")
print ('welcome to my island ! in my island you might get killed so watch up you have 3 lives')
print(' there are two doors in front of you 🚪 a red door and 🚪a blue door' )
door= input(' which one do you want to open\n').lower()
killes =0
dead =False
while killes <3 :

    if door == 'blue' and not dead :
        print('oops ! you chose the crocodile door . 🐊🐊🐊')
        killes +=1
        dead = True
    elif door == 'red' and not dead:
        print ('Great now you enterd a room.')
        print('you found three boxes :📦 white 📦 black 📦 green ')
        box = input("wich box do you open ?\n").lower()
        if box == 'white' and not dead:
            print("oops ! you opened a box filled with snakes 🐍🐍🐍")
            killes +=1
            dead=True
        elif box == 'black' and not dead:
            print (' oops ! you openes a box filled with spiders 🕷🕷')
            killes+=1
            dead = True
        elif box == 'green'and killes<3:
            print('congratulations ! you found the treasure ! 💎💎')        
        else:
            print('invald value try again !')    
    else :
        print('invald value try again !')


input("the game has ended")
 