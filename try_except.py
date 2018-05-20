valid = False
while valid == False:
    try:
        amount = int(input("Enter the total amount: "))
        valid = True     # This statement will only execute if the above statement executes without error.
        print("You must be {0} years old.".format(amount))
    except ValueError:
        print("Your amount must be numeric.")
