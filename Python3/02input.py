# Sample Code - Intro
print("Welcome to DataScience with Python ")
birth_year = input('what year were you born? ')
import datetime
x = datetime.datetime.now()
current_year = x.year
age = int(current_year) - int(birth_year)
print('you are {} years old'.format(age))
