'''
        Bullin_Coupound_Interest_Calc.py
        calculates annually compounded interest for a given initial amount(initialAmount) and given rate (annualRate)
        Jacob Emory Bullin
        Jan 28, 2019
'''


def main():
    ## get inputs (initial amount, the number of years to invest, and the annual interest rate
    initialAmount = int(input("Initial investment (enter number): "))
    numYears = int(input("How many years are you investing for (enter number): "))
    annualRate = int(input("What is the annual rate (enter as percentage): "))

    ## calculations
    ## convert annualRate to decimal (float)
    rate = (annualRate / 100)

    ## Calculate investment
    finalAmount = initialAmount * (1 + ((rate / 1) ** (numYears)))

    for i in range(0,numYears):

        print("Interest gained in year", i," : ", (initialAmount * (1 + ((rate / 1) ** i))) - initialAmount)


    ## print the amount
    print("Your investment total is :", finalAmount)


main()
