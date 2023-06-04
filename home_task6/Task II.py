import math

def read_triangle_parameters(user_prompt, lower_bound=0, upper_bound=9999999):
    """
    Отвечает за считывание у пользователя строки и конвертации её в число
    Считывание происходит до тех пор, пока введённая строка не удовлетворит все условия
    :param user_prompt: комментарий для контекста пользователю
    :param lower_bound: нижнее допустимое значение
    :param upper_bound: верхнее допустимое значение
    :return: считанное у пользователя число в рамках допустимых значений
    """
    # тело функции на отступе
    while True:
        number = input(f'{user_prompt}\n>')
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

print(type(read_triangle_parameters), read_triangle_parameters)
a = read_triangle_parameters('Введите сторону треугольника a=')
b = read_triangle_parameters('Введите сторону треугольника b=')
c = read_triangle_parameters('Введите сторону треугольника b=')


print(a, fuel_liter_price, age)