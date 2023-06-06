# Перевод секунд в формат чч.мм.сс

s = int(input("Введите количество секунд:\n> "))
seconds = s


def convert(seconds):
    seconds %= 24 * 3600
    hours = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    print("Полученное значение в формате чч.мм.сс:")
    print(f'{hours}:{minutes}:{seconds}')


convert(seconds)
