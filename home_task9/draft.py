import os

# имя файла
FILENAME = "notes.txt"
# определяем пустой список
notes = list()

for i in range(3):
    note = input("Add a notes " + str(i + 1) + ": ")
    notes.append(note + "\n")

# запись списка в файл
with open(FILENAME, "a") as file:
    for note in notes:
        file.write(note)

# считываем сообщения из файла
print("Read notes")
with open(FILENAME, "r") as file:
    for note in file:
        print(note, end="")
