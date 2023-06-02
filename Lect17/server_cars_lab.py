import requests
import json


key_names = ["id", "brand", "model", "production_year", "convertible"]
key_widths = [10, 15, 10, 20, 15]
h_close = {"Connection": "Close"}
h_content = {"Content-Type": "application/json"}


def show_head():
    """Функция выводит таблицу данных.

    key_names это список названий колонок, а key_widths это список
    их соответствующей ширины. Названия выводятся по очереди, каждое
    подходящей ширины, после чего ставится разделитель "|".

    Args:
        Функция не принимает параметров.

    Returns:
        Возвращает заголовки выровненные по левому краю с
        указаной шириной.
    """
    for n, w in zip(key_names, key_widths):
        print(n.ljust(w), end="| ")
    print()


def show_empty():
    """Эта функция печатает пустую строку с
    вертикальными линиями для каждого элемента.
    """
    for w in key_widths:
        print("".ljust(2), end="| ")
    print()


def show_car(car: dict):
    """Функция принимает словарь "car" и выводит его содержимое в виде таблицы."""
    for n, w in zip(key_names, key_widths):
        print(str(car.get(n)).ljust(w), end="| ")
    print()


def show(json):
    """Функция, которая принимает список или словарь.

    Args:
        Принимает аргумент json, который может быть списком
        или словарем.

    Returns:
        Если json список, то для каждого элемета вызывается функция show_car,
        если json словарь то вызывается функция show_car, либо show_empty, если
        словарьь пуст. Так же в начале функции вызывается функция show_head.
    """
    show_head()
    if isinstance(json, list):
        for car in json:
            show_car(car)
    elif isinstance(json, dict):
        if json:
            show_car(json)
        else:
            show_empty()


def get_api():
    """Посылает GET запрос на http://localhost:3000/cars/{get_id}.

    При вызове она запрашивает у пользователя ввод ID(или оставляет поле пустым,
    чтобы получить полный список) и отправляет запрос на сервер
    с особым заголовком в h_close.

    Args:
        Функция не принимает параметры.

    Returns.
        Если запрос прошел успешно, функция выводит код успешного подключения (res=200),
        тип соединение и данные ответа(если код состояния равен 200).


    Raises:
        RequestException: Communication error.

    """
    try:
        get_id = str(
            input("Введите id или оставтье поле пустым для вывода полного списка:")
        )
        reply_get = requests.get(f"http://localhost:3000/cars/{get_id}")
        print(f"res={reply_get.status_code}")
        reply_get = requests.get(
            f"http://localhost:3000/cars/{get_id}", headers=h_close
        )
    except requests.RequestException:
        print("Communication error")
    else:
        print("Connection=" + reply_get.headers["Connection"])
        if reply_get.status_code == requests.codes.ok:
            show(reply_get.json())
        elif reply_get.status_code == requests.codes.not_found:
            print("Resource not found")
        else:
            print("Server error")


def delete_api():
    """Функция отправляет запрос HTTP DELETE на локальный адрес.

    Удаляет авто с предоставленным id_for_del. Если запрос прошел успешно,
    функция выводит код успешного подключения (res=200),
    тип соединение и данные ответа(если код состояния равен 200).

    Args:
        id_for_del: id авто для удаления

    Raises:
        RequestException: Communication error.
    """

    try:
        id_delet = input("Введите id для удаления:")
        # Метод DELETE.
        reply_delete = requests.delete(f"http://localhost:3000/cars/{id_delet}")
        print(f"res={reply_delete.status_code}")
        reply_delete = requests.get(f"http://localhost:3000/cars/", headers=h_close)
    except requests.RequestException:
        print("Communication error")
    else:
        print("Connection=" + reply_delete.headers["Connection"])
        if reply_delete.status_code == requests.codes.ok:
            show(reply_delete.json())
        elif reply_delete.status_code == requests.codes.not_found:
            print("Resource not found")
        else:
            print("Server error")


def post_api():
    """Посылает POST запрос на http://localhost:3000/cars/.

    Добавляет новые значения на сервере которые передает пользователь в параметре
    new_car в виде словаря с ключ: значения. Если запрос прошел успешно,
    функция выводит код успешного подключения (res=200), тип соединение и
    данные ответа(если код состояния равен 200).

    Args:
        new_car: словарь со значеиями авто.

    Raises:
        RequestException: Communication error.
    """
    try:
        # Костыль для True or False.
        conv = input("Является ли машина кабриолетом. True/False --> ")
        # Запрашиваем у пользователя данные.
        dict_input = {
            "id": int(input("Введите id:")),
            "brand": input("Введите бренд:"),
            "model": input("Введите Модель:"),
            "production_year": str(input("Введите год производства:")),
            "convertible": conv,
        }
        reply_post = requests.post(
            "http://localhost:3000/cars/",
            headers=h_content,
            data=json.dumps(dict_input),
        )
        print(f"res={reply_post.status_code}")
        reply_post = requests.get("http://localhost:3000/cars/", headers=h_close)
    except requests.RequestException:
        print("Communication error")
    else:
        print("Connection=" + reply_post.headers["Connection"])
        if reply_post.status_code == requests.codes.ok:
            show(reply_post.json())
        elif reply_post.status_code == requests.codes.not_found:
            print("Resource not found")
        else:
            print("Server error")


def put_api():
    try:
        what_updt = input("Введите id авто для обновления:")
        conv = input("Является ли машина кабриолетом. True/False --> ")
        update_dict = {
            "brand": input("Введите бренд:"),
            "model": input("Введите Модель:"),
            "production_year": str(input("Введите год производства:")),
            "convertible": conv,
        }
        reply_put = requests.put(
            f"http://localhost:3000/cars/{what_updt}",
            headers=h_content,
            data=json.dumps(update_dict),
        )
        reply_put = requests.get("http://localhost:3000/cars/", headers=h_close)
    except requests.RequestException:
        print("Communication error")
    else:
        print("Connection=" + reply_put.headers["Connection"])
        if reply_put.status_code == requests.codes.ok:
            show(reply_put.json())
        elif reply_put.status_code == requests.codes.not_found:
            print("Resource not found")
        else:
            print("Server error")


def show_task():
    print(
        """
    1: GET-Запрос -- Получить список авто.
    2: POST-Запрос -- Добавить авто.
    3: PUT-Запрос -- Обновить авто.
    4: DELETE-Запрос -- Удалить авто.
    5: Показать доступные задачи.
    0: Выход.
    """
    )


def main():
    # Выводим меню.
    show_task()
    # Запрашиваем номер задачи.
    try:
        user_input = int(input("Введите номер задачи:"))
    except ValueError:
        print("Неккоректный ввод. Введите целое число.")
        user_input = int(input("Введите номер задачи: "))
    while user_input != 0:
        if user_input == 1:
            get_api()
        elif user_input == 2:
            post_api()
        elif user_input == 3:
            put_api()
        elif user_input == 4:
            delete_api()
        elif user_input == 5:
            show_task()
        else:
            print("Неверный номер задачи. Попробуйте ещё раз")
        user_input = int(input("Введите номер задачи: "))


if __name__ == "__main__":
    print("Программа запущена самостоятельно")
    main()
else:
    print("Cars_client запущен как модуль")
