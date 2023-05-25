# ВАРИАНТ 1
# Программа считает сумму введенных пользователем чисел
# до тех пор, пока пользователь не введет "0"

total = 0
number = float(input('Enter your number:\n> '))
# прибавлять числа, пока не введут ноль
while number != 0:
    total += number
# ввести еще одно число
    number = float(input('Enter another number:\n> '))

print('Your total:', total)


