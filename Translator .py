# the girrafe languge 
def translate (phrase ):
    translation = ""
    for letter in phrase:
        print (letter)
        if letter.lower() in 'aeiou':
            translation = translation+ "g"
        else:
            translation =translation + letter
    return translation



print (translate (input ( 'enter a phrase : \n' ) ))