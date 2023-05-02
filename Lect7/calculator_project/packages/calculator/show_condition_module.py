from packages.calculator.math_func import summa, subtraction, multi, divide


def cond_list():
    li = [summa.__doc__, subtraction.__doc__, multi.__doc__, divide.__doc__,]
    for i, func_name in enumerate(li, 1):
        print('Введи цифру', i, 'для того чтобы воспользоваться:')
        print(func_name)

    print('Введи цифру', 0, 'для того чтобы воспользоваться:\n \
          Функция для вывода доступных операций.')
    print()
    print('Введи цифру', -1, 'для того чтобы воспользоваться:\n \
          Завершения работы программы.')
    
    
if __name__ == '__main__':
    print("show_condition_module.py - Запущена как самостоятельный модуль.")
else:
    print("show_condition_module.py - Запущена как импортируемый модуль.")         
