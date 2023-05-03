# def decor(fnct):
#     def inner_wrapper(arg):
#         print('СССР Всё ещё, что?...')
#         print(fnct(arg))
    
#     return inner_wrapper


# @decor
# def lenin(take):
#     return take, True

# @decor
# def stalin(take):
#     return take, True

# @decor
# def gorbachev(take):
#     return take, False

# lenin('Ya strou socialism')
# stalin("odni plasch i sapogi")
# gorbachev("zato u menia primia")


# def simple_decorator(own_function):

#     def internal_wrapper(*args, **kwargs):
#         print(f'{own_function.__name__} was called with the following arguments')
#         print(f'\t{args}\n\t{kwargs}\n')
#         own_function(*args, **kwargs)
#         print("Decotator is still operating")
#     return internal_wrapper

# @simple_decorator
# def combiner(*args, **kwargs):
#     print("\tHello from the decorated fucntion;\n\
#           received arguments:", args, kwargs)
    
# combiner('a', "b", exec = "yes")

class Example:
    __internal_counter = 0

    def __init__(self, value):
        Example.__internal_counter += 1

    @classmethod
    def get_internal(cls):
        return f'# of objects created: {cls.__internal_counter}'
    

print(Example.get_internal())

examle1 = Example(10)
print(Example.get_internal())
examle2 = Example(50)
print(Example.get_internal())
