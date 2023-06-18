# Функция добавляет новую заметку

def add_name():
    name = input("Enter a new notes: ")
    names.append(name)
    return names


# Сортировка от самой ранней до самой поздней:
def earliest_names():
    for x in names:
        print(x)
    print()


# Сортировка от самой поздней к самой ранней:
def latest_names():
    for x in sorted(names, reverse=True):
        print(x)
    print()


# Сортировка от самой длинной до самой короткой:
def longest_names():
    for x in sorted(names, key=lambda a: len(a)):
        print(x)
    print()


# Сортировка от самой короткой до самой длинной:
def shortest_names():
    for x in sorted(names, key=lambda a: len(a) - 1):
        print(x)
    print()


# Функция выводит "меню" варианты работы с программой, завершение программы:
def main():
    again = "y"
    while again == "y": # в случае ввода правильного варианта выводится запрошенное действие и меню
        print("1) Add a notes")
        print("2) Earliest a notes")
        print("3) Latest a notes")
        print("4) Longest a notes")
        print("5) Shortest a notes")
        print("6) Quit")
        selection = int(input("What do you want to do? "))
        if selection == 1:
            names = add_name()
        elif selection == 2:
            names = earliest_names()
        elif selection == 3:
            names = latest_names()
        elif selection == 4:
            names = longest_names()
        elif selection == 5:
            names = shortest_names()
        elif selection == 6:
            again = "n"
        else:
            print("Incorrect option: ") # в случае ввода не правильного варианта выводится фраза и меню


if __name__ == '__main__':
    names = []
    main()
