# Task 1

print('Example output:')
print('\t1. Soup and salad')
print('\t2. Pasta with meat sauce')
print('\t3. Chef\'s special')

while True:
    number = int(input('Which number would you like to order? '))
    if number == 1:
        print('\t1. Soup and salad')
    elif number == 2:
        print('\t2. Pasta with meat sauce')
    elif number == 3:
        print('\t3. Chef\'s special')
    else:
        print('\tSorry, that is not a valid choice')
