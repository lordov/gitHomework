class Timer:
    '''
    Конструктор класса который принимает 3 
    целочисленных значения: часы , минуты, секунды.
    '''
    def __init__(self, hours:int = 0, minutes:int = 0, seconds:int = 0):
        self.hours, self.minutes, self.seconds = hours, minutes, seconds
    
    def __str__(self):
        '''
        Метод который позволяет распечатать принятые значения.
        '''
        return f'{self.hours}:{self.minutes}:{self.seconds}'
    
    # Метод который добавляет 1 секунду.
    def next_second(self):
        self.seconds += 1
        if self.seconds > 59:

            self.seconds = 0
            self.minutes += 1

            if self.minutes > 59:

                self.minutes = 0
                self.hours += 1

                if self.hours > 23:
                    self.hours = 0

    # Метод который отнимает 1 секунду.
    def prev_second(self):
        self.seconds -= 1
        if self.seconds < 0:

            self.seconds = 59
            self.minutes -= 1

            if self.minutes < 0:

                self.minutes = 59
                self.hours -= 1

                if self.hours < 0:
                    self.hours = 23

timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)      

if __name__ == '__main__':
    print('Miakish_Sviataslau_home_work_10_1.py запущена сама по себе')
else:
    print('Miakish_Sviataslau_home_work_10_1.py импортирована')  
