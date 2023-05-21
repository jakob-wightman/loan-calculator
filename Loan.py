class Loan:
  def __init__(self, loanAmount = 10000, annualRate = 5, year = 10):
    self.__loanAmount = loanAmount
    self.__annual_rate = annualRate
    self.__year = year

  def monthly_payment(self):
    monthly_interest_rate = (int(self.__annual_rate) / 100) / 12
    return (int(self.__loanAmount) * monthly_interest_rate) / (1 - (1/pow(1 + monthly_interest_rate, int(self.__year*12))))

  def total_payment(self):
     return self.__loanAmount * (1 + ((self.__annual_rate / 100.0)*self.__year))

  def get_loan_amount(self):
    return self.__loanAmount

  def set_loan_amount(self,loanAmount):
    return self.__loanAmount == loanAmount

  def get_annual_rate(self):
    return self.__annual_rate

  def set_annual_rate(self, annualRate):
    return self.__annual_rate == annualRate

  def get_year(self):
    return self.__year

  def set_year(self, year):
    return self.__year == year

  def __str__(self):
    return 'Loan Amount: ' + self.__loan_amount.__str__() + '\nAnnual Rate: ' + self.__annual_rate.__str__() + '\nYear: ' + self.__year.__str__() + '\nMonthly Payment: $' + self.monthly_payment().__str__()
    

