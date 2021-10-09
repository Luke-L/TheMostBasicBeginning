sval = int(input("enter starting value "))
eval = int(input("enter final value "))
step = int(input("what is the step? "))
numbers = range(sval, eval, step)
for number in numbers:
    print(number)