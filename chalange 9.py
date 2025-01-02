# passward program

password = ''
correct_password = input (" enter a strong passward but make sure to remember it \n ")
times = 0
out_of_guesses = False

while password != correct_password and not out_of_guesses :
    if times < 1:
        password =input (" enter your password \n")
        times +=1
    elif times <3:
        password= input (' incorrect password try again \n' )    
        times+=1
    else:
         out_of_guesses = True      

if password == correct_password :
    print ("the password is correct ")
else :
    print ('it seems like you have forgoten your password ')    
    new_password =input (" enter your new password \n ")