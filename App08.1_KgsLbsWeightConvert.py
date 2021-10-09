weight = input("What is your weight? ")
conv = 0.4535


question = input("(K)g or (L)bs? ")
if question == "K" or question == "k":
    print("You weigh " + str(float(weight) / float(conv)) + " lbs.")

elif question == "L" or question == "l":
    print("You weigh " + str(float(weight) * float(conv)) + " kgs")