# Home work 4.0.

# Функция сложения.
def plus(val1, val2):
    print(f'{val1} + {val2} = {val1 + val2}')


# Функция вычитания.
def minus(val1, val2):
    print(f'{val1} - {val2} = {val1 - val2}')


# Функция деления.
def divide(val1, val2):
    print(f'{val1} / {val2} = {val1 / val2}')


# Функция умножения.
def multi(val1, val2):
    print(f'{val1} * {val2} = {val1 * val2}')

# Создаем калькулятор.


def calculator():
    print("Выберете операцию")

# Запрашиваем у пользователя оператор.
    operator = input("(+ - / *) или exit для выхода ")

    if operator not in ["+", "-", "/", "*", "exit"]:
        print("Не вернный ввод")
        return

    # Проверяем какой оператор ввел пользователь и производим вычисления.
    while operator != "exit":
        num1, num2, = int(input("Введите первое число ")), int(
            input("Введите второе число "))
    # Сумма.
        if operator == "+":
            plus(num1, num2)
    # Вычитание.
        elif operator == "-":
            minus(num1, num2)
    # Деление.
        elif operator == "/":
            divide(num1, num2)
    # Умножение.
        elif operator == "*":
            multi(num1, num2)

        operator = input(
            "Введите один оператор из (+ - / *) или exit для выхода ")

    else:
        print("Bye, bye")


calculator()
