# class a:
#     pass

# print(a.__dict__)

# class g:
#     def __init__(self, j, k, name):
#         self.j = j
#         self.k = k
#         self.name = name

# gg1 = g(777, 999, "PEtr")

# print(gg1.__dict__)

# class f:
#     a = 11
#     def __init__(self, a):
#         self.a = a

# ff = f(55)

# print(ff.__dict__)
# print(f.__dict__)


# class Classy:
#     def method(self, par):
#         print('Hello', par)

# f = Classy()
# print(f.method(1))

# class Classy:
#     varia = 2
#     def method(self):
#         print(self.varia, self.var)

# obj = Classy()
# obj.var = 3 
# print(obj.method())


# # ЧТО-то НА ПОЛЕЗНОМ
# class User:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age


# Petia = User("Petia", 33)
# Kate = User("Kate", 23)

# li = []        
# for i in range(3):
#     name = input("n -- >")
#     age = int(input("A -->"))
#     li.append(User(name, age))

# for inst in li:
#     print(inst.name, inst.age)

# class MyClass:
#     pass

# obj = MyClass()
# obj.a = 1
# obj.b = 2
# obj.i = 3
# obj.ireal = 3.5
# obj.integer = 5
# obj.z = 5

# def incIntsI(obj):
#     for name in obj.__dict__.keys():
#         if name.startswith('i'):
#             val = getattr(obj, name)
#             if isinstance(val, int):
#                 setattr(obj, name, val + 3)

# print(obj.__dict__)
# incIntsI(obj)
# print(obj.__dict__)

# # Функция __str__ для вывода экзэмпляров(и не только) через принт.
# class Star:
#     def __init__(self, name, galaxy):
#         self.name = name
#         self.galaxy = galaxy
#     def __str__(self):
#         return f'{self.name} {self.galaxy}'

# sun = Star("Sun", "Mlky way")
# print(sun)

# class Vehicle:
#     pass


# class LandVehicle(Vehicle):
#     pass

# class TrackedVehicle(LandVehicle):
#     pass



# for cls1 in [Vehicle, LandVehicle, TrackedVehicle]:
#     for cls2 in [Vehicle, LandVehicle, TrackedVehicle]:
#         print(issubclass(cls1, cls2))
#     print()        


# # ОБЫЧНОЕ НАСЛЕДОВАНИЕ ИЛИ ОДИНАРНОЕ.
# class Super:
#     def __init__(self, name):
#         self.name = name
    

#     def __str__(self):
#         return "my name is " + self.name
    

# class Sub(Super):
#     def __init__(self, name):
#         super().__init__(name)


# obj = Sub("andy")

# print(obj)


# # МНОЖЕСТВЕННОЕ НАСЛЕДОВАНИЕ
# class SuperA:
#     var_a = 10
#     def fun_a(self):
#         return 11


# class SuperB:
#     var_b = 20
#     def fun_b(self):
#         return 21


# class Sub(SuperA, SuperB):
#     pass


# obj = Sub()

# print(obj.var_a, obj.fun_a())
# print(obj.var_b, obj.fun_b())

# # ПОЛИМОРФИЗЩМ


# class one:
#     def do_it(self):
#         print("do_it from one")
    
#     def doanything(self):
#         self.do_it()


# class Two(one):
#     def do_it(self):
#         print("do_it from Two")


# One = one()
# two = Two()

# print(One.doanything(), two.doanything())


# try:
#     1/1
# except ZeroDivisionError:
#     print("except")
# else:
#     print("else")
# finally:
#     print("finally")

# # FINALLY
# def reciprocal(n):
#     try:
#         n = 1 / n
#     except ZeroDivisionError:
#         print('Division failed')
#         n = None
#     else:
#         print("Everything went fine")
#     finally:
#         print("It's time to say goodbye")
#         return n

# print(reciprocal(2))
# print(reciprocal(0))

# def sum_(*args): #  Функция принимает на вход кортеж.
#     result = None

#     try:
#         return sum(args)
#     except TypeError:
#         return "error"
#     finally:
#         print("run before the method returns")

# print(sum_(1, 2, 5))

# try:
#     i = int("Hello!")
# except Exception as e:
#     print(e)
#     print(e.__str__())



# err = 15
# try:
#     print(err)
#     1 / 0 
# except ZeroDivisionError as err:
#     print(err)
#     err = 22 
#     print(err)
# print(err)