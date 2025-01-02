# add the first color you like : blue
# Do you want to add more colors yes , or no ? yes
# Add another color to the list : green
# the colors you like are :['blue' , 'green']

colors = []
colors.append(input('Add the first color you like :\n'))
checking = True
check = input(
    "Do you want to add more colors the list (yes or no )? \n ")
if check.lower() == 'yes':
    colors.append(input('Add another color to the list : \n'))
    print(f"the colors you like are :")
    print(colors)
else:
    print(f'thank you here is your list ')
    print(colors)
