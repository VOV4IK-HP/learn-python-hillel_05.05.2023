name = input("Введіть своє ім'я: ")
print("Приємно познайомитися,", name,"!")
while True:
    request = input(name+': ')
    request = request.lower()
    if 'хай' in request or 'привіт' in request or 'доброго' in request or 'вітаю' in request:
        print('БОТ: Доброго вечора, я бот з України!')
    if 'як' in request or 'що' in request or 'чим' in request:
        print('БОТ: Вчусь програмувати на Python!')
    if 'фільм' in request or 'серіал' in request or 'кіно' in request:
        print('БОТ: Подивись фільм ""Банди Нью-Йорка"", він просто бомба!')
    if 'бот рекомендує' in request or 'круто' in request or 'ого' in request:
        print('БОТ: Соррі що втручаюсь, не знаю про що йдеться мова,\n але подивись фільм ""Банди Нью-Йорка"", він просто бомба!')
    if 'бувай' in request or "добре" in request or "до зустрічі" in request:
        exit('БОТ: Побачимось у мережі, Coming soon.')