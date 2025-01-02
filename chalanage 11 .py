# list of products 
#           watches phones charagers

produces= input (' do you want \\watctes \\ or \\ phones\\ or \\chargers \\ \n')
#print (produces .lower())

if produces.lower() == 'watches' :
    print ('what kind of watches do you want ?')
elif produces.lower() == 'phones' :
    print ('what kind of phones do you want ?')
elif produces.lower() == 'chargers':
    print ('what kind of chargars do you want ?')
else:
    print('invaled input try again ')    