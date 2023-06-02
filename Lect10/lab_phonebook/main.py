from Miakish_Sviataslau_lab_phonebook import PhoneNumbersList, PhoneNumberError


# Определяем экземпляр класса.
my_phone_book = PhoneNumbersList()

# Выводим текущий список номеров.
print(my_phone_book.get_numbers_list())

# Cписок номеров для добавления.
nubmers_to_add = ['372235523', "375296865610", "1235235Gsd"]

# Итерируемся по списку номеров.
for number in nubmers_to_add:
    try:
        # Если номер добавился выводим True.
        print(my_phone_book.add_number(number))
        # Если в номере содержались ошибки выводим номер и сообщение об ошибке.
    except PhoneNumberError as err:
        print(f'{err.phone} --> {err.msg}')


# Выводим список с добавленными номерами
print(my_phone_book.get_numbers_list())

if __name__ == '__main__':
    print('main.py запущена сама по себе')
else:
    print('main.py импортирована')
