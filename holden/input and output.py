userFirst = input('what is your name?')
userLast = input('what is your last name?')
userBirthyear = input('what year were you born?')
currentYear = 2019

greeting = 'Hello ' + userFirst + ' ' + userLast + '!'
print(greeting.center(50, '*'))
print('you were born in 0000' + str(userBirthyear))
print('the current year is {0:0.3e}'.format(currentYear))
print('you are', 2019 - int(userBirthyear), 'years old')
print('your mystical magic percentage is {0:0.4f}'.format(int(userBirthyear) / 2019 * 100))
print('Goodbye!'.rjust(50,' '))
