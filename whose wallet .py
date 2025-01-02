# welcome to whose wallet ?
# you will give me a list of names , and i will pick a person to pay
# if you`re ready , enter the names seprated by a comma
# name name name name
# please ask name to take his wallet out . Dinner is on name
# every time a diffirent name is picked

# psodo code
import random
print('welcome to `whose wallet ?`')
print('you will give me a list of names , and i will pick a person to pay ')
string_input = input(
    "if you are ready , enter the names seprated by a comma \n ")
listed = string_input.split(', ')
length = len(listed)
picking = random.randint(0, length-1)
choicen = (listed[picking])
print('please ask ' + choicen + ' to take his wallet out . Dinner is on ' + choicen)
