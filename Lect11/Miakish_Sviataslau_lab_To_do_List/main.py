import time
import datetime


class BadPriorityError(Exception):
    def __init__(self, priority, message):
        Exception.__init__(self, message)
        self.priority = priority


class BadIdError(Exception):
    def __init__(self, id, message):
        super().__init__(id, message)
        self.id = id


class BadNameError(Exception):
    def __init__(self, badname, message):
        super().__init__(badname, message)
        self.badname = badname


class Task:
    list_to_do = []

    def __init__(self):
        self.id = ''
        self.name = ''
        self.prior = ''
        self.time = ''

    def add_task(self, id, name, prior, time=0):
        '''Метод для добавления основных задач,
        состоящаяя из 3 циклов в которых мы спрашиваем у 
        пользователя: Номер задачи, Имя задачи, Приоритет здачи.
        В конце добовляем результат в список, который передаем функции.
        '''
        self.id = id

        if self.id < 1 or self.id > 30:
            raise BadIdError(
                self.id, "id может быть только в диапазоне от 1 до 30")

        self.name = name

        if len(self.name) < 5:
            raise BadNameError(self.name, "Введите другое имя")

        self.prior = prior

        if self.prior < 1 or self.prior > 100:
            raise BadPriorityError(self.prior,
                                   "приоритет может быть только в диапазоне от 1 до 100")

        # Фиксируем время, когда задача была записана.
        self.time = datetime.datetime.now()

        # Объединяем данные о задаче в словарь и добавляем его в список задач.
        task_dict = {'id': self.id, 'name': self.name,
                     'prior': self.prior, 'time': self.time}
        Task.list_to_do.append(task_dict)

        print(f"ID № {self.id}, Имя {self.name}, Приоритет № {self.prior},\
 дата добавления {self.time} - успешно добавлены\n")

    def show_task(self):
        for i, task in enumerate(self.list_to_do):
            print(f"Задача №{i+1}: ID - {task['id']}, Имя - {task['name']},\
 Приоритет - {task['prior']}, Дата добавления - {task['time']}")


task, kekl = Task(), Task()
task.add_task(1, "Badly1", 5)
kekl.add_task(10, "goodlo", 15)
kekl.add_task(15, "go1243dlo", 14)
print(kekl.show_task())


def main():
    '''
    Основная функция. 
    Пользователь будет передавать значения
    для взаимодействия с программой. 
    '''
    # Выводим окно с условиями.
    cond_diplay()

    # Пустой список, в который будут добавляться все задачи пользователя.
    task_list = []

    # Запускаем цикл взаимодействия пользователя с программой.
    cond_number = int(input("Выберите номер операции:"))

    while cond_number != 0:
        if cond_number == 1:
            try:
                enter_task(task_list)
            except:
                print("Что-то пошло не так.")
        elif cond_number == 2:
            disp_task(task_list)
        elif cond_number == 3:
            cond_diplay()
        else:
            print("Не понимаю, выбери операцию")

        cond_number = int(input("Выберите номер операции:"))


if __name__ == "__main__":
    print("Я запущена сама по себе, как самостоятельный модуль(программа).")
    # Фиксируем начало работы с программой.
    starttime = datetime.datetime.now()
    # Запускаем программу
    main()
    # Фиксируем время выхода из программы.
    endtime = datetime.datetime.now()
    # Выводим пользователю количество потраченного времени в программе.
    print(f"Пока! Ты потратил {endtime - starttime} ")
    time.sleep(3)
else:
    print("Я запущена не сама по себе, как встроенный модуль (программа) в другю программую.")
