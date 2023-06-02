def minus(num1, num2):
    '''Функция для вычитания между num1 и num2.

    num1 - целое или дробное число.
    num2 - целое или дробное число.
    '''

    return num1 - num2


def plus(num1, num2):
    '''Функция для суммы  num1 и num2.

    num1 - целое или дробное число.
    num2 - целое или дробное число.
    '''

    return num1 + num2


def multi(num1, num2):
    '''Функция для умножения между a и b.

    num1 - целое или дробное число.
    num2 - целое или дробное число.
    '''

    return num1 * num2


def dev(num1, num2):
    '''Функция для деления a на b.

    num1 - целое или дробное число.
    num2 - целое или дробное число.
    '''

    return num1 / num2


def cond_list():
    li = [plus.__doc__, minus.__doc__, multi.__doc__, dev.__doc__,]
    for i, func_name in enumerate(li, 1):
        print('Введи цифру', i, 'для того чтобы воспользоваться:')
        print(func_name)

    print('Введи цифру', 0, 'для того чтобы воспользоваться:\n \
          Функция для вывода доступных операций.')
    print()
    print('Введи цифру', -1, 'для того чтобы воспользоваться:\n \
          Завершения работы программы.')
    
def main():

    cond_list()
    operator = int(input("Введи номер операции:"))

    while operator != -1:

        if operator == 0:
            cond_list()
        
        num1 = int(input('Введите первое число --> '))
        num2 = int(input('Введите второе число --> '))

        if operator == 1:
            print(plus(num1, num2))
        elif operator == 2:
            print(minus(num1, num2))
        elif operator == 3:
            print(multi(num1, num2))
        elif operator == 4:
            print(dev(num1, num2))
        operator = int(input("Введи номер операции:"))

    exit()


if __name__ == '__main__':
    print("main.py - Запущена как самостоятельный модуль.")
    main()
else:
    print("main.py - Запущена как импортируемый модуль.")      
