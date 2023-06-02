class QueueError(Exception):
    def __init__(self, message):
        self.message = message


class Queue:
    def __init__(self):
        self.__queue_list = []

    def put(self, val):
        '''
        Метод push, который позволяет добавлять в списки экзэмпляров значения.
        '''
        self.__queue_list.append(val)

    def get(self):
        '''
        Метод pop, который позволяет удалять первое значение в списках экзэмпляра.
        '''
        if len(self.__queue_list) != 0:
            return self.__queue_list.pop(0)
        raise QueueError("Очередь пуста! Извелкать нечего")


def main():
    que = Queue()

    que.put(2)
    que.put("Carrot")
    que.put(False)
    try:
        for i in range(4):
            print(que.get())
    except QueueError as que:
        print(f'{que}')


if __name__ == '__main__':
    print('Miakish_Sviataslau_home_work_10_2.py запущена сама по себе')
    main()
else:
    print('Miakish_Sviataslau_home_work_10_2.py импортирована')
