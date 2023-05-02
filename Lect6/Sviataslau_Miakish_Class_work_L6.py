# Class work L6.

# empty_tuple = ()
# print(isinstance(empty_tuple, tuple))

# tp =(1, 2, 3,)
# a, b, c = tp
# print(a, b, c)

# my_tuple = (1, 10, 100, 1000,)

# print(my_tuple[0])

# print(my_tuple[-1])

# print(my_tuple[1:])

# print(my_tuple[:-2])

# my_tuple = (1, 10, 100, 1000,)

# print(my_tuple*3)

# li = [1, 4,5]
# tp = (1, 2, li,)

# tp[2].append("привет")
# print(tp)

# my_tuple = (1, 10, 100, 1000,)

# t1 = my_tuple + (24, 2421,)
# t2 = my_tuple * 3
# print(t1,t2)

# a, b, *c = my_tuple

# print(a, b, c)

# di = {1: 'one', 2: 'two'}
# print(di[1])

# thisdict = {
#     "brand": "Ford",
#     "model": "mustang",
#     "year": 1964, 
# }

# print(thisdict["model"])

# dictonary1 = {
#     "cat": "chat",
#     "dog": "chien",
#     "horse": "cheval"
# }

# words = {"cat", "lion", "horse"}

# for word in words:
#     if word in dictonary1:
#         print(word, "-->", dictonary1[word])
#     else:
#         print(word, "is not in dictonary")

# car = {
#     "brand": "Ford",
#     "model": "mustang",
#     "year": 1964, 
# }

# print(thisdict.get("brand"))

# car = {
#     "brand": "Ford",
#     "model": "mustang",
#     "year": 1964, 
# }

# for key in car.keys():
#     print(car.get(key))

# for key, val in car.items():
#     print(key, val)

# for tupl in car.items():
#     print(tupl[0], tupl[1])

# print(car.values())

# car = {
#     "brand": "Ford",
#     "model": "mustang",
#     "year": 1964, 
# }

# car.update({"sport": "yes"})
# print(car)

# import datetime

# start = datetime.datetime.now()
# kekl = input("Введите число")
# end = datetime.datetime.now()
# alltime = print(end - start)

# my_tuple = (1, 2, True, "a string", (3, 4), [5, 6], None)
# print(my_tuple)


# my_list = [1, 2, True, "a string", (3, 4), [5, 6], None]

# my_dict = {1: 'kekl'}
# print(my_dict.keys())

brend = "brand"
score = "ford"

car = {
     brend: score,
    "model": "mustang",
    "year": 1964, 
}


print(car.get(brend))



