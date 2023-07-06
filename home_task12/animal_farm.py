from animals import Dog, Hen, Cow, Cat
from random import choices, choice, randint

if __name__ == '__main__':
    animals = [
        Cat("Мурка", 1),
        Dog('Жучка', 3),
        Hen('Коко', 2),
        Cow('Милка', 5),
            ]

    available_food = ['сено', 'трава', "зерно", "пшено", "каша", "мясо", "кость", "тортик", "корм", "рыба"]

    what_we_got = list()
    what_we_lost = list()
    for animal in animals:
        animal.say()
        for food in choices(available_food, k=3):
            what_we_lost.append(food)
            animal.eat(food)
        if animal.hungry:
            print(f'{animal} голодает! Покормите ее.')
        what_we_got.append(animal.treat(randint(0, 5)))
        print('=' * 20)
        if animal.check:
            print(f'{animal} не проверяли у ветеринара! Проверьте ее.')
        what_we_got.append(animal.healthy(randint(0, 5)))


    print(f'Сегодня на ферме мы потратили: {", ".join(what_we_lost)} и получили {", ".join(what_we_got)}')
