name = input("Введіть своє ім'я: ")
print("Приємно познайомитися,", name,"!")
while True:
    request = input(name+': ')
    request = request.lower()
    if request == 'хай'or request == 'доброго' or request == 'вітаю' or request == 'привіт':
        print('БОТ: Доброго вечора, я бот з України!')
    if request == 'як справи?' or request == 'що робиш?' or request == 'чим займаєшся?':
        print('БОТ: Вчусь програмувати на Python!')
    if request == 'фільм' or request == 'серіал' or request == 'кіно':
        print('БОТ: Соррі що втручаюсь, не знаю про що йдеться мова, але подивись фільм ""Банди Нью-Йорка"", він просто бомба!')
    if request == 'бот рекомендує фільм' or request == 'бот рекомендує серіал':
        print('БОТ: Соррі що втручаюсь, не знаю про що йдеться мова, але подивись фільм ""Банди Нью-Йорка"", він просто бомба!')
    if request == 'бувай' or request == "добре" or request == "до зустрічі":
        exit('БОТ: Побачимось у мережі, Coming soon.')