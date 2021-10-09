import time
name = input('What is your name? ')
print('Hello, ' + name)

birth_year = input("enter your birth year: ")
age = 2021 - int(birth_year)
print("sorry, " + name + ", no one asked")   #print response to age

time.sleep(2)                 #delay response for comedic effect
print("anyway i guess you are " + str(age) + " years old. congrats.")
time.sleep(2)