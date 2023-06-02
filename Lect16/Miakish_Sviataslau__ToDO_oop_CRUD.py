import sqlite3
import logging
import configparser
import csv
import json


config = configparser.ConfigParser()
config.read('config.ini')


FORMAT = '%(name)s:%(levelname)s:%(asctime)s:%(message)s'

logger = logging.getLogger(__name__)

handler = logging.FileHandler('ToDo.log', mode='a')
handler.setLevel(logging.CRITICAL)

formatter = logging.Formatter(FORMAT)
handler.setFormatter(formatter)

logger.addHandler(handler)


class PriorityExc(Exception):
    '''
    Класс ошибки приоритета. В котором есть логирование,
    чтобы при вызове ошибок сразу записывалось все в файл.
    '''

    def __init__(self, head="ToDoPriorityError", message="Bad priority"):
        super().__init__(message)
        self.head = head
        self.message = message
        logger.critical(f'{self.head, self.message}')


class IdExc(Exception):
    '''
    Класс ошибки ID.В котором есть логирование,
    чтобы при вызове ошибок сразу записывалось все в файл.
    '''

    def __init__(self, head="ToDoIDError", message="Bad ID!"):
        super().__init__(message)
        self.head = head
        self.message = message
        logger.critical(f'{self.head, self.message}')


class NameExc(Exception):
    '''
    Класс ошибки наименования.В котором есть логирование,
    чтобы при вызове ошибок сразу записывалось все в файл.
    '''

    def __init__(self, head="ToDoTaskNameError", message="Bad name!"):
        super().__init__(message)
        self.head = head
        self.message = message
        logger.critical(f'{self.head, self.message}')


class MyEncoder(json.JSONEncoder):
    '''Encode to JSON.'''

    def default(self, w):
        if isinstance(w, Todo):
            return w.__dict__
        return super().default(w)


class MyDecoder(json.JSONDecoder):
    def __init__(self):
        json.JSONDecoder.__init__(self, object_hook=self.decode_who)

    def decode_who(self, d):
        return Todo(**d)


class Todo:
    '''
    Класс, который позвоялет нам работать с БД, с помощью
    различных методов.
    '''

    def __init__(self):
        '''
        Конструктор класса, который открывает соеденение с БД.
        '''
        self.conn = sqlite3.connect(config['db']['name'])
        self.c = self.conn.cursor()
        self.create_tasks_table()

    def create_tasks_table(self):
        '''
        Метод, который создает таблицу tasks если такой нет в БД.
        '''
        self.c.execute('''CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        priority INTEGER NOT NULL
        );''')

    def add_task(self):
        '''
        Метод, который позвоялет добавлять задачу в таблицу task.
        '''

        self.task_name = input('Enter task name: ')
        if len(self.task_name) < 5 or self.task_name.isspace():
            raise NameExc

        res = self.find_task(self.task_name)

        if res is not None:
            raise NameExc(message="This name already in tasks!")

        self.priority = int(input("Enter priority: "))
        if self.priority < 1 or self.priority > 100:
            raise PriorityExc

        self.c.execute('INSERT INTO tasks (name, priority) VALUES (?, ?)',
                       (self.task_name, self.priority))
        self.conn.commit()

    def find_task(self, task_name):
        '''
        Метод, который проверят есть ли задача с таким же именем
        которое ввел пользователь
        '''
        self.task_name = task_name

        for row in self.c.execute('''SELECT id, name, priority FROM tasks;'''):
            if row[1] == self.task_name:
                return row

    def show_tasks(self):
        '''
        Метод, который показывает какие текущие задачи есть в БД.
        '''
        print("Task table contain the next tasks...")
        print("ID  | Task name | Priority")
        for row in self.c.execute('''SELECT * FROM tasks;'''):
            print(row)

    def update_priority(self):
        '''
        Метод который обновляет приоритет в БД по ID.
        '''
        self.priority = int(input("Enter preferable priority: "))
        if self.priority < 1 or self.priority > 100:
            raise PriorityExc

        self.numid = int(input("Enter id: "))
        if self.numid < 1:
            raise IdExc

        self.c.execute('UPDATE tasks SET priority = ? WHERE id = ?;',
                       (self.priority, self.numid))
        self.conn.commit()

    def delete_task(self):
        '''
        Метод который удаляет задачу по Id в БД.
        '''
        self.numid = int(input('Enter id which you want to delete:'))
        if self.numid < 1:
            raise IdExc

        self.c.execute(
            '''SELECT COUNT(*) FROM TASKS WHERE ID = ?;''', (self.numid,))
        rows = self.c.fetchone()[0]

        if rows == 0:
            raise IdExc

        self.c.execute('''DELETE FROM TASKS WHERE ID = ?;''', (self.numid,))
        self.conn.commit()

    def close_connection(self):
        '''Метод который закрывает соединение с БД.'''

        print('Connection was closed, bye')
        self.c.close()
        self.conn.close()

    def task_export_csv(self, filename):
        '''Метод, который экспортирует данные из таблицы tasks в файл СSV.'''
        self.filename = filename
        with open(self.filename, 'w', newline='') as csvfile:
            writer_csv = csv.writer(
                csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            self.c.execute('SELECT id, name, priority FROM tasks')
            rows = self.c.fetchall()
            for row in rows:
                writer_csv.writerow(row)

    def export_tasks_to_json(self, filename_json):
        '''
        Метод для экспорта данных из таблицы tasks в JSON-файл.
        '''
        self.filename_json = filename_json
        # Retrieve all rows from tasks table
        with open(self.filename_json, 'w') as json_file:
            self.c.execute('SELECT * FROM tasks;')
            tasks = []
            for row in self.c.fetchall():
                task = {
                    'id': row[0],
                    'name': row[1],
                    'prirority': row[2]
                }
                tasks.append(task)

            json.dump(tasks, json_file, cls=MyEncoder)


def show_main_task():
    # Выводим меню для пользователя
    print('''
                1. Show Tasks
                2. Add Task
                3. Change Priority
                4. Delete Task
                5. Show menu
                6. Export to CSV.
                7. Export to json.
                0. Exit
                ''')


def main():
    '''Основная программа, для использования пользователем.'''
    app = Todo()

    show_main_task()
    # Запрашиваем у пользователя ввод.
    try:
        put = int(
            input("Enter what you want 1, 2, 3 , 4 , 5, 6, 7 or 0 for exit: "))
    except:
        put = -1
    while put != 0:
        if put == 1:
            # Показываем задачи которые записаны в БД.
            app.show_tasks()

        elif put == 2:
            try:
                app.add_task()
            # Я решил все-таки оставить уведомление пользователю об ошибках.
            except NameExc as e:
                print(e.message)
            except PriorityExc as e:
                print(e.message)
            except:
                print("Invalid input. Please enter a valid option")
            else:
                print(f"Name : {app.task_name}\npriority: {app.priority} \
                    \nWas added successfully.")
        elif put == 3:
            # Обновляем приоритет.
            try:
                app.update_priority()
            except PriorityExc as e:
                print(e.message)
            except IdExc as e:
                print(e.message)
            except:
                print("Invalid input. Please enter a valid option")
            else:
                print('The task was updated successfully.')
        elif put == 4:
            # Удаляем задачу.
            try:
                app.delete_task()
            except IdExc as e:
                print(e.message)
            except:
                print("Invalid input. Please enter a valid option")
            else:
                print('The task was updated successfully.')
        elif put == 5:
            # Выводим меню программы.
            show_main_task()
        elif put == 6:
            filename = input(
                'Введите имя файла в который вы хотите сохранить бд:')
            # Экспортируем в файл CSV.
            app.task_export_csv(filename + '.csv')
        elif put == 7:
            filename_json = input(
                'Введите имя файла в который вы хотите сохранить бд:')
            # Выводим меню программы.
            app.export_tasks_to_json(filename_json + '.json')
        else:
            print("Invalid input. Please enter a valid option")
        try:
            put = int(
                input("Enter what you want 1, 2, 3 , 4 ,5, 6 or 0 for exit: "))
        except:
            put = -1
    else:
        app.close_connection()


if __name__ == "__main__":
    print('main.py запущена сама по себе')
    main()
else:
    print('main.py импортирована')
