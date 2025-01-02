# to make a calculater that can rase a number to power

def rase_to_power (base_num , power_num):
    the_base =1
    for index in range (power_num):
        print (index)
        the_base = the_base* base_num
    return the_base 


print(rase_to_power (2,2))