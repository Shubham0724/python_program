## If Statements
applePrice = 180
budget = 200
if (applePrice <= budget):
    print("Alexa, add 1kg Apples to the cart.")


##if-else Statements
applePrice = 210
budget = 200
if (applePrice <= budget):
    print("Alexa, add 1kg Apples to the cart.")
else:
    print("Alexa, do not add Apples to the cart.")

##elif Statement
num = 0
if (num < 0):
    print("Number is negative.")
elif (num == 0):
    print("Number is Zero.")
else:
    print("Number is positive.")

##Nested if Statement
num = 18
if (num < 0):
    print("Number is negative.")
elif (num > 0):
    if (num <= 10):
        print("Number is between 1-10")
    elif (num > 10 and num <= 20):
        print("Number is between 11-20")
    else:
        print("Number is greater than 20")
else:
    print("Number is zero")        
