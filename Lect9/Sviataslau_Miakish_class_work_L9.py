# try:
#     y = 1 / 0
# except ZeroDivisionError:
#     print("Ooooppss...")

# print("The End.")

# try:
#     y = 1 / 0
# except ArithmeticError:
#     print("Ooopss...2")
# print('The end.2')

# def bad_fun(n):
#     try:
#         return 1 / n
#     except ArithmeticError:
#         print ('Arithmetic Prolem!')
#     return None

# bad_fun(0)
# print("The End")


# def bad_func1(n):
#     return 1 / n

# try:
#     bad_func1(0)
# except ArithmeticError:
#     print("What happened? An exception was raised")

# print('The end')


# # Блок для обработки исключений с инстантным вызовом ошибки.
# def bad_fun(n):
#     raise ZeroDivisionError

# try:
#     bad_fun(0)
# except ArithmeticError:
#     print("WH??")

# def bad_fun(n):
#     try:
#         return n / 0
#     except:
#         print("I did it again!")
#         raise


# try:
#     bad_fun(0)
# except ArithmeticError:
#     print("I see!")

# print('The end')

# import math

# x = float(input("Enter a number: "))
# assert x >= 0.0

# x = math.sqrt(x)

# print(x)

# customer_price = 77
# discount = 0.05 if customer_price >= 100 else 10
# assert 0 < discount < 1, "Wrong discount"

# final_price = customer_price * (1 - discount)
# print(final_price)

# import traceback


# def is_odd_or_even(number):
#     return number % 2 == 0 # True or False


# def test_is_odd_or_even():
#     assert is_odd_or_even(2) == "True" , 'error case: 2'
#     assert is_odd_or_even(6) == False, 'error case: 3'
#     assert is_odd_or_even(20) == True
#     assert is_odd_or_even(0) == True
#     assert is_odd_or_even(-4) == True


# if __name__ == "__main__":
#     print("Тестиру  функцию в модуле, так как программа запущена сама по себе")
#     try:
#         test_is_odd_or_even()
#         print("Ок")
#     except AssertionError as err:
#         print(f"Не ок --> {err}")
#         tb = err.__traceback__
#         traceback.print_tb(tb)

# else:
#     print("Функция из модуля импортирована!")

# class thesimpleclass:
#     pass

# myfitstobject = thesimpleclass()
# print(type(myfitstobject))
# a = 100
# print(type(a))

# class Customer:
#     '''Created when new customer registers'''

#     def __init__(self, first_name:str, last_name:str, age:int = None):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#         self.full_name = f'{first_name} {last_name}'

# custumer = Customer('Joe', 'Adams', 25)
# another_customer = Customer('Maria', "Smith")

# class ExampleClass:
#     counter = 0
#     def __init__(self, val = 1):
#         self.first = val
#         ExampleClass.counter += 1

#     def set_second(self, val):
#         self.set_second = val

# example_object_1 = ExampleClass()
# example_object_2 = ExampleClass(2)

# example_object_2.set_second(3)

# example_object_3 = ExampleClass(4)
# example_object_3.third = 5 

# print(example_object_1.__dict__, example_object_1.counter)
# print(example_object_2.__dict__, example_object_2.counter)
# print(example_object_3.__dict__, example_object_3.counter)


# Переменную классу можно читать через экземпляр, но перезаписать только через класс,
# Если пытаться перезаписать через экхемпляр просто создастя пееменная с таким же именем вутри экземпляра.
# class MyClass:
#     class_attribute = 'Python is awesome!'

# foo = MyClass()
# bar = MyClass()

# print(foo.class_attribute)
# print(bar.class_attribute)
# foo.class_attribute = 'new value'
# print(foo.class_attribute)
# MyClass.class_attribute = '!!!'
# print(foo.class_attribute)
# print(bar.class_attribute)
# print(foo.__dict__)
# print(bar.__dict__)
# print(MyClass.__dict__)


# # WHAT IS A STACK.

# stack = []

# def push(val):
#     stack.append(val)


# def pop():
#     val = stack[-1]
#     del stack[-1]
#     return val

# push(3)
# push(2)
# push(1)

# print(pop())
# print(pop())
# print(pop())

# class Stack:
#     def __init__(self):
#         self.__stack_list = []

    
#     def push(self, val):
#         self.__stack_list.append(val)
    
    
#     def pop(self):
#         val = self.__stack_list[-1]
#         del self.__stack_list[-1]
#         return val

# stack_object_1 = Stack()
# stack_object_2 = Stack()

# stack_object_1.push(3)
# stack_object_2.push(stack_object_1.pop())

# print("Stack obj sec:", stack_object_2.pop())

# # НАСЛЕДОВАНИЕ И ПОЛИМОРФИЗМ
# class Stack:
#     def __init__(self):
#         self.__stack_list = []

    
#     def push(self, val):
#         self.__stack_list.append(val)
    
    
#     def pop(self):
#         val = self.__stack_list[-1]
#         del self.__stack_list[-1]
#         return val


# class AddingStack(Stack):
#     def __init__(self):
#         Stack.__init__(self)
#         self.__sum = 0
    

#     def get_sum(self):
#         return self.__sum
    
#     def push(self, val):
#         self.__sum += val
#         Stack.push(self, val)
    
    
#     def pop(self):
#         val = Stack.pop(self)
#         self.__sum -= val
#         return val
    
# stack_object = AddingStack()

# for i in range(6):
#     stack_object.push(i)
# print(stack_object.get_sum())    

# for i in range(6):
#     print(stack_object.pop())

# # __slots__

# class MyClass:
#     __slots__ = ["just_one"]

#     def __init__(self, number):
#         self.just_one = number

# foo = MyClass(222)
# foo.just_one  # 222 
# foo.__dict__  # AtributeError
# foo.some_attr = 5 # AttributeError
# foo.just_one = "it works"
