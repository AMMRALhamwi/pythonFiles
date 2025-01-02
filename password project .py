# password app pro max

password1 = input (" enter your new password \n")
password2 = input (" rewrite your new password \n")
hint = input ('enter a hint so we can help to remember your password if you forgot it \n')

# checking if the passwords 2=1
if len(password2)<8 :
    print ('the password should be at least 8 charecters or numbers ')
elif password1 == password2 :
    correct_password =password2 
else :
    print (" the passwords are not the same please try again ") 

       # the user opnes the app and entering the  password
password =""
times =0
out_of_chanses = False
while password != correct_password and not out_of_chanses :
    if times <1:
       password = input ("enter your password\n")
       times +=1
    elif times<2:
        password = input ('the password is incorrect try again \n ')
        times +=1
        print ('this might help '+hint)
    elif times <3 :
        password = input ("the password is incorrect please try again \n ") 
        times+=1 
        print ('this might help '+hint)
    else :
        out_of_chanses = True
if password == correct_password :
    print (" the password is correct : WELCOME ")
else :
    print("it seems like you have forgoten your password ")                  