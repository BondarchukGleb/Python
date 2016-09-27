# Paying off credit card debt

balance = float(input('Balance = '))
annualInterestRate = float(input('Annual interest rate = '))
monthlyPaymentRate = float(input('Monthly payment rate = '))

months = 12
monthlyInterestRate = annualInterestRate / months

currentMonth = 1
currentBalance = balance
totalPaid = 0

while currentMonth <= months:
    minimumMonthlyPayment = currentBalance * monthlyPaymentRate
    monthlyUnpaidBalance = currentBalance - minimumMonthlyPayment
    currentBalance = monthlyUnpaidBalance + monthlyUnpaidBalance * monthlyInterestRate
    print('Month: ' + str(currentMonth))
    print('Minimum monthly payment: %.2f' % minimumMonthlyPayment)
    print('Remaining balance: %.2f\n' % currentBalance)
    currentMonth += 1
    totalPaid += minimumMonthlyPayment

print('Total paid: %.2f' % totalPaid)
print('Remaining balance: %.2f' % currentBalance)
