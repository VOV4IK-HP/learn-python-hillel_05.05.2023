str = input("Please, input your string\n-> ") # вводим слово или набор цифр/символов
str = str.lower() # переводим в нижний регистр
str = str.replace(",", "") # удаляем знаки препинания, пробелы, табуляции, перенос на нижнюю строку
str = str.replace(".", "")
str = str.replace("-", "")
str = str.replace(":", "")
str = str.replace(";", "")
str = str.replace(" ", "")
str = str.replace(" ", "")
str = str.replace(":", "")
str = str.replace("\n", "")
if str != str[::-1]: # -1 здесь шаг строки: от конца к началу
    print("It's not palindrome") # отрицательная проверка
else:
    print("It's palindrome") # положительная проверка