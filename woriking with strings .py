# to creat a new line we use \n 
print ('creat a new line here \n like this')
# to write anythig inside the string thet python dont allow it we use \ befor it 
# like : to put a ( " ) inside a string we put ( \ ) befor it
print (' ammar said once \' life is for smart people only \' ')

# a very cool thig we can do with bool and fuctions
smart = ' ammar '
print ( smart .upper () .isupper ())

# to know how many charecters inside a string we use len ()
print (len ( smart ))
 # to print a spicefic charecter that i know its index we do this
print ( smart [2]) 

# if u want to know the index of a charectar do this
print ( smart .index ('a'))
# to replace something use 
print ( smart .replace ('a', 'A'))
# to delete spaces  or any characer given
sentence = ("      3d     he loves her      $$$$   ")
print ( sentence .strip())
print (sentence .lstrip())
print (sentence .rstrip ())
print (sentence.strip ("$"))

# to make the fist litter of every word capital  and every litter after a number
print (smart .title())
# also to make every word captial but this fuctiona does not work after nums
print (smart .capitalize ())




# zfill

c , d ,e ,f = '1','24','35','656'
print (d)
print (e)
print (c)
print (f)

print (d.zfill(2))
print (e.zfill(2))
print (c.zfill(2))
print (f.zfill(2))


#spilt ()
# it splits the string into list using spaces by defult unless u gave it something
a = 'she love python and me'
a = 'she-love-python-and-me'

print (a.split())
print (a .split('-'))

# we can also give the spilt a max time for spilts 
print (a.spilt (),3)


# rspilt do the spilt but only  from the right
print (a.rsplit())

# center()

e = 'ammar'

print (e.center(9))
print (a.center(9,'#'))

# count 
f = ' i love python and java secerbt'
print (f.count('love'))
print (f .count('java',0,22))

# swapcase ()
g = 'i love python'
h = ' i  LOVE  pythobn'

print (g.swapcase())

# startwith()
# endwith()
i ='do you s]love python '

print (i.startswith("d"))
print (i("d"))

