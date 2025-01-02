# we need to know if the use is over 18 and if he has a  licens to drive
age = int(input ('what is your age ? \n '))


if age >=18 :
    license = input ('do you have a license ?').lower()
    if license== 'yes':
        print ( f' your age is {age} and you have license u r good to go ')
    elif license== "no":
        print(f'your age is {age} you cannt drive go get yourself a license ')
    else :
        print(' invaled answer try again ')        
    
else :
    print('you are under age you cannot drive wait until 18')    