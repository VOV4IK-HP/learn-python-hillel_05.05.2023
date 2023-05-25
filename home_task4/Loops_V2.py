# ВАРИАНТ 2
# Цикл считает сумму введенных пользователем чисел
# до тех пор, пока пользователь не введет "sum", выход "exit" или "quit"

sum1 = 0
while True:
    value = input('Enter your number:\n> ')
    if value.isdigit(): # проверка строки на число
        sum1 += int(value) # здесь его уже переводим
    if value == "sum":
        print('Your total:', sum1)
    elif value == 'exit' or value == 'quit':
        break
print('Completed')