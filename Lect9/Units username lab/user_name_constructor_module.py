def user_name_constructor(firstname: str, lastname: str):
    '''
    Функция которая принимает два параметра(Имя, Фамилия) в виде строки и
    проверят соответсвуют ли введенные в нее параметры, в конце
    выводит результат, которым будет являться Имя Фамилия
    '''
    # Проверяем являются ли введенные параметры в одном из них 0.
    if len(firstname) == 0 or len(lastname) == 0 or \
            not all([len(firstname), len(lastname)]):
        return "is empty"
    # Проверяем являются ли введенные параметры пробелом.
    if firstname.isspace() or lastname.isspace() or \
            all([firstname.isspace(), lastname.isspace()]):
        return "is space"
    # Проверяем есть ли внутри параметров цифры.
    if not all([firstname.strip().isalpha(), lastname.strip().isalpha()]):
        return "is number inside"
    # Распечатываем результат функции если все ок.
    return " ".join([firstname.strip(), lastname.strip()])


if __name__ == '__main__':
    print('user_name_constructor запущена сама по себе')
else:
    print('user_name_constructor импортирована')    
