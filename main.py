from Loan import Loan

def main():
  #Get user inputs
  loanAmount = float(input('Enter loan amount: '))
  annualRate = int(input('Enter annual rate: '))
  year = int(input('Enter duration of loan in years: '))

  #Create a loan object
  loan = Loan(loanAmount, annualRate, year)

  #call monthly payment
  print(f'\nMonthly Payment: ${loan.monthly_payment():.2f}')
  #call total payment
  print(f'Total Payment: ${loan.total_payment():.2f}')
  #Displays Info

  print(f'\nLoan Amount: ${loan.get_loan_amount()}')
  print(f'Annual Interest Rate: {loan.get_annual_rate()}%')
  print(f'Number of Years: {loan.get_year()}')

if __name__ == '__main__':
  main()
