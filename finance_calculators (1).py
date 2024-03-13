import math

print("investment \t - to calculate the amount of interest you'll earn on your \
investment \nbond \t \t - to calculate the amount you'll have to pay on a \
home loan\n")

calculator_choice = input("Enter either 'investment' or 'bond' from the menu \
above to proceed: ").lower()

if calculator_choice == "investment":
    print("You have selected the investment calculator.")
    deposit = float(input("How much money are you depositing? Please enter a \
number: "))
    inv_interest_rate = float(input("What is your interest rate? Please enter a \
number: "))
    years = int(input("How many years do you plan to invest? Please enter a \
number: "))
    interest = input("Would you like simple or compound interest calculated? \
Please enter either 'simple' or 'compound': ").lower()
    if interest == "simple":
        simple_interest = deposit * (1 + ((inv_interest_rate / 100)*years))
        print(f"The total amount is {simple_interest}.")
    elif interest == "compound":
        compound_interest = deposit * math.pow((1+(inv_interest_rate / 100)),years)
        print(f"The total amount is {compound_interest}. ")
    
elif calculator_choice == "bond":
    print("You have selected the home repayment calculator.")
    house_value = float(input("What is the present value of the house? Please \
enter a number: "))
    house_interest_rate = float(input("What is the interest rate? Please \
enter a number: "))
    months = int(input("How many months do you plan to take to repay the \
bond? Please enter a number: "))
    repayment = ((house_interest_rate / 12) * house_value)/(1 - (1+(house_interest_rate / 12))**(-months))
    print(f"Each month, you should repay {repayment}: ")
              
else:
    print ("Error. Please make a valid selection.") 