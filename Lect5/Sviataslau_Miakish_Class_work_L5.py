# def times(x, y):
#     '''Умножает x на y.'''
#     z = x * y
#     times.__doc__ = "Чтоо-то на задкуменченном прикольно что __doc__ перебивает ''' ''' :) .  "
#     return z


# results = times(4, 5)
# print(results)

# # help(times)

# def yell(text):
#     return f'{text.upper()}!'


# bark = yell

# nonono = bark

# del yell



# print(bark("hell no"))

# def happy_new_year(wishes = True):
#     print(3)
#     print(2)
#     print(1)
#     if not wishes:
#         return

# happy_new_year(False)



# value = None
# if value is None:
#     print("Sorry, you don't carry any value.")

# def list_summ(lst):
#     s = 0

#     for elem in lst:
#         s += elem
#     return s

# print(list_summ([5, 4, 3]))

# def fool(value):
#     if value:
#         return value
#     return value

# def strange_list_fun(n):
#     strange_list = []
    
#     for i in range(0, n):
#         strange_list.insert(0, i)
    
#     return strange_list

# print(strange_list_fun(6))

# def wishes():
#     print("My wishes")
#     return "Happy birthday"


# def is_int(data):
#     return isinstance(data, int)

# print(is_int(5))
# print(is_int(5.))

# def hil(my_list):
#     my_list[1] = 1111
#     print("Inside the func", my_list)

# a = ["Adam", "John", "Dima"]
# print("Original list:", a)
# hil(a)
# print("Original after proc:", a, "\n")

# a = ["Adam", "John", "Dima"]
# print("Original list:", a)
# hil(a[:])
# print("Original after proc:", a, "\n")

# a = ["Adam", "John", "Dima"]
# print("Original list:", a, )
# hil(a[:2])
# print("Original after proc:", a, "\n")


# def fac(n):
#     if n == 0:
#         return 1
#     return n * fac(n-1)

# print(fac(5))