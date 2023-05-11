import csv


class PhoneContact:
    '''Класс телефонного контакта, который включает в себя конструктор класса,
    который принимает в качестве экзэмпляров класса, Имя и номер телефон.    
    '''
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone


class Phone():
    '''Класс телефон, который имеет телефонный список и два метода:
    загрузка контактов из csv файла и поиск загруженных контактов.
    '''
    def __init__(self):
        self.contacts = []
    
    def load_contacts_from_csv(self, file):
        '''
        Метод для импорта контактов из csv файла.
        '''
        with open(file, newline='') as csvfile:
            fieldnames = ['Name', 'Phone']
            reader = csv.DictReader(csvfile, fieldnames)

            for row in reader:
                self.contacts.append(PhoneContact(row['Name'], row['Phone']))

    def search_contacts(self, phrase):
        '''Метод для поиска контактов, которые есть в списке контактов в телефоне.'''
        count = 0
        for contact in self.contacts:
            if phrase.lower() in contact.name.lower() \
                or phrase in contact.phone:
                print(f'{contact.name}, {contact.phone}')
                count += 1
        if count == 0:
            print('No contact found!')


def show_menu():
    print('''
    1: Загрузить контакты.
    2: Найти контакт.
    ''')


def main():
    # Создаем экзепляр класса.
    phone = Phone()
    # Выводим меню.
    show_menu()
    # Запрашиваем пользовательский ввод.
    enter = int(input("Введи номер задачи."))
    while enter != 0:
        # Загружаем контакты в экземпляр класса.
        if enter == 1:
            phone.load_contacts_from_csv("contacts.csv")
            enter = int(input("Введи номер задачи."))
        # Поиск имени в списке контактов.
        elif enter == 2:
            phrase = input('Search contacts: ')
            if phrase != "exit":
                phone.search_contacts(phrase)
            else:
                enter = int(input("Введи номер задачи."))

   
if __name__ == '__main__':
    print('labphoneebook.py запущена сама по себе')
    main()
else:
    print('labphoneebook.py импортирована')  
