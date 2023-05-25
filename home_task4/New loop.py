# Программа считает сумму введенных пользователем чисел,
# пока пользователь не введет "sum"
EXIT_COMMAND = 'sum'

total = 0
# запуск вечного цикла
while True:
    # пользователь делает ввод
    number = input('Enter your number (type `sum` to leave):\n> ')
    # проверка на команду 'sum'
    if number == 'sum':
        # при получении 'sum' вывод суммарного результата
        print('=' * 20)
        print('Your total:', total)
        # завершение работы цикла
        break
    # если ввод не равен 'sum' переход в данное условие
    else:
        try:
            # проверяем на предмет ошибки переменной 'number'  конвертацией в 'float'
            # при ошибке переход в 'except' и вызов тела 'except'
            number = float(number)
            # прибавляем числа к имеющемуся значению
            total += number
        except Exception:
            print('You entered a letter or symbol! Enter a number!')