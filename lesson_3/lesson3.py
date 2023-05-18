#  Строки

example_string = "что-то"
print(example_string)

some_string = r'Файл на диске \n c:\''
print(some_string)


print("Что будет если мы" + "применим плюс к строке")
print('5' + '5')

my_variable = 7
my_variable = my_variable * 3
print(my_variable)
my_variable += 3
print(my_variable)

my_string = "Hello, "
print(id(my_string))
my_string = my_string + "something"
print(my_string)

a = b = 7
print(id(a))
print(id(b))

print("90" in "12345678910")

example_string = "12345678910"
#string[start:stop:step]
print(example_string[::-1])

a = 2
print(type(a))
b = "2"
print(type(b))

new_a = str(a)
print(type(new_a))

my_string = "2"
print(type(my_string))
my_new_string = int(my_string)
print(type(my_new_string))

s = "2"
print(s.isdigit())

st = "Привет, человек"
for letter in st:
    print(letter)

a = 7
my_string = f"Нас в группе {a} человек"
print(my_string)