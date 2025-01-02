guess = ""
secret_word = "ammar"
times = 0
out = False

while guess != secret_word and not out:
    if times <1 :
        guess = input ("u have 3 trys ,throw a guess \n")
        times+=1
    elif times <2 :
        guess = input ("u still have two try , try again \n ")
        times +=1
    elif times <3 :
        guess = input ("its ur last chance if u did not guess corectly u are gonna lose\n try again \n")
        times +=1
           
    else :
        out = True
if guess == secret_word:
    print ("we have a winer")
else:
    print ("Game over")    
        
