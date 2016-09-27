# Paying debt off int a year using bisection search to make it more faster

balance = float(input('Balance = '))
annualInterestRate = float(input('Annual interest rate = '))

months = 12
monthlyInterestRate = annualInterestRate / months
monthlyPaymentLowerBound = balance / months
monthlyPaymentUpperBound = balance * (1 + monthlyInterestRate) ** months / months
fixedMonthlyPayment = (monthlyPaymentLowerBound + monthlyPaymentUpperBound) / 2

currentBalance = balance
while abs(currentBalance) > 0.01:
    currentMonth = 1
    currentBalance = balance
    while currentMonth <= months:
        monthlyUnpaidBalance = currentBalance - fixedMonthlyPayment
        currentBalance = monthlyUnpaidBalance + monthlyUnpaidBalance * monthlyInterestRate
        currentMonth += 1
    if currentBalance > 0:
        monthlyPaymentLowerBound = fixedMonthlyPayment
    else:
        monthlyPaymentUpperBound = fixedMonthlyPayment
    fixedMonthlyPayment = (monthlyPaymentUpperBound + monthlyPaymentLowerBound) / 2

print('Lowest Payment: %.2f' % fixedMonthlyPayment)
