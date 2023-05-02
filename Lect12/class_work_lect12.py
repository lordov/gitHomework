# class Demo:
#     class_var = 'shared variable'

# d1 = Demo()
# d2 = Demo()

# print(Demo.class_var)
# print(d2.class_var)
# print(d1.class_var)


# class Duck:
#     counter = 0
#     species = 'duck'

#     def __init__(self, height, weight, sex):
#         self.height = height
#         self.weight = weight
#         self.sex = sex
#         Duck.counter += 1

#     def walk(self):
#         pass

#     def quack(self):
#         print('quacks')

# class Chicken:
#     species = 'chicken'

#     def walk(self):
#         pass

#     def cluck(self):
#         print('clucks')

# duckling = Duck(height = 10, weight = 3.4, sex = "male")
# drake = Duck(height = 25, weight = 3.7, sex = "male")
# hen = Duck(height = 20, weight = 3.4, sex = "female")

# chicken = Chicken()

# print("So many ducks were born:", Duck.counter)

# for popultry in duckling, drake, hen, chicken:
#     print(popultry.species, end=" ")
#     if popultry.species == "duck":
#         popultry.quack()
#     elif popultry.species == 'chicken':
#         popultry.cluck()

# class Phone:
#     counter = 0

#     def __init__(self, number):
#         self.number = number
#         Phone.counter += 1

#     def call(self, number):
#         message = f'Calling {number} using own number {self.number}'
#         return message


# class FixedPhone(Phone):
#     last_SN = 0

#     def __init__(self, number):
#         super().__init__(number)
#         FixedPhone.last_SN += 1
#         self.SN =  f'FP - {FixedPhone.last_SN}'


# class MobilePhone(Phone):
#     last_SN = 0

#     def __init__(self, number):
#         super().__init__(number)
#         MobilePhone.last_SN += 1
#         self.SN =  f'MP - {MobilePhone.last_SN}'


# print('Total number of phone devices created:', Phone.counter)
# print('Creating 2 devices')
# fphone = FixedPhone('2-90-80')
# mphone = MobilePhone("3756562610")

# print("Total number of phone devices created:", Phone.counter)
# print('Total number of mobile phones created:', MobilePhone.last_SN)

# print(fphone.call('16543-9523'))

# print(f"Fixed phone recevied {fphone.SN}")
# print(f"Mobile phone recevied {mphone.SN}")


class Vehicle:
    def __init__(self, kind, weight):
        self.kind = kind
        self.weight = weight

    def __add__(self, other):
        return self.weight + other.weight
    
mustang = Vehicle("car", 3532)
pirus = Vehicle('car', 3101)

print(f"Total ewight of m an p: {mustang + pirus}")
