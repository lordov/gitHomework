# Home work 5.1

# Запрашиваем у пользователя номер года.
def leap(year):
    '''Функция которая вычисляет высокосный год или нет, а так же возвращает 
    ошибку, если год не в пределах Григорианского календаря.'''
    # Произвожу вычисления высокосный год или нет и вывожу результат. 
    if year % 4 != 0:
        return False
    elif year < 1582:
        return False   
    else:
        return True

print(leap(1900))


test_data = [1901, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
    yr = test_data[i]
    print(f'{yr} -->', end="")
    result = leap(yr)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")

# Home work 5.2

def BYN_to_USD(dollars):
    """Конвертирует BYN в USD."""
    usd = 2.9
    byn = dollars * usd
    return byn


def USD_to_BYN(rubels):
    """Конвертирует BYN в USD."""
    byn = 0.34
    byn = rubels * byn
    return byn


print(USD_to_BYN(725))
print(BYN_to_USD(250))

# Home work 5.3

import sys
print(sys.getrecursionlimit())

def factorial(number):
    if number == 0:
        return print(1)
    factor_val = 1
    for i in range(1, number + 1):
        factor_val *= i
    return print(factor_val)


factorial(1000)

# Homwe work 5.4

def febo(number):
    ''' Вычисляем числа Фибоначчи циклом for'''
    if number < 1 or \
    number == 3:
        return 1
    fib1, fib2 = 1, 1
    for i in range(2, number):
        fib1, fib2 = fib2, fib1 + fib2
    print(fib2)   


# Просим пользователя ввести число.
number = int(input("Введите число Фибоначчи:"))
# Используем функцию для вывода результата.
febo(number)
