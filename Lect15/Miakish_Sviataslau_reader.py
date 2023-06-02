import csv


def show_task():
    print('''1: Прочитать документ как список.
    2: Прочитать документ через ,
    3: Прочитать документ как словарь.
    4: Прочитать документ как словарь с заголовками столбцов.
    5: Прочитать только имена.
    6: Прочитать только номера.
    7: Показать список доступных задач. 
    0: Выход.
    ''')


def main():
    '''Функция, которая позволяет читать csv файл,
    разными способами от списков до словарей без заголовков 
    и с заголовками.
    '''
    show_task()
    enter = int(input('Введи номер задачи 1-7, 0 выход --> '))
    while enter != 0:
        if enter == 1:
            # Читаем документ как список.
            with open('contacts.csv', newline="") as csvfile:
                reader = csv.reader(csvfile, delimiter=",")
                for row in reader:
                    print(row)
        elif enter == 2:
            # Читаем документ как строки через ','.
            with open('contacts.csv', newline="") as csvfile:
                reader = csv.reader(csvfile, delimiter=",")
                for row in reader:
                    print(",".join(row))
        elif enter == 3:
            # Читаем документ как словарь.
            with open('contacts.csv', newline="") as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    print(row["Name"], ':', row["Phone"])
        elif enter == 4:
            # Читаем документ с указанием заголовков заголовками.
            with open('contacts.csv', newline="") as csvfile:
                filednames = ['Name', 'Phone']
                reader = csv.DictReader(csvfile, fieldnames=filednames)
                for row in reader:
                    print(row["Name"], ':', row["Phone"])
        # Прочитать только имена.
        elif enter == 5:
            with open('contacts.csv', newline="") as csvfile:
                filednames = ['Name', 'Phone']
                reader = csv.DictReader(csvfile, fieldnames=filednames)
                for row in reader:
                    print(row["Name"])
        # Прочитать только номера.
        elif enter == 6:
            with open('contacts.csv', newline="") as csvfile:
                filednames = ['Name', 'Phone']
                reader = csv.DictReader(csvfile, fieldnames=filednames)
                for row in reader:
                    print(row["Phone"])
        elif enter == 7:
            show_task()
        enter = int(input('Введи номер задачи 1-7, 0 выход --> '))
    else:
        print("Пока, пока!")


if __name__ == "__main__":
    print('main.py запущена сама по себе')
    main()
else:
    print('main.py импортирована')
