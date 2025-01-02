# if u want to add a list into another list use
lucky_people = ['katreen','reem','fadowa','raghad']
normal_people = ['kazem','bashar']
print ('these people are luck and normal becase they are gonna work for me ') 
lucky_people.extend(normal_people)
print (lucky_people)

# if u want to add an item into a list 
lucky_people.append ('deama')
print (lucky_people)

#if u want to add an item into a spicific place in a list
lucky_people .insert(3 , " reham")
print (lucky_people)

#if u want to remove an item
lucky_people .remove ('reem')
print (lucky_people)

# if u want to remove everything 
#lucky_people.clear()
#
#print ( lucky_people) 

# to remove the last item 
lucky_people.pop()
print (lucky_people )

# to check if an item is exeit in the list
print( lucky_people .index("raghad"))
lucky_people .append ("jim")
lucky_people . append ("jim")
print (lucky_people)
print (lucky_people.count("jim"))

# to sort AKA organize the list ues sort
lucky_people .sort ()
print (lucky_people)

# to revers the order of the list

lucky_people .reverse()
print (lucky_people)

# to copy a hole list
lucky_people_2 = lucky_people.copy ()
print (lucky_people_2)