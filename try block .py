# there is a way that we can use to make the program fuctionl even if the user was an ediot
# lets say u asked for a number but the user did enter someting ese like this \;
 :
    num =int(input('enter a number \n'))
    print (num)
except :
    print ( " you are an ediot are not you ")    

    # we can make this block catch specific kind of errors

 :
    num1 = int(input ("enter a num \n"))
    num2 =int(input ("enter a num \n"))
    print (num1 / num2)
except ZeroDivisionError :
    print ("math do not eccepet division to zero ")    
except ValueError as err :
    print (err)    