import math


def read_user_number(user_prompt, lower_bound=0, upper_bound=9999999):
    '''
    :param user_prompt: комментарий для контекста пользователю
    :param lower_bound: нижнее допустимое значение
    :param upper_bound: верхнее допустимое значение
    :return: считанное у пользователя число в рамках допустимых значений
    '''
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


# находим периметр треугольника
def perimeter(a, b, c):
    return sum((a, b, c))


# находим площадь треугольника
def area(a, b, c):
    p = perimeter(a, b, c) / 2
    s = math.sqrt(p * (p - a) * (p - b) * (p - c))
    return s


if __name__ == '__main__':
    a = read_user_number('Введите длину первой стороны: a')
    b = read_user_number('Введите длину второй стороны: b')
    c = read_user_number('Введите длину третьей стороны: c')
    print('Периметр треугольника:')
    print(perimeter(a, b, c))
    print('Площадь треугольника:')
    print(area(a, b, c))
