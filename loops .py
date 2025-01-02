    # while loops
i = 0
while i <= 6 :
    print ('i love my life')
    i += 2
print ("the loop is done ")

#there is an other way to do a loop
# the word *continue * help u to ascape one loop or mabye more it depends

i = 1
while i<=10:
    i+= 1
    if i == 7 : continue
    print ( i )
print ('we are done here there is nothing to see')

#also we can use (break ) to end the loop immadetly

i =1
while i<=10 :
    i += 1
    if i == 4 : continue
    if i == 8 : break
print ("say something smart")    

#new loop named (for loop)
for me in 'life is full of chances ':
    print (me)

    # if you want to use a list

jobs = [ " editor " , " programer" , " driver"] 

for me in jobs :
    print (jobs[1])   
    print (jobs)

# something with nums
 
for anything in range (5 ,10) :
    print (anything)

for a in range (3,8) :
    print (a)
# if you want to be cool look at this 

jobs # i have it fome befor
for me in range (len(jobs)):
    print (me)