# # Class work L3

# li = [1 , 2, 4, 65, 1,3]

# print(li.index(1))

# li1 = li.copy()

# print(li1)
# print(li is li1)

# li = [1, 2, 3]
# li1 = [3, 4, 6]
# li += li1
# print(li)

# del li[-1]
# print(li)

# numbers = [111, 7, 2, 1]
# print(len(numbers))
# print(numbers)

# numbers.append(4)
# print(numbers)

# numbers.insert(0, 222)
# print(numbers)

# my_list = []
# for i in range(5):
#     my_list.append(i +1)
#     print(my_list)
#     print("len = ", my_list)
# print()
# print(my_list)

# my_list = [10, 1, 8, 3]
# total = 0
# for i in range(len(my_list)):
#     total += my_list[i]
# print(total)

# my_list = [10, 1, 8, 3]
# print(sum(my_list))

# my_list = [10, 1, 8, 3]
# total = 0

# for i in  my_list:
#     total += i
# print(total)    

# my_list = ["white", "Purle", "blue"]
# print(len(my_list))

# del my_list[2]
# print(len(my_list)) 

# lst = [1, 2, 3, 4, 5]
# lst_2 = []
# add = 0

# for number in lst:
#     add += number
#     lst_2.append(add)

# print(lst_2)

# my_list = ["w", "p", "b", "y", "g"]
# for color in my_list:
#     print(color)

# li = [1, 2, 3, 4]
# for i in li:
#     print(i)

# my_list = [8, 10, 6, 2 ,4]
# swapped = True

# while swapped:
#     swapped = False
#     for i in range(len(my_list)- 1):
#         if my_list[i] > my_list[i + 1]:
#             swapped = True
#             my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

# print(my_list)

# Copying the entire list


# list_1 = [1]
# list_2 = list_1[:]
# print(list_1, list_2)
# list_1[0] = 2
# print(list_1, list_2)

# my_list = [0, 3, 12, 8, 2]
# print(5 in my_list)

# my_list = [17, 3 , 11, 5, 19, 9, 7, 15, 13]
# largest = my_list[0]

# for i in range(1, len(my_list)):
#     if my_list[i] > largest:
#         largest = my_list[i]
    
# print(largest)

# my_list = [1, 2 , 3, 4, 5]
# slice_one = my_list[2:]
# slise_two = my_list[:2]
# slice_three = my_list[-2:]

# print(slice_one)
# print(slise_two)
# print(slice_three)

# li = [value for value in range(1, 11)]
# print(li)

# li1 = [value for value in range(1, 11) if value % 2 == 0]
# print(li1)