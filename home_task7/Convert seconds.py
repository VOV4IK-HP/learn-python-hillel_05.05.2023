# Функция переводит введенное число секунд в формат чч.мм.сс
s = int(input("Введите количество секунд:\n> "))
seconds = s


# прописываем правила рекалькуляции в часы, минуты, секунды
def convert(seconds):
    seconds = s
    seconds %= 24 * 3600
    hours = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    print("Полученное значение в формате чч.мм.сс:")
    print(f'{hours}:{minutes}:{seconds}')


# выводим конвертируемые данные (секунды)
if __name__ == '__main__':
    qty_seconds = seconds
    convert(qty_seconds)
