import random
print('welcome to the coin guessing game')
print("let`s choose a method to toss the coin :")
print("""1. using random.random() \n2. using random.randint()
""")
choise = int(input('enter your choise (1 or 2 ): \n'))
if choise == 1:
    user_guess = input(' enter your guess , tails or heads ? \n ').lower
    random_number = random.random()
    if random_number >= 0.5:
        print("the coin landed on heads ")
        if user_guess == 'heads':
            print("congratuationd , it`s heads")
        else:
            print("its heads you lose ")
    else:
        print("the coin landed on tails ")
        if user_guess == 'tails':
            print(' nice guess you won ')
        else:
            print("hard luck its heads, you lose")
elif choise == 2:
    user_guess = input(' enter your guess , tails or heads ? \n ').lower
    random_number2 = random.randint(0, 1)
    if random_number2 == 1:
        print("the coin landed on heads ")
        if user_guess == "heads":
            print("congratuationd , it`s heads")
        else:
            print("its tails you lose ")
    else:
        print("the coin landed on tails ")
        if user_guess == 'tails':
            print(' nice guess you won ')
        else:
            print("hard luck its tails, you lose")
else:
    print(' you should choose only 1 or 2')
