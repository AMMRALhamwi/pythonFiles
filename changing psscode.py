# enter a 4-digits PIN code:
# failure ! PIN code did not match/
# The computer generated this PIN : somenumber
import random
try:
    user_guss = int(input("enter a 4-digit PIN code :\n"))
except NameError:
    print("you did not enter a number")
except ValueError:
    print("you did not enter a number 2")

    if user_guss < 1000:

        print("you entered a 3 digits number or less , please enter a 4-digit number")
    elif user_guss > 9999:
        print('you entered a number that has more than 4 digits')
    else:
        com = random.randint(1000, 9999)

        if com == user_guss:
            print('CONGRATULATIONS \n you win this is the correct PIN ')
        else:
            print(" you lose \n the correct PIN is "+str(com))
