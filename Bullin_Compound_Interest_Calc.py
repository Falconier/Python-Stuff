''' 
        Bullin_Coupound_Interest_Calc.py
        calculates annually compounded interest for a given initial amount(initialAmount) and given rate (annualRate)
        Jacob Emory Bullin
        Jan 28, 2019
'''
def main():
    initialAmount = input("Initial investment (enter number): ")
    
    numYears = input("How many years are you investing for (enter number): ")
    annualRate = input("What is the annual rate (enter as percentage): ")

    rate = (annualRate/100)

    finalAmount = initialAmount*(1+((rate/1)**(numYears)))

    print(finalAmount)

main()