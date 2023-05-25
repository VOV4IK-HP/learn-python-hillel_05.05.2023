# task 1
# name = input('What is your name?\n')
# print ("Hello", name)

# task 1
#name = input('What is your name?\n-> ')
#surname = input('What is your surname?\n-> ')
#print ("Hallo,", name, surname)

# task 3
#dialog = input('What do you call a bear with no teeth?\nA gummy bear!')
#print(dialog)

# task 4
#num1 = int(input('Please enter your first number \n-> '))
#num2 = int(input('Please enter your second number \n-> '))
#answer = num1 + num2
#print('The total is', answer)

# task 5
#num1 = int(input('Please enter your first number \n-> '))
#num2 = int(input('Please enter your second number \n-> '))
#num3 = int(input('Please enter your third number \n-> '))
#answer = (num1 + num2) * num3
#print('The total is', answer)

# task 6
#num1 = int(input('How many slices of pizza did you have? \n-> '))
#num2 = int(input('How many slices of pizza did you eat? \n-> '))
#num3 = num1 - num2
#print ("You have", num3, 'slices of pizza left!')

# task 7
#name = input('Please enter your name?\n-> ')
#age = int(input('Please enter your age?\n-> '))
#newAge = age + 1
#print(name, 'next birthday will be', newAge)

# task 8
#invoice = int(input('Please enter the total invoice amount\n-> '))
#number = int(input('Plese enter the number of people\n-> '))
#average = invoice / number
#print('Every people must pay:', average)

# task 9
#days = int(input('Please enter yor period of time in days\n-> '))
#hours = days * 24
#minutes = hours * 60
#second = minutes * 60
#print('In your period:')
#print(hours, 'hours')
#print(minutes, 'minutes')
#print(second, 'second')

# task 10
#kg = int(input('Please enter yor weight in kilograms\n-> '))
#pounds = kg * 2.204
#print('Your weight:\n->', pounds, 'pounds')

# task 11
#number_more = int(input('Please enter yor number more than 100\n-> '))
#number_less = int(input('Please enter yor number less than 10\n-> '))
#times = number_more // number_less
#print('Your less number fits into the larger one', times, 'times ')

# task 12
#num1 = int(input("Enter your first number: "))
#num2 = int(input("Enter your second number: "))
#if num1 > num2:
# print(num2)
#else:
# print(num1, num2)

# task 13
#num = int(input("Enter your number less than 20:\n-> "))
#if num >= 20:
# print('Too high')
#else:
# print('Thank you')

# task 14
#num = int(input("Enter your number between 10 and 20:\n-> "))
#if num >= 10 and num <= 20:
# print('Thank you')
#else:
# print('Incorrect answer')

# task 15
#color = input("Enter your favorite color:\n-> ")
#color = str.lower(color)
#if color == "red":
# print('I like red too')
#else:
# print('I do not like', color, 'I prefer red')

# task 16
#raining = input("It is raining?\n-> ")
#raining = str.lower(raining)
#if raining == "yes":
#    windy = input("It is windy?\n-> ")
#    windy = str.lower(windy)
#    if windy == "yes":
#        print('«It is too windy for an umbrella')
#    else:
#        print('Take your umbrella')
#else:
#    print('Enjoy your day')

# task 17
#age = int(input("Enter your age?\n-> "))
#if age >= 18:
#    print('You can vote')
#elif age == 17:
#    print('You can learn to drive')
#elif age == 16:
#    print('You can buy a lottery ticket')
#else:
#    print('You can go Trick-or-Treating')

# task 18
#num = int(input("Enter your number?\n-> "))
#if num < 10:
#    print('Too low')
#elif num >= 10 and num <= 20:
#    print('Correct')
#else:
#    print('Too high')

# task 19
#num = input("Enter 1, 2 or 3: ")
#if num == "1":
# print("Thank you")
#elif num == "2":
# print("Well done")
#elif num == "3":
# print("Correct")
#else:
# print("Error message")

# task 20
#name = input('What is your name?\n-> ')
#name = len(name)
#print(name)

# task 21
#firstname = input('What is your name?\n-> ')
#surname = input('What is your surname?\n-> ')
#name = firstname + ' ' + surname
#lenght = len(name)
#print(name)
#print(lenght)

# task 22
#firstname = input('What is your name in low register?\n-> ')
#surname = input('What is your surname in low register?\n-> ')
#name = firstname + ' ' + surname
#name = name.upper()
#print(name)

# task 22
#firstname = input("Enter your first name in lowercase: ")
#surname = input("Enter your surname in lowercase: ")
#firstname = firstname.title()
#surname = surname.title()
#name = firstname + " " + surname
#print(name)

#
'''EXIT_COMMAND = 'n'
num1 = float(input("Enter a number: "))
total = num1
again = "y"
while again == "y":
 num2 = float(input("Enter another number: "))
 total = total + num2
 again = input("Do you want to add another number? (y/n) ")
print("The total is ",total)'''

# program to calculate the sum of numbers
# until the user enters zero

"""total = 0
number = float(input('Enter your number:> '))
# add numbers until number is zero
while number != 0:
    total += number  # total = total + number
    # take integer input again
    number = float(input('Enter another number:> '))
print('=' * 20)
print('Your total:>', total)"""

'''BREAK_COMMAND = 0
total = 0 # общая сумма
while True: # бесконечный цикл
    x = float(input('Insert your number:\n-> ')) # каждая строка содержит число
    if x == 0: # нашли ноль
        break  # выходим из цикла
    total += x # суммируем
print(('Your total:'), total) # печатаем результат'''

sum1 = 0
while True:
    value = input('Enter your number:\n> ')
    if value.isdigit(): # проверка строки на число
        sum1 += int(value) # здесь его уже переводим
    if value == "sum":
        print('Your total:', sum1)
    elif value == 'exit' or value == 'quit':
        break
print('Completed')