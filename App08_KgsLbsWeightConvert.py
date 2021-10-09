weight = input("What is your weight? ")
conv = 2.205

question = input("(K)g or (L)bs? ")

if question == "K" or question == "k":
    print("You weigh " + str(float(weight) * float(conv)) + " kgs")      #print weight converted from kg to lbs

elif question == "L" or question == "l":
    print("You weigh " + weight + " lbs.")
