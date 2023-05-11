from datetime import datetime


def time_stampin_machine(fun):
    def inner_wrapepr(*args):
        print(datetime.now().strftime('%H:%M:%S'))
        return(fun(*args))

    return inner_wrapepr


@time_stampin_machine
def simple_hello():
   print('Hello from simple fuction!')


@time_stampin_machine
def plus(num1, num2):
    return num1 + num2


@time_stampin_machine
def multi(num1, num2):
    return num1 * num2


simple_hello()
print("Result:", plus("Hello", "Python"))
print("Result:", plus(100, 90))
print("Result:", multi(100, 24))
