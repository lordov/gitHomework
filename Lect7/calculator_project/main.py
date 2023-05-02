from packages.calculator.math_func import summa, subtraction, divide, multi
from packages.calculator.show_condition_module import cond_list


def main():

    cond_list()
    operator = int(input("Введи номер операции:"))

    while operator != -1:

        if operator == 0:
            cond_list()
        else:  
            number1 = int(input('Введите первое число --> '))
            number2 = int(input('Введите второе число --> '))

            if operator == 1:
                print(summa(number1, number2))
            elif operator == 2:
                print(subtraction(number1, number2))
            elif operator == 3:
                print(multi(number1, number2))
            elif operator == 4:
                print(divide(number1, number2))
            operator = int(input("Введи номер операции:"))

    exit()


if __name__ == '__main__':
    print("main.py - Запущена как самостоятельный модуль.")
    main()
else:
    print("main.py - Запущена как импортируемый модуль.")      
