from os import strerror


class PizzaError(Exception):
    def __init__(self, pizza, message):
        Exception.__init__(self, message)
        self.pizza = pizza


class MuchChesseError(Exception):
    
    def __init__(self, pizza, cheese, message):
        super().__init__(pizza, message)
        self.cheese = cheese


class Pizzeria:
    # Текущий список пицц.
    list_of_pizzas = ["margarita", "capricciosa", "calzone", "mafia"]
    def __init__(self):
        self.pizza = ''
        self.__pizza_to_remove = ''
    
    def add_pizza(self, pizza):
        '''
        Метод, который добовляет пиццу в меню пицц, если такая пицца 
        уже есть, то метод сообщит что пицца уже в меню.
        '''
        self.pizza = pizza
        if self.pizza in Pizzeria.list_of_pizzas:
            raise PizzaError(self.pizza, 'pizza already in menu')
        
        # Добовляем пиццу и выводим сообщение об этом.
        Pizzeria.list_of_pizzas.append(self.pizza)
        print(self.pizza, ": Succesfully added to menu !")
        print("Menu of pizzas:", Pizzeria.list_of_pizzas)

    def remove_pizza(self, pizza):
        '''
        Метод, который удаляет пиццу из меню пицц, если такая пицца
        существует в меню, если такой пиццы нет в меню, метод сообщит об этом.
        '''
        self.__pizza_to_remove = pizza
        if self.__pizza_to_remove not in Pizzeria.list_of_pizzas:
            raise PizzaError(self.pizza, "pizza not exist!")
        
        # Удаляем пиццу из списка и выводим сообщение об этом.
        Pizzeria.list_of_pizzas.remove(self.__pizza_to_remove)
        print(self.__pizza_to_remove, ": Succesfully removed from list of pizza!")
        print("List of pizzas", Pizzeria.list_of_pizzas)


class Order(Pizzeria):
    '''
    Класс для оформления заказа с последующей
    записью заказа в файл.
    '''
    def __init__(self):
        super().__init__()
        self.orders = {}
        self.counter = 1
        self._fo = open('pizzas_order.txt', 'wt', encoding = "utf-8")
        self._fo.close()

    def make_order(self, pizza, cheese):
        self.mpizza = pizza
        self.__cheese = cheese

        if self.mpizza not in Pizzeria.list_of_pizzas:
            raise PizzaError(self.mpizza, "no such pizza!")

        if self.__cheese > 100:
            raise MuchChesseError(self.mpizza, self.__cheese, "too much cheese")
        # Записываем заказ в виде словарая.
        self.orders.update({self.counter : f'{self.mpizza} : {self.__cheese}'})
        print('Order:', self.counter, self.orders[self.counter], ': Has succesfully created!')

        try:
            # Открываем файл в режиме "добавить в конец".
            self._fo = open('pizas_order.txt', 'at')
            result_order = f'{self.counter} {self.mpizza } with {self.__cheese} cheese \n\n'
            # Записываем результат заказа.
            self._fo.write(result_order)
            # Закрываем файл.
            self._fo.close()
        except IOError as err:
            print('Error - ', strerror(err.errno)) 
        else:
            print("Succesfully written to file!")
            self.counter += 1


order = Order()

def main():
    # Добавляем пиццу.
    for pz in ['peperoni', "margarita", "mafia"]:
        try:
            order.add_pizza(pz)
        except PizzaError as pe:
            print(f'{pe} : {pe.pizza}' )

    print()
    print()
    # Удаляем пиццу.
    for pz in ["calzone"]:
        try:
            order.remove_pizza(pz)
        except PizzaError as pe:
            print(f'{pe} : {pe.pizza}')
    print()
    print()

    # Заказываем пиццу.
    for (pz, ch) in [('peperoni', 0), ("margarita", 110), ("mafia", 20)]:
        try:
            order.make_order(pz, ch)
        except MuchChesseError as tmch:
            print(tmch, ':', tmch.cheese)
        except PizzaError as pe:
            print(f'{pe} : {pe.pizza}')
        print()
        print()



if __name__ == '__main__':
    print('pizzeria_L11.py запущена сама по себе')
    main()
else:
    print('pizzeria_L11.py импортирована')  
