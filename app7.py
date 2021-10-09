temp = 30
print("The temperature is currently " + str(temp) + " degrees.")
print()         #line break

if temp > 75:   #HOT DAY
    print("It's a hot day.")
    print("Drink plenty of water!")
elif temp < 75: #NORMAL DAY
    print("It's a nice day.")
elif temp < 55:
    print("It's a bit chilly out.")
    print("You might want to get a jacket.")