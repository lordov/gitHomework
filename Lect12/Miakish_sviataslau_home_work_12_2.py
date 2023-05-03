class Timer:
    '''
    Конструктор класса который принимает 3 
    целочисленных значения: часы , минуты, секунды.
    '''
    def __init__(self, hours:int = 0, minutes:int = 0, seconds:int = 0):
        self.hours = hours
        self.minutes = minutes
        self.seconds =  seconds
    
    def __str__(self):
        '''
        Метод который позволяет распечатать принятые значения.
        '''
        return f'{self.hours}:{self.minutes}:{self.seconds}'
    
    def __add__(self, other):
        total_hours = self.hours + other.hours
        total_minutes = self.minutes + other.minutes
        total_seconds = self.seconds + other.seconds
    
        if total_seconds >= 60:
            total_minutes += 1
            total_seconds -= 60
            if total_minutes >= 60:
                total_hours += 1
                total_minutes -= 60
        return Timer(total_hours, total_minutes, total_seconds)
    
    def __sub__(self, other):
        total_hours = self.hours - other.hours
        total_minutes = self.minutes - other.minutes
        total_seconds = self.seconds - other.seconds
    
        if total_seconds < 0:
            total_minutes -= 1
            total_seconds += 60
            if total_minutes < 0:
                total_hours -= 1
                total_minutes += 60
                if total_hours < 0:
                    total_hours, total_minutes, total_seconds = 0, 0, 0
        return Timer(total_hours, total_minutes, total_seconds)
    

tim1 = Timer(21, 58, 50)
tim2 = Timer(2, 59, 53)
 
print(tim1 + tim2)
print(tim1 - tim2)


if __name__ == '__main__':
    print('Miakish_Sviataslau_home_work_12_2.py запущена сама по себе')
else:
    print('Miakish_Sviataslau_home_work_2_2.py импортирована')  
