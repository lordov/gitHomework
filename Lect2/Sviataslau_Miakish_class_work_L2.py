## Class work L2_p1.

# my_name = input("Put your name here - - ->")

# print(f'Your name is {my_name}')

## Type casting -- to Integer.

# x = int(1)  # x will be 1
# y = int(2.8)  # y will be 2
# z = int("3")  # z will be 3

## Type cassting - to float.

# x = float(1)  # x will be 1.0.
# y = float(2.8)  # y will be 2.8.
# z = float("3")  # z will be 3.0.
# w = float("4.2")  # w will be 4.2.
# print(x, y, z, w, sep="\n")

## Type casting -- to string.

# x = str("1")  # x wtill be "s1".
# y = str(2)  # y will be "2".
# z = str(3.0)  # z will be "3.0"
# print(x, y, z, sep="\n")

# # Concatenation.

# fnam = input("May i have your first name, please? ")
# lnam = input("May I have your last name, please? ")
# print("Tank you.")
# print("\nYour name is " + fnam + " " + lnam, end=".")

## Auto Concatenation

# my_string = "Lenin" "ninel"  # Autocncat.
# '2000$'  # Just igbore 2000$

# print(my_string)

# print("Why", "hell"
#       "no" "hell", "?")  # Why hellnohell ?

# my_string1 = ("Lenin" "nineL"  # Autoconcat.
#               "2000$")  # also 2000$.

# print(my_string1)

# # Replication

# print("+" + 10 * "-" + "+")
# print(("|" + " " * 10 + "|\n") * 5, end="")
# print("+" + 10 * "-" + "+")

# print("James" * 4 + "Bond" * 2)

# a = 100

# print(f"{a = }")

# jo_apples = 55
# kate_apples = 77 
# jo_and_kate_apples = jo_apples + kate_apples

# print(f"Our results is: {jo_apples} + {kate_apples} = {jo_and_kate_apples}")

# This program is a simple calculator.
# Just put two ints and waiting for math results.

# # Too stupid.

# a = input()
# b = input()
# a = int(a)
# b = int(b)

# print("\nResults of maths! + - * /")
# print(a, "+", b, "=", a + b)
# print(a, "-", b, "=", a - b)
# print(a, "*", b, "=", a * b)
# print(a, "/", b, "=", a / b)

# # Still to stupid.

# a, b = input(), input()
# a, b = int(a), int(b)

# print("\nResults of maths! + - * /")
# print(a, "+", b, "=", a + b)
# print(a, "-", b, "=", a - b)
# print(a, "*", b, "=", a * b)
# print(a, "/", b, "=", a / b)

# # Too simple.

# first_number = input("Put first integer number: ")
# second_number = input("Put second integer number: ")
# first_number = int(first_number)
# second_number = int(second_number)

# print("\nResults of maths! + - * /")
# print(first_number, "+", second_number, "=", first_number + second_number)
# print(first_number, "-", second_number, "=", first_number - second_number)
# print(first_number, "*", second_number, "=", first_number * second_number)
# print(first_number, "/", second_number, "=", first_number / second_number)

# # Less better.

# first_number = int(input("Put first integer number: "))
# second_number = int(input("Put second integer number: "))


# print("\nResults of maths! + - * /")
# print(first_number, "+", second_number, "=", first_number + second_number)
# print(first_number, "-", second_number, "=", first_number - second_number)
# print(first_number, "*", second_number, "=", first_number * second_number)
# print(first_number, "/", second_number, "=", first_number / second_number)

# Less less better.

# first_number = int(input("Put first integer number: "))
# second_number = int(input("Put second integer number: "))

# print("\nResults of maths! + - * /")
# # Just use f-strings - started with python 3.6.
# print(f'{first_number} + {second_number} = {first_number + second_number}')
# print(f'{first_number} - {second_number} = {first_number - second_number}')
# print(f'{first_number} * {second_number} = {first_number * second_number}')
# print(f'{first_number} / {second_number} = {first_number / second_number}')

# # This is OK.

# first_number, second_number = int(
#     input("Put first integer number: ")),int(input("Put second integer number: "))

# print("\nResults of maths! + - * /")
# # Just use f-strings - started with python 3.6.
# print(f'{first_number} + {second_number} = {first_number + second_number}')
# print(f'{first_number} - {second_number} = {first_number - second_number}')
# print(f'{first_number} * {second_number} = {first_number * second_number}')
# print(f'{first_number} / {second_number} = {first_number / second_number}')

# name = "He say: 'Hello Jonny'"

# # Exponentation (power).

# print(2 ** 3)
# print(2. ** 3)
# print(2 ** 3.)
# print(2. ** 3. ** 2)

# # Multiplication.

# print(2 * 3)
# print(2. * 3)
# print(2 * 3.)
# print(2. * 3. * 2)

# # Division / . Always a float.

# print(6 / 3)
# print(6 / 3.)
# print(6. / 3)
# print(6. / 3.)

# # Integer Division // .

# print(6 // 3)
# print(6 // 3.)
# print(6. // 3)
# print(6. // 4.)

# Remainder(modulo) % .

# print(15 % 3 )
# print(14 % 4.)
# print(14. % 4)
# print(14. % 4.)

# # Reserved keywords

# import keyword

# print("Ключевые слова языка Pyhthon: {} {}".format('\n', keyword.kwlist))

# anything = int(input("Enter a number: "))
# something = anything ** 2.0

# print(f"{anything} to the power of 2 is {something}")

# Class work_L2_P3

# n = int(input("Enter a number: "))

# print(n < 100)
# print(n > 100)
# print(n == 55)
# print(n != 55)
# print(n >= 100)
# print(n <= 100)

# x = 10
# y = 20
# z = 20

# print(x == y)  # Output: False.
# print(z == y)  # Output: True.
# print(x !=y )  # Output: True.
# print(x > 20)  # Output: False.
# print(x < y)  # Output: True.
# print(x >= 10)  # Output: True.
# print(y <= 20)  # Output: True

# # IF statement.

# a = 33 
# b = 50

# if b > a:
#     print(f"{b} is greater than {a}")


# # kLASS work for svIat

# # Store the current largest number here.

# largest_number = - 9999999

# # Input the first value.

# number = int(input("Enter a number or type -1 to stop:"))

# # If the number is not equal to -1, continue.
# while number != -1:
#     # Is number larger than largest_number?
#     if number > largest_number:
#         # Yes, update largest number.
#         largest_number = number
#         # Input the next number.
#         number = int(input("Enter a number or type -1 to stop: "))

# # Print the largest number.
# print("The largest number is:", largest_number)

# odd_numbers = 0
# even_numbers = 0

# # Read the first number.
# number = int(input("Enter a number or type 0 to stop: "))

# # 0 terminates execution.
# while number != 0:
#     # Check if the number is odd.
#     if number % 2 == 1:
#         # Increase the odd_numbers counter.
#         odd_numbers += 1
#     else:
#         # increase the even_numbers counter.
#         even_numbers += 1
#     # Read the next number.
#     number = int(input("Enter a number or type 0 to stop: "))

# # Print results.
# print("Odd numbers count:", odd_numbers)
# print("Even numbers count:", even_numbers)

# counter = 5
# while counter != 0:
#     print("Inside the loop" , counter)
#     counter -= 1
# print("Outside the loop.", counter)

# for i in range (10):
#     print("The value of i is currently", i)

# power = 1
# for expo in range(16):
#     print("2 to the power of", expo, "is", power)
#     power *= 2

# import time
# for i in range(1, 10):
#     pp = i ** 2
#     print(i, "-->", pp)
#     time.sleep(1)

# PART OF HOME WORK 

# import time

# for i in range(1, 6):
#         print(i, "Mississippi")
#         time.sleep(1)
# print("Ready or not, here i come!")

# # break - example

# print("The break instruction:")
# for i in range(1, 6):
#     if i == 4:
#         break
#     print("inside the loop.", i)
# print("Outside the loop.")

# # continue - example 

# print("\nThe continue instruction:")
# for i in range(1, 6):
#     if i == 3:
#         continue
#     print("Inside the loop.", i)
# print("Outside the loop.")

# largest_number = -9999999
# counter = 0

# number = int(input("Enter a number or type -1 to end program: "))

# while number != -1:
#     counter +=1
    
#     if number > largest_number:
#         largest_number = number
#     number = int(input("Enter a number or type -1 to end program: "))

# if counter:
#     print("The largest number is", largest_number)
# else:
#     print("You haven't entered any number.")

# IN NOT IN

# name = "Pyotr Yan"
# to_find = input()

# print(name, to_find)

# print(to_find in name)
# print(to_find not in name)

# # СВЯТ ВЫРЕЗАТЬ в домашку.

# name = input("Введите Ваше имя: ")
# name = name.upper()
# for i in name:
#     if i in "AEIOU":
#         continue
#     print(i)

# The while loop and the else branch


# numbers = [11, 33, 53, 35, 65, 765, 345,761,13]

# for num in numbers:
#     if num % 2 == 0:
#         print("The list contauns an even number")
#         break
# else:
#     print("The list does not contain even number")

# # Home work 2.6

# operator = input("Введите один оператор из (+ - / *) или exit для выхода ")

# while operator != "exit":
#     num1, num2, = int(input("Введите первое число ")), int(input("Введите второе число "))
    
#     if operator == "+":
#         summarize = num1 + num2
#         print(summarize)
    
#     elif operator == "-":
#         subtraction = num1 - num2
#         print(subtraction)
    
#     elif operator == "/":
#         division = num1 / num2
#         print(division)
    
#     elif operator == "*":
#         multiplication = num1 * num2
#         print(multiplication)
    
#     operator = input("Введите один оператор из (+ - / *) или exit для выхода ")

# else:
#     print("Bye, bye")

