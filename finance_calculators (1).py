"""
This program will allow the user to access two different financial calculators.
The investment calculator will calculate the user's interest on an investment.
The home loan repayment calculator will calculate the amount that should be
repaid on a home loan each month.

The user can choose which calculation they want to do. Capitalisation in user
input will not affect validity of entries, but the program will show an error
message if the user doesn't type in a valid input.

If the user selects the investment calculator, the program will:

    Ask the user to input the amount of money they are depositing, the interest
    rate (as a number percentage), and the number of years they plan on
    investing.

    Ask the user if they want simple or compound interest, and
    store this in a variable called 'interest'.
    
    Output the amount the user will get back after the given period, at the
    specified interest rate.

    The program will caculate simple interest using the formula,
    A = P(1 + r x t), written in Python as A = P *(1 + r*t).

    The program will calculate compound interest using the formula,
    A = P(1 + r)^t, written in Python as A = P * math.pow((1+r),t).

    In the formulae above, 'r' is the interest entered by the user divided
    by 100.'P' is the amount that the user deposits. 't' is the number of
    years that the money is being invested. 'A' is the total amount once the
    interest has been applied.
    
If the user selects the home loan repayment calculator, the program will:

    Ask the user to input the present value of the house, the interest rate,
    and the number of months they plan to take to repay the bond.
    
    Calculate the amount to be repaid on a home loan each month using the
    following formula. repayment = ((i x P) divided by (1- ((1+i)^-n)), written
    in Python as repayment = (i * P)/(1 - (1+i)**(-n)).
    
    Output how much money the user will have to repay each month.
    
    In the formulae above, 'P' is the present value of the house, 'i' is the
    monthly interest rate, 'n' is the number of months over which the bond will
    be repaid.  
    
"""
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