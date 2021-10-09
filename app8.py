weight = input("What is your weight? ")
conv = 2.205


question = input("(K)g or (L)bs? ")
if question == "K" or question == "k":
    product = float(weight) * float(conv)
    print("You weigh " + str(product) + " kgs.")
elif question == "L" or question == "l":
    print("You weigh " + weight + " lbs.")
