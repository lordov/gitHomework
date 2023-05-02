# # Создаем класс-исключение унаследованное от Exception.
# class PhoneNumberError(Exception):
#     # Создаем конструктор класс.
#     def __init__(self, phone, message):
#         self.phone = phone
#         self.msg = message


# class PhoneNumbersList:
#     # Создаем пременную класса с пустым списком.
#     __numbers_lsit = []
#     # Констркутор класса.
#     def __init__(self):
#         self.number  = 0

#     # Метод класса который возвращает список номеров.
#     def get_numbers_list(self):
#         return PhoneNumbersList.__numbers_lsit
    
#     def add_number(self, number: str):
#         '''
#         Метод проверяет есть ли в переданном ему списке значений буквы или символы,
#         если такове имеются то номер добавлен в список не будет, и выведет ошибку с
#         указанием номера, который и вызвал ошибку, в противном случае методо вернет TRUE.
#         '''
#         if number.isnumeric():
#             PhoneNumbersList.__numbers_lsit.append(number)
#             return True
        
#         raise PhoneNumberError(number, 'contain not numbers')
    


# if __name__ == '__main__':
#     print('Miakish_Sviataslau_lab_phonebook.py запущена сама по себе')
# else:
#     print('Miakish_Sviataslau_lab_phonebook.py импортирована')    
    