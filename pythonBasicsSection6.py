### Methods and Functions ###

# mylist = [1,2,3]
# mylist.append(4)
# print(mylist)
# mylist.pop()
# print(mylist)
# mylist.insert(2, 5)
# print(mylist)

# def say_hello(name = 'Razvan'):
#     print(f'Hello {name}')

# say_hello('Sam')
# say_hello()

# def print_result(a, b):
#     print(a + b)

# def return_result(a, b):
#     return a + b

# print_result(10, 20)
# print(return_result(10, 20))

# def sum_numbers(num1, num2):
#     return num1 + num2

# print(sum_numbers(10, 20)) # 30
# print(sum_numbers('10', '20')) # 1020

# def sum_numbers2(num1, num2):
#     return int(num1) + int(num2)

# print(sum_numbers2('10', '20')) # 30

# def even_check(number):
#     return number % 2 == 0

# print(even_check(20)) # True

# # Return true if any number is even inside a list
# def check_even_list(num_list):
#     for number in num_list:
#         if number % 2 == 0:
#             return True
#     return False

# print(check_even_list([1, 3, 5])) # False
# print(check_even_list([1, 3, 5, 6])) # True

# # Return all even numbers in a list
# def return_even_list(num_list):
#     even_numbers = []
#     for number in num_list:
#         if number % 2 == 0:
#             even_numbers.append(number)
#     return even_numbers

# print(return_even_list([1, 2, 3, 4, 5, 6])) # [2, 4, 6]
# print(return_even_list([1, 3, 5])) # []

# stock_price = [('APPL', 200), ('GOOG', 400), ('MSFT', 100)]

# for item in stock_price:
#     print(item)

# for ticker, price in stock_price:
#     print(ticker)
#     print(price + (0.1 * price))

# work_hours = [('Razvan', 10000), ('Abby', 100), ('Billy', 400), ('Cassie', 800)]

# def employee_of_the_month(employees):
#     employee = ''
#     most_hours = 0
#     for name, hours in employees:
#         if most_hours < hours:
#             most_hours = hours
#             employee = name
#     return (employee, most_hours)
    
# print(employee_of_the_month(work_hours))
# nume, ore = employee_of_the_month(work_hours)
# print(f'Angajatul lunii este {nume} cu {ore} ore lucrate')

# from random import shuffle

# game_list = [' ', 'O', ' ']
# def shuffle_list(mylist):
#     shuffle(mylist)

#     return mylist

# def player_guess():
#     answer = ''
#     while answer not in ['1', '2', '3']:
#         answer = input('Where is the ball?(1, 2, 3)\n')

#     return int(answer)

# def check_guess(mylist, guess):
#     if mylist[guess - 1] == 'O':
#         print('You found it!')
#     else:
#         print('Better luck next time!')
#         print('It was in position: ' + str(mylist.index('O') + 1))
#         print(mylist)

# def game(list, answer):
#     if (list.index('O') == answer - 1):
#         print('You found it!')
#     else:
#         print('Better luck next time!')
#     # match(answer):
#     #     case '1':
#     #         if (list.index('O') == int(answer) - 1):
#     #             print('You found it!')
#     #         else:
#     #             print('Better luck next time!')
#     #     case '2':
#     #         if (list.index('O') == int(answer) - 1):
#     #             print('You found it!')
#     #         else:
#     #             print('Better luck next time!')
#     #     case '3':
#     #         if (list.index('O') == int(answer) - 1):
#     #             print('You found it!')
#     #         else:
#     #             print('Better luck next time!')
            
# shuffled_list = shuffle_list(game_list)
# # print(shuffled_list)
# player_answer = player_guess()
# # print(player_answer)
# check_guess(game_list, player_answer)
# # game(game_list, player_answer)

# def myfunc(a, b, c = 0, d = 0, e = 0):
#     # Returns the sum of a and b
#     return sum((a, b, c, d, e)) 

# print(myfunc(40, 60)) # 100
# print(myfunc(40, 60, 100)) # 200

# def myfunc2(*args):
#     for item in args:
#         print(item)
#     return sum(args)

# myfunc2(40, 60, 100, 1, 2, 3, 4, 5) # 215

# def myfunc3(**kwargs):
#     print(kwargs)
#     if 'fruit' in kwargs:
#         print(f'My fruit of choice is {kwargs["fruit"]}')
#     else:
#         print('I did not find any fruit here')

# myfunc3(fruit = 'apple', veggie = 'lettuce') # My fruit of choice is apple

# def myfunc4(*args, **kwargs):
#     print(args)
#     print(kwargs)
#     print(f'I would like {args[0]} {kwargs["food"]}')

# myfunc4(10, 20, 30, fruit = 'orange', food = 'eggs', animal = 'dog') # I would like 10 eggs

# def myfunc(*args):
#     mylist = []
#     for num in args:
#         if num % 2 == 0:
#             mylist.append(num)
#     return mylist
    
# print(myfunc(1, 2, 3, 4, 5, 6))

# def myfunc(my_string):
#     new_string = ''
#     for index, letter in enumerate(my_string):
#         if index % 2 == 0:
#             new_string += letter.upper()
#         else:
#             new_string += letter.lower()
#     return new_string

# print(myfunc('Razvan')) # RaZvAn

# hello = ' sadasdaasdas'

# def square(num):
#     return num**2

# my_nums = [1, 2, 3, 4, 5]

# for item in map(square, my_nums):
#     print(item)

# print(list(map(square, my_nums))) # [1, 4, 9, 16, 25]

# def splicer(mystring):
#     if len(mystring) % 2 == 0:
#         return 'EVEN'
#     return mystring[0]

# names = ['Andy', 'Eve', 'Sally']

# for name in map(splicer, names):
#     print(name)

# print(list(map(splicer, names))) # ['EVEN', 'E', 'S']

# def check_even(num):
#     return num % 2 == 0

# mynums = [1, 2, 3, 4, 5, 6]

# for num in filter(check_even, mynums):
#     print(num)

# list(filter(check_even, mynums)) # [2, 4, 6]

def square(num):
    return num**2

print(square(3)) # 9

square = lambda num: num**2

print(square(11)) # 121

print(list(map(lambda num: num**2, [1, 2, 3, 4, 5, 6]))) # [1, 4, 9, 16, 25, 36]

print(list(filter(lambda num: num % 2 == 0, [1, 2, 3, 4, 5, 6]))) # [2, 4, 6]
