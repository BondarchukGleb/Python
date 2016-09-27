# Paying debt off int a year

balance = float(input('Balance = '))
annualInterestRate = float(input('Annual interest rate = '))

months = 12
monthlyInterestRate = annualInterestRate / months
minimumFixedMonthlyPayment = 0
fixedMonthlyPayment = minimumFixedMonthlyPayment

currentBalance = balance
while currentBalance > 0:
    fixedMonthlyPayment += 10
    currentBalance = balance
    currentMonth = 1
    while currentMonth <= months:
        monthlyUnpaidBalance = currentBalance - fixedMonthlyPayment
        currentBalance = monthlyUnpaidBalance + monthlyUnpaidBalance * monthlyInterestRate
        currentMonth += 1

print('Lowest Payment: %.2f' % fixedMonthlyPayment)
