import platform


def pyt_v():
    '''Выводит кортеж с версией питона'''
    print("Твоя версия Python в кортеже")
    return platform.python_version_tuple()


def bits_32_or_64():
    '''Выводит разрядность ОС'''
    print("Твоя разрядность")
    return platform.architecture()


def processor():
    '''Выводит информацию по процессору'''
    print("Твой процессор")
    return platform.processor()


def pyth_impl():
    '''Выводит реализацию питона'''
    print("Реализация питона")
    return platform.python_implementation()


def pyth_version_str():
    '''Выводит версию питона в строке'''
    print("Версия питона в строке")
    return platform.python_version()


def display_conditions():
    func_list = [pyt_v, bits_32_or_64,
                 processor, pyth_impl, pyth_version_str, ]
    print('''
 __________________________________________________
|              _______                     ___    |
|  |\     /|  |         |       |   |     /   \   |
|  | \   / |  |         |       |   |    /     \  |
|  |  \ /  |  |○○○○○○   |○○○○○○c|   |○○○○       | |
|  |   ○   |  |         |       |   |    \     /  |
|  |       |  |_______  |       |   |     \___/   |
|                                                 |
|_________________________________________________|
    ''')

    for index, funct in enumerate(func_list, 1):
        print(index, "––>", funct.__name__)
        help(funct)

    print()


if __name__ == "__main__":
    print("functions.py - Запущена как самостоятельный модуль.")

    print()
    display_conditions()
    print()

    func_list = [pyt_v, bits_32_or_64,
                 processor, pyth_impl, pyth_version_str, ]

    for funct in func_list:
        print(funct())
else:
    print("functions.py - Запущена как импортируемый модуль.")
