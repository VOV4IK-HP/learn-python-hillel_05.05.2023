# Программа рассчитывает количество использованной электроэнергии и ее стоимость:
def read_user_number(user_prompt, lower_bound=0, upper_bound=9999999):
    """
    Отвечает за считывание у пользователя строки и конвертации её в число
    Считывание происходит до тех пор, пока введённая строка не удовлетворит все условия
    :param user_prompt: комментарий для контекста пользователю
    :param lower_bound: нижнее допустимое значение
    :param upper_bound: верхнее допустимое значение
    :return: считанное у пользователя число в рамках допустимых значений
    """
    while True:
        number = input(f'{user_prompt}\n> ')
        try:
            number = float(number)
            if lower_bound < number < upper_bound:
                # return - выход из функции с возвращением некоего значения
                return number
                # return  # return без ничего возвращает None
            else:
                print(f'Введите число в таких рамках: от {lower_bound} до {upper_bound}')
        except Exception:
            print(f'Не удалось получить число из ввода: "{number}", повторите пожалуйста попытку')

if __name__ == '__main__':
    old_data = read_user_number('Введите предыдущие показания счетчика, кВт')
    new_data = read_user_number('Введите текущие показания счетчика, , кВт')
    price = read_user_number('Введите тариф, грн/кВт')

    # Использовано кВт, грн.:
    used = new_data - old_data

    # Нужно оплатить, грн.:
    coast = used * price

    print('Использовано:')
    print(float(used), 'кВт.')
    print('Нужно оплатить:')
    print(float(coast), 'грн.')
