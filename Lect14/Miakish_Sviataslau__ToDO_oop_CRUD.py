import sqlite3


class PriorityExc(Exception):
    '''
    Класс ошибки приоритета.
    '''
    def __init__(self, head = "ToDoPriorityError", message = "Bad priority"):
        super().__init__(message)
        self.head = head
        self.message = message


class IdExc(Exception):
    '''
    Класс ошибки ID.
    '''
    def __init__(self, head = "ToDoIDError", message = "Bad ID!"):
        super().__init__(message)
        self.head = head
        self.message = message


class NameExc(Exception):
    '''
    Класс ошибки наименования.
    '''
    def __init__(self, head = "ToDoTaskNameError", message = "Bad name!"):
        super().__init__(message)
        self.head = head
        self.message = message


class Todo:
    '''
    Класс, который позвоялет нам работать с БД, с помощью
    различных методов.
    '''
    def __init__(self):
        '''
        Конструктор класса, который открывает соеденение с БД.
        '''
        self.conn = sqlite3.connect('todo.db')
        self.c = self.conn.cursor()
        self.create_tasks_table()
        
    def create_tasks_table(self):
        '''
        Метод, который создает таблицу tasks если такой нет в БД.
        '''
        self.c.execute('''CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMATY KEY,
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

        if res != None: 
            raise NameExc(message = "This name already in tasks!")

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
        find = False

        rows = self.c.execute('''SELECT id, name, priority FROM tasks;''')

        for row in rows:
            if row[1] == self.task_name:
                find = True
                return row
        else:
            return None
            
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

        self.c.execute('''DELETE FROM TASKS WHERE ID = ?;''',(self.numid,))
        self.conn.commit()    

    def close_connection(self):
        '''Метод который закрывает соединение с БД.'''

        print('Connection was closed, bye')
        self.c.close()
        self.conn.close()

def show_main_task():
            # Выводим меню для пользователя
            print('''
                1. Show Tasks
                2. Add Task
                3. Change Priority
                4. Delete Task
                5. Show menu
                0. Exit        
                ''')
            
def menu_controller(put = 0):
    '''Контролер который выполняет методы, 
    которые передал пользователь по значению. '''

    if put == 1:
        # Показываем задачи которые записаны в БД.
        app.show_tasks()
    
    elif put == 2:
        try:
            app.add_task()
        except NameExc as e:
            print(e.message)
        except PriorityExc as e:
            print(e.message)
        except:
            print("Something goes bad ")
        else:
            print("The task was added successfully.")
        finally:
            print()
    
    elif put == 3: 
        # Обновляем приоритет.
        try:
            app.update_priority()
        except PriorityExc as e:
            print(e.message)
        except IdExc as e:
            print(e.message)
        except:
            print("Soms bad")
        else:
            print('The task was updated successfully.')
        finally:
            print() 

    elif put == 4:
        # Удаляем задачу.
        try:
            app.delete_task()
        except IdExc as e:
            print(e.message)
        except:
            print("Soms bad")
        else:
            print('The task was updated successfully.')
        finally:
            print()

    elif put == 5:
        # Выводим меню программы.
        show_main_task()
    
    elif put == 6:
        # Закрываем соеденение с БД и выходим из программы.
        app.close_connection()
        
    
def main():
    '''Основная программа, для использования пользователем.'''
    show_main_task()
    put = int(input("Enter what you want 1, 2, 3 , 4 , 5 or 0 for exit: "))
    while put != 0:
        try:
            if put in [1, 2 , 3, 4, 5, 6]:
                menu_controller(put)         
        except:
            print("Bad operation, enter the right numbers")
        
        put = int(input("Enter what you want 1, 2, 3 , 4 ,5 or 0 for exit: "))
    else:
        menu_controller(6)
        
        
if __name__ == "__main__":
    print('main.py запущена сама по себе')
    app = Todo()
    main()
else:
    print('main.py импортирована')    
                