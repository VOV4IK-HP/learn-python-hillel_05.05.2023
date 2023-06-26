# Функция добавляет новую заметку
def add_name():
    name = input("Enter a new notes: ")
    names.append(name + '\n')
    return names


# Функция выводит "меню" варианты работы с программой, завершение программы:
def main():
    while True:  # в случае ввода правильного варианта выводится запрошенное действие и меню
        print("1) Add a notes\n"
              "2) Save & Exit")
        selection = int(input("What do you want to do? "))
        if selection == 1:
            list = add_name()
        elif selection == 2:
            quit()
        else:
            print("Incorrect option: ")  # в случае ввода не правильного варианта выводится фраза и меню


if __name__ == '__main__':
    names = []
    main()
