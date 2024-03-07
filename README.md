
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
