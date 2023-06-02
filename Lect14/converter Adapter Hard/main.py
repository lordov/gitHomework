import sqlite3


class Task:
    def __init__(self, name: str, priority: float) -> None:
        self.name, self.priority = name, priority

    def __repr__(self) -> str:
        return f'Task({self.name}, {self.priority})'


class Todolist:
    def __init__(self) -> None:
        self.con = sqlite3.connect(
            "todolist.sqlite3", detect_types=sqlite3.PARSE_DECLTYPES
        )
        self.cur = self.con.execute(
            '''CREATE TABLE IF NOT EXISTS tasks(
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    t task)'''
        )

    def add_task(self, tsk: Task):
        try:
            self.cur.execute("INSERT INTO tasks(t) VALUES(?)", (tsk,))
        except:
            print("something goes wrong...")
        else:
            self.con.commit()

    def del_task(self, tid: int):
        try:
            self.cur.execute("DELETE FROM tasks WHERE id = ?", (tid,))
        except:
            print("Something goes wrong...")
        else:
            self.con.commit()

    def __repr__(self) -> str:
        self.st = "ID_|__TASK_NAME__|__PRIORITY__\n\n"

        for c in self.cur.execute('SELECT id, t FROM tasks'):
            self.st += f"{c[0]} | {c[1].name} | {c[1].priority}\n"

        return self.st

    def close(self) -> None:
        self.cur.close()
        self.con.close()


def adapt_point(task) -> str:
    return f'{task.name};{task.priority}'


def convert_point(s) -> Task:
    li = s.split(b";")
    name, priority = bytes.decode(bytes(li[0])), float(li[1])
    return Task(name, priority)


sqlite3.register_adapter(Task, adapt_point)
sqlite3.register_converter("task", convert_point)


def oper_input() -> int:
    try:
        put = int(input("1 add, 2 del, 3 show, 0 exit:"))
    except:
        print('Something goes wrong...')
    else:
        return put


def main() -> None:
    td = Todolist()

    put = oper_input()
    while put != 0:
        if put == 1:
            nm = input("Task name:")
            pr = input("Task priority:")
            tsk = Task(nm, pr)
            td.add_task(tsk)

        elif put == 2:
            tid = int(input("id -->"))
            td.del_task(tid)
        elif put == 3:
            print(td)

        put = oper_input()

    td.close()


if __name__ == "__main__":
    print('main.py запущена сама по себе')
    main()
else:
    print('main.py импортирована')
