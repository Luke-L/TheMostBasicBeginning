import time
from time import gmtime, strftime
name = input('What is your name? ')
print('Hello, ' + name)

CurYear = float(strftime("%Y", gmtime()))       #get the current year (holy shit it works
birth_year = input("enter your birth year: ")
age = int(CurYear) - int(birth_year)
print("sorry, " + name + ", no one asked")      #print response to age

time.sleep(2)                                   #delay response for comedic effect
print("anyway i guess you are about " + str(age) + " years old. congrats.")
time.sleep(2)