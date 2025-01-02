num1 = float (input ("please enter a number : \n"))
operatoer = input ("what opreatoer do you wanna use ? \n ")
num2 = float (input("please enter the second number :\n "))

if operatoer == "+" :
    print (num1 + num2)
elif operatoer == "-":
    print (num1 - num2)
elif operatoer == "*" :
    print (num1 * num2)
elif operatoer == '/' :
    print (num1 / num2)
else : print ("are you an ediot ? i told to use an operator ")            

print ("goodbye")