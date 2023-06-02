class PizzaError(Exception):
    def __init__(self, pizza, message):
        Exception.__init__(self, message)
        self.pizza = pizza


class MuchChesseError(Exception):
    def __init__(self, pizza, cheese, message):
        PizzaError.__init__(self, pizza, message)
        self.cheese = cheese


class Pizzeria:
    '''
    Конструктор класса, который представляет из себя
    приватный список из трех пицц.
    '''

    def __init__(self):
        self.__pizza_list = ["margherita", "capricciosa", "calzone"]

    def make_pizza(self, pizza, chesse):
        '''
        Метод который принимает два значения
        и выводит сообщения об ошибке если значения
        не соответствуют условиям.
        '''
        self.pizza = pizza
        self.cheese = chesse
        if pizza not in self.__pizza_list:
            raise PizzaError(pizza, "no such pizza on the menu")
        if chesse > 100:
            raise MuchChesseError(pizza, chesse, "too much cheese")
        print("Pizza ready")


def main():
    # Создаем экземпляр класса
    pizza_test = Pizzeria()

    # Записываем значения в переменные.
    for (pz, ch) in [('calzone', 0), ("margherita", 110), ("mafia", 20)]:
        try:
            # Передаем записанные переменные в метод класса.
            pizza_test.make_pizza(pz, ch)
        except MuchChesseError as much:
            print(f'{much} : {much.cheese}')
        except PizzaError as pe:
            print(f'{pe} : {pe.pizza}')


if __name__ == '__main__':
    print('pizzeria.py запущена сама по себе')
    main()
else:
    print('pizzeria.py импортирована')
