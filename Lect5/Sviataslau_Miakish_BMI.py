# BMI PROJECT.

# Приветствуем пользователя.
print("""
#================================#
| Добро пожаловать в программу   |
| для    вычисления      ИМТ!    |
| Если хотите узнать свой ИМТ    |
| Введите всего  2   значения    |
| Вес (кг)  и   рост (м.см)      |
| Для выхода введите два раза -1 |
#================================#
""")

# Cоздаем функцию вычисления ИМТ.


def bmi(weight="", height=""):
    '''Формула вычисления ИМТ и условия проверки.'''
    if weight <= 0 or height <= 0 \
            or weight > 200 or height > 2.:
        return "Введи другое значение"
    imt = weight / height ** 2
    print(f"Ваш ИМТ {imt}")
    if imt <= 16.:
        print("Выраженный дефицит массы тела")
    elif imt <= 18.5:
        print("Недостаточная (дефицит) масса тела")
    elif imt <= 25.:
        print("Норма")
    elif imt <= 30.:
        print("Избыточная масса тела (предожирение)")
    elif imt <= 35.:
        print("Ожирение 1 степени")
    elif imt <= 39.9:
        print("Ожирение 2 степени")
    elif imt >= 40.:
        print("Ожирение 3 степени")
    return imt


# Запрашиваем данные у пользователя.
weig, heig = float(input("Введите ваш вес:")), float(
    input("Введите ваш рост:"))
# Запускаем цикл обработки данных и выводим результат.
while weig != -1.0 and heig != -1.0:
    bmi(weig, heig)
    weig, heig = float(input("Введите ваш вес:")), float(
        input("Введите ваш рост:"))
else:
    print("Спасибо что воспользовались программой!")
