from .animal import Animal



class Cat(Animal):
    # init так же называют конструктором класса
    def __init__(self, name: str, age: int, say_word='Мyauuu!'):
        """
        Класс отвечает за симуляцию животного кот
        """
        super().__init__(
            name=name,
            age=age,
            say_word=say_word,
            preferred_food={'корм', 'мясо', 'рыба'},
        )
        self.animal_type = 'Кошка'

    def treat(self, hours: int) -> str:
        """
        Ухаживая за кошкой должное количество времени, мы получаем хорошее настроение
        :param hours: время ухаживания
        :return: настроение или ничего
        """
        if hours > 1:
            print(f'Вы ухаживаете за {self} {hours} часов и получаете хорошее настроение')
            return 'Хорошее настроение'
        print(f'Вы ухаживаете за {self} {hours} часов.')
        return ''
