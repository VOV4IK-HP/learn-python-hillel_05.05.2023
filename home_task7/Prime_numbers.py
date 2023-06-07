# Функция проверяет введенное пользователем число, является ли оно простым числом (PRIME_NUMBER)


PRIME_NUMBER = ({2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97})

number = int(input("Введите ваше число:\n> "))

# Простое число имеет ровно два различных натуральных делителя, отлично от 1
# и делится без остатка только на 1 и на само себя.

def user_prime(number):
    if number == 2 or number == 3:
        return True
    if number % 2 == 0 or number < 2:
        return False
    for i in range(3, int(number ** 0.5) + 1, 2):
        if number % i == 0:
            return False
    return True


# Если число простое, пользователь получает ответ -> True
# Если число не является простым, пользователь получает ответ -> False
if __name__ == '__main__':
    check_number = number
    print(user_prime(check_number))
