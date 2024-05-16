'''
Mortgage Calculator - Calculate the monthly payments of a fixed term mortgage over given Nth terms at a given interest rate. 
Also figure out how long it will take the user to pay back the loan. 
'''

def mortgageCalculator():
    loanAmount = float(input("Enter the loan amount: "))
    interestRate = float(input("Enter the interest rate: "))
    loanTerm = int(input("Enter the loan term in years: "))
    monthlyInterestRate = interestRate / 100 / 12
    numberOfPayments = loanTerm * 12
    monthlyPayment = (loanAmount * monthlyInterestRate) / (1 - (1 + monthlyInterestRate) ** -numberOfPayments)
    totalPayment = monthlyPayment * numberOfPayments
    print(f"Monthly payment: {monthlyPayment}")
    print(f"Total payment: {totalPayment}")
    print(f"Total interest paid: {totalPayment - loanAmount}")

mortgageCalculator()
