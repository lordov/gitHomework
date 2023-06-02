# Cоздаем класс.
class Stack:
    # Конструктор класса, который присваивает каждому,
    # новому экзэмпляру класса пустой список.
    def __init__(self):
        self.__stack_list = []

    def push(self, val):
        '''
        Метод push, который позволяет добавлять в списки экзэмпляров значения.
        '''
        self.__stack_list.append(val)

    def pop(self):
        '''
        Метод pop, который позволяет удалять последнее значение в списках экзэмпляра.
        '''
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val

# Создаем второй класс наследуемый от класса Stack.


class CountingStack(Stack):
    # Создаем конструктор класса.
    def __init__(self):
        Stack.__init__(self)
        self.__counter = 0

    # Метод класса, который будет возвращать количество итераций.
    def get_counter(self):
        return self.__counter

    def pop(self):
        '''
        Метод класса, который удаляет последнее значение из списка,
        и считает количество удаленных значений.
        '''
        val = Stack.pop(self)
        self.__counter += 1
        return val


stk = CountingStack()
for i in range(50):
    stk.push(i)
    stk.pop()
print(stk.get_counter())
