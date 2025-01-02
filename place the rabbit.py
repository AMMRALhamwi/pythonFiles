
print('Welcome to place the rabbit [ 🌳 , 🌳 , 🐇 ]')
field = [[' 🌳 ',  ' 🌳 ', ' 🌳 '],  [' 🌳 ', ' 🌳 ',  ' 🌳 '], [' 🌳 ', ' 🌳 ', ' 🌳 ']]
print(f'{field[0]}\n {field[1]} \n {field[2]}')
indix = input(
    'where should the rabbit go ?\n please choose a row and a column \n')
row = int(indix[0])
column = int(indix[1])

field[row-1][column-1] = "🐇"
print(f'{field[0]} \n {field[1]} \n {field[2]}')
