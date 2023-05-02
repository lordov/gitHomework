# Home work 6.1
import time
import datetime
import show_tasks_module
import enter_task_module


# Пустой список, в который будут добавляться все задачи пользователя.
task_list = []   

# Основная функция, которой пользователь будет передавать значения
# для взаимодействия с программой. 
def main():
    # Фиксируем начало работы с программой.
    starttime = datetime.datetime.now()
    # Выводим окно с условиями.
    show_tasks_module.cond_diplay()
    # Запускаем цикл взаимодействия пользователя с программой.
    while main != 0:
        cond_number = int(input("Выберите номер операции:"))
        if cond_number ==1:
            enter_task_module.enter_task(task_list)
        elif cond_number == 2:
            show_tasks_module.disp_task(task_list)
        elif cond_number == 3:
            show_tasks_module.cond_diplay()
        elif cond_number == 0:
            # Фиксируем время выхода из программы.
            endtime = datetime.datetime.now()
            # Выводим пользователю количество потраченного времени в программе.
            print(f"Пока! Ты потратил {endtime - starttime} ")
            time.sleep(3)
            exit()
        else:
            print("Не понимаю, выбери операцию")


if __name__ == "__main__":
    print("main.py запущен, как самостоятельный модуль(программа).")
    main()
else:
    print("main.py запущен, как встроенный модуль (программа) в другю программую.")
            