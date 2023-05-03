class MobilePhone:
    
    def __init__(self, number, status = False):
        '''
        Конструктор класса который принимает номер телефона и
        по умолчанию создает выключеный телефон.
        '''
        self.number = number
        self.status = status  
    
    def turn_on(self):
        '''
        Метод класса, который позволяет включить
        выключенный телефон, но он не включит телефон, который
        уже включен.
        '''
        if self.status == False:
            self.status = True  
            return f'mobile phone {self.number} is turned on'
        else:
            return 'mobile phone alredy on!'
        
    def turn_off(self):
        '''
        Метод класса, который позволяет выключить
        выключенный телефон, но он не выключит телефон, который
        уже выключен.
        '''
        if self.status == True:
            self.status = False
            return f'mobile phone {self.number} is turned off'
        else:
            return 'mobile phone alredy off'

    def call(self, cally):
        '''
        Метод класса, который позволяет позвонить если
        телефон включен, но он не позвонит если телефон
        уже выключен.
        '''
        if self.status == True:
            return f'calling {cally}'
        else:
            return f'The phone is OFF'  


mobile1 = MobilePhone('375296841633')
mobile2 = MobilePhone('375445750828')

print(mobile1.turn_on())
print(mobile2.turn_off())

print(mobile1.call('29080'))
print(mobile2.call('29080'))

print(mobile1.turn_on())
print(mobile2.turn_off())


def main():
    input_phone = int(input('How much numbers do you want to enter --> '))
    phone_list = []
    for i in range(input_phone):
        number_input = input('Enter the numbers: ')
        phone = MobilePhone(number_input)
        phone_list.append(phone)
    print('You have entered the following numbers:', [phone.number for ph in phone_list])
    
    
if __name__ == '__main__':
    print('mymobile_lab.py запущена сама по себе')
    main()
else:
    print('mymobile_lab.py импортирована')  
