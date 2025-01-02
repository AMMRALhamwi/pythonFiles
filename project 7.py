 # project 7 how old are you

print ('please enter your birthday date ')

str_year = input (" the year : \n")
str_month = input (" the month: \n")
str_day = input (' the day : \n')

print ('please enter the current date ')
str_current_year = input (" the year : \n")
str_current_month = input (" the month : \n")
str_current_day = input (" the day : \n")

#convert

float_year = float (str_year)
float_month = float (str_month)
float_day = float (str_day)
float_current_year = float (str_current_year)
float_current_month = float (str_current_month)
float_current_day = float (str_current_day)

# the currnt age

float_result_year = float_current_year - float_year
float_result_month = float_current_month - float_month
float_result_day = float_current_day - float_day

float_months = float_result_year * 12 + float_result_month
float_days = (float_result_year * 365 ) + (float_months *30.5 ) + float_day
float_hours = float_days * 24
float_minutes = float_hours * 60
float_seconds = float_minutes * 60

#  convert

years = str (float_result_year)
months = str (float_result_month)
days = str (float_result_day)

age_by_months = str (float_months)
age_by_days = str (float_days)
age_by_hours = str (float_hours)
age_by_minuts = str (float_minutes)
age_by_seconds = str (float_seconds)

print ("you have " + years + ' years and '+ months + ' months ' + days + ' days ' )
print ("your age by months is : " + age_by_months )
print ("your age by days is : "+ age_by_days )
print (" your age by hours is : "+ age_by_hours)
print (" your age by minutes is : " + age_by_minuts )
print (" your age by seconds is : " + age_by_seconds )