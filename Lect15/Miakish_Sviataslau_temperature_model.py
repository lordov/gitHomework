import logging
import random


FORMAT = '%(levelname)s - %(message)s'

class BatterySimulation:
    '''Класс, который включает в себя коннструктор класса, который
    принимает в качестве экземпляра логгер, и метода, который симулирует
    перегрев телефона.
    '''
    def __init__(self, logger):
        self.logger = logger
    
    def simulate_last_hour(self):
        '''Метод, который симулирует перегрев телефона и
        в зависимости от температуры печатает ошибку.
        '''
        for minute in range(1, 60 + 1):
            temperature = random.randint(20, 40)

            if temperature < 30:
                self.logger.debug(f'{temperature} C')
            elif temperature >= 30 and temperature <= 35:
                self.logger.warning(f'{temperature} C')
            elif temperature > 35:
                self.logger.critical(f'{temperature} C')  
            else:
                raise Exception('Temperture out of range.')

def main():
    logger = logging.getLogger('Battery.temperture')

    handler = logging.FileHandler('battery_temperature.log', mode='w')
    handler.setLevel(logging.DEBUG)

    formatter = logging.Formatter(FORMAT)
    handler.setFormatter(formatter)

    logger.addHandler(handler)

    simulation = BatterySimulation(logger)
    simulation.simulate_last_hour()


if __name__ == '__main__':
    print('temperature_model запущена сама по себе')
    main()
else:
    print('temperature_model импортирована')  
