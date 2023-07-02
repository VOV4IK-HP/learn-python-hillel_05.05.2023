from random import choices, randint, random


class Cat:
    # тело класса
    # self - обязательный параметр методов класса (метод - это функция в классе), который должен быть первым
    def __init__(self, name: str, age: int, breed: str, preferred_food: set):
        """
        Класс кот
        :param name: имя
        :param age: возраст
        :param breed: порода
        :param preferred_food: предпочитаемая еда
        """
        print('Создан объект класса Cat')
        self.name = name
        self.age = age
        self.breed = breed
        self.preferred_food = preferred_food

        # голоден ли кот
        self.hungry = True
        # сколько часов гулял
        self.hours_outdoors = 0

    def __str__(self):
        starting_str = f"{self.breed.capitalize()} {self.name}, {self.age} "
        if self.age == 1:
            starting_str += "год"
        elif 2 <= self.age <= 4:
            starting_str += "года"
        else:
            starting_str += "лет"
        starting_str += f", часов гулял: {self.hours_outdoors}, голоден: {self.hungry}"
        return starting_str

    def bark(self, count: int):
        if count > 0:
            barking_str = '-'.join(["мяу"] * count).capitalize()
            print(f"{self.name} мяукает: {barking_str}!")

    def eat(self, food: str):
        if self.hungry:
            if food in self.preferred_food:
                print(f"{self.name} кушает {food}")
                self.hungry = False
            else:
                print(f"{self.name} такое не ест: {food}")
                self.bark(randint(1, 5))
        else:
            print(f"{self.name} не голоден")

    def walk(self, alone: bool):
        """
        Кот гуляет
        :param alone: если True, то кот гуляет один, если False - то с хозяином
        Если кот гулял суммарно больше 1 часа, то он проголодался
        :return: если с хозяином - повышается настроение (у хозяина), если сам - None
        """
        if alone:
            hours = randint(2, 6)
            with_str = "сам"
        else:
            hours = randint(1, 3)
            with_str = "с хозяином"
        print(f"{self.name} гуляет {with_str} {hours} часа")
        self.hours_outdoors += hours
        if self.hours_outdoors > 1:
            self.hungry = True
        return "Хорошее настроение!" if not alone else None


if __name__ == '__main__':
    # Как передавать значения в класс и делать объекты разными
    d = Cat('Барсик', 2, "персидский кот", {'овощи', 'корм'})
    x = Cat('Томас', 4, "дворняга", {'мясо', 'рыба'})
    y = Cat('Феликс', 3, "камышовый кот", {'рыба', 'мясо', 'вискас'})
    z = Cat('Марсик', 5, "сиамский кот", {'мясо', 'корм', 'сало'})
    cats = [d, x, y, z]
    print(d.name, x.name, y.name, z.name)
    print(d)
    print(x)
    print(y)
    print(z)

    potential_food = ['каша', 'хлеб', 'рыба', 'борщ', 'сало', 'торт', 'яблоко', 'корм', 'овощи']
    print('Обычный день в жизни одного кота :)')
    print('-' * 20)
    for cat in cats:
        events_for_cat = randint(1, 8)
        for _ in range(events_for_cat):
            if random() > 0.5:
                print(f'Кормим {cat.name}')
                for random_food in choices(potential_food, k=3):
                    cat.eat(random_food)
            else:
                if random() > 0.5:
                    result = cat.walk(alone=True)
                else:
                    result = cat.walk(alone=False)
                print(f'После прогулки хозяин понял, что: {result}')
        print(f'Прошел день для: {cat}')
        print('=' * 20)
