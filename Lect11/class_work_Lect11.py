# from random import seed, randint

# seed()
# data = [randint(-10, 10) for x in range(5)]
# filtered = list(filter(lambda x: x > 0 and x % 2 == 0, data))

# print(data)
# print(filtered)


# # ZIPS
# cities = ["France", "Russia", "Japan"]
# writers = ["Victor Hugo", "Fyodor Dostoevsky"]
# romans = ["A", "B", "s"]
# print(list(zip(cities, writers, romans)))


# # Замыкание
# def outer(par):
#     loc = par

#     def inner():
#         return loc
#     return inner

# var = 1
# fun = outer(var)
# print(fun())


# def make_closure(par):
#     loc = par

#     def power(p):
#         return p ** loc
#     return power

# fsqr = make_closure(2)
# fcub = make_closure(3)

# for i in range(15):
#     print(i, fsqr(i), fcub(i))


# # Работа с Файлами


# stream = open("tzop.txt", 'rt', encoding = "utf-8")

# print(stream.read())

# from os import strerror

# try:
#     cnt = 0
#     s = open('text.txt', 'rt')
#     ch = s.read(1)
#     while ch != '':
#         print(ch, end = '')
#         cnt += 1
#         ch = s.read(1)
#     s.close()
#     print('\n\nCharacters in file:', cnt)
# except IOError as e:
#     print("I/O error ccurred: ", strerror(e.errno))

# from os import strerror

# try:
#     cnt = 0
#     s = open('text.txt', 'rt')
#     content = s.read()
#     for ch in content:
#         print(ch, end = '')
#         cnt += 1
#     s.close()
#     print('\n\nCharacters in file:', cnt)
# except IOError as e:
#     print("I/O error ccurred: ", strerror(e.errno))

# from os import strerror

# try:
#     ccnt = lcnt = 0
#     s = open('text.txt', 'rt')
#     line = s.readline()
#     while line != "":
#         lcnt += 1
#         for ch in line:
#             print(ch, end = '')
#             ccnt += 1
#         line = s.readline()
#     s.close()
#     print('\n\nCharacters in file:', ccnt)
#     print("Lines in file: ", lcnt)
# except IOError as e:
#     print("I/O error ccurred: ", strerror(e.errno))


# fo = open('newtext.txt', 'wt')
# for i in range(10):
#     s = "line #" + str(i + 1) + "\n"
#     for ch in s:
#         fo.write(ch)
# fo.close


# fo = open('newtext.txt', 'wt')
# for i in range(10):
#     fo.write("kekline #" + str(i + 1) + "\n")        
# fo.close

# with open("newtxt.txt", 'wt') as fo:
#         for i in range(10):
#             s = "nekekline #" + str(i + 1) + "\n"
#             for ch in s:
#                   fo.write(ch)        
# fo.close