num = int(input ( " Enter the duration in seconds : \n " ))
rest_h = num %3600 
rest_min = rest_h %60
print (f" the duration is: {num // 3600} hours , {rest_h //60} minutes and {rest_min} seconds ")