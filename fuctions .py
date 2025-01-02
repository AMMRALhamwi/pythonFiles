# this how to creat a fuction 
def sayHi ():
    print ('HI USER , HAVE A NICE DAY')

    # TO CALL THE FUCTION 
    #type the name of it with open and close
sayHi ()    

# we can do this cool stuff
name = input ('enter ur name\n')
def hi (name):
    print ('how is it going '+name)

hi (name)

# if you want to have information back use return 
# but be aware that when ever u use retern its gonna be the end of the fuction

def cube (num) :
    return num * num*num

print (cube (2))