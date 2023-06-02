import requests
import json


def get_all_tasks():
    res = requests.get("http://localhost:5000/todos")
    if res:
        print("Ok", json.loads(res.text), res.status_code)


def get_one_tasks():
    ids = input("Put id --> ")
    res = requests.get(f"http://localhost:5000/todos/todo{ids}")
    if res:
        print("Ok", json.loads(res.text), res.status_code)


def delete_one_tasks():
    ids = input("Put id --> ")
    res = requests.delete(f"http://localhost:5000/todos/todo{ids}")
    if res:
        print("Ok", json.loads(res.text), res.status_code)


def post_one_tasks():
    text_message = input("Put text message --> ")
    res = requests.post(f"http://localhost:5000/todos", json={"task": text_message})
    if res:
        print("Ok", json.loads(res.text), res.status_code)


def put_one_tasks():
    ids = input("Put id --> ")
    text_message = input("Put text message --> ")
    res = requests.put(
        f"http://localhost:5000/todos/todo{ids}", json={"task": text_message}
    )
    if res:
        print("Ok", json.loads(res.text), res.status_code)


def main():
    message = """
    Введи номер операции:
    1 - вывести все задачи
    2 - вывести одну задачу по id
    3 - УДАЛИТЬ одну задачу по id
    4 - создать задачу
    5 - обновить задачу по ud 
    0 - выход
    """

    operation = int(input(message))

    while operation != 0:
        if operation == 1:
            get_all_tasks()
        elif operation == 2:
            get_one_tasks()
        elif operation == 3:
            delete_one_tasks()
        elif operation == 4:
            post_one_tasks()
        elif operation == 5:
            put_one_tasks()
        else:
            print("Не понимаю")
        operation = int(input(message))


if __name__ == "__main__":
    main()
