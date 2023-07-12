import os
import random


# Функция-генератор для чтения заметок из файла
def read_notes():
    filename = get_filename()
    if os.path.isfile(filename):
        with open(filename, 'r') as file:
            for line in file:
                yield line.strip()


# Функция-генератор для записи заметок в файл
def write_notes(notes):
    filename = get_filename()
    with open(filename, 'w') as file:
        for note in notes:
            file.write(note + '\n')


# Функция для получения имени файла
def get_filename():
    return 'notes.txt'


# Функция для добавления заметки
def add_note():
    note = input('Введите заметку: ')
    notes.append(note)


# Функция для вывода всех заметок
def show_all_notes():
    print('Все заметки:')
    for note in notes:
        print(note)


# Функция для вывода последних n заметок
def show_last_notes(n):
    print('Последние {} заметок:'.format(n))
    for note in notes[-n:]:
        print(note)


# Функция для вывода случайной заметки
def show_random_note():
    if notes:
        note = random.choice(notes)
        print('Случайная заметка:', note)
    else:
        print('Нет заметок')


# Функция для сохранения заметок и выхода из программы
def save_and_exit():
    write_notes(notes)
    print('Заметки сохранены. До свидания!')
    exit()


# Главная функция программы
def main():
    # Чтение заметок из файла (если есть)
    notes.extend(read_notes())

    while True:
        print('=== Меню ===')
        print('1. Добавить заметку')
        print('2. Вывести все заметки')
        print('3. Вывести последние заметки')
        print('4. Вывести случайную заметку')
        print('5. Сохранить и выйти')
        choice = input('Выберите действие: ')

        if choice == '1':
            add_note()
        elif choice == '2':
            show_all_notes()
        elif choice == '3':
            n = int(input('Сколько заметок вывести? '))
            show_last_notes(n)
        elif choice == '4':
            show_random_note()
        elif choice == '5':
            save_and_exit()
        else:
            print('Неверный ввод')


# Заметки
notes = []

# Запуск программы
main()
