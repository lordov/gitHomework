import json


class Vehicle:
    def __init__(self, reg_number, year_of_prod, passegner, mass):
        self.reg_number = reg_number
        self.year_of_prod = year_of_prod
        self.passenger = passegner
        self.mass = mass


class MyEncoder(json.JSONEncoder):
    def default(self, veh):
        if isinstance(veh, Vehicle):
            return veh.__dict__
        else:
            return super().default(self, veh)


class MyDecoder(json.JSONDecoder):
    def __ini__(self):
        json.JSONDecoder.__init__(self, object_hook=self.decode_vehicle)

    def decode_vehicle(self, veh):
        return Vehicle(**veh)


def main():
    print('''
    What can i do for you?
    1 - produce a JSON string describing a vehicle
    2 - decode a JSON string into vehicle data
    ''')

    answr = ''
    while answr not in ['1', '2']:
        answr = input('Your choice: ')
    if answr == '1':
        rn = input('Registration number: ')
        yop = int(input('Year of production: '))
        psg = input('Passenger [y/n]: ').upper() == 'Y'
        mss = float(input('Vehicle mass: '))
        vehicle = Vehicle(rn, yop, psg, mss)
        print('Resulting JSON strin is: ')
        print(json.dumps(vehicle, cls=MyEncoder))
    else:
        json_str = input('Enter vehicle JSON string: ')
        try:
            new_car = json.loads(json_str, cls=MyDecoder)
            print(new_car)
        except TypeError:
            print("The JSON string doesn't decribe a valid vehicle")
    print('Done')


if __name__ == "__main__":
    print('main.py запущена сама по себе')
    main()
else:
    print('main.py импортирована')
