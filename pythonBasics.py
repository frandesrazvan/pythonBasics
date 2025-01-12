# a = 2 + 5
# print(a)
# print(type(a))

# b = 'i\'m going \n to mars'

# print(b)
# print(len(b))

# c = "Hello World"
# print(c[:3])
# print(c[3:])
# print(c[::3]) # HlWl
# print(c[::-1]) # reverse
# print(c[::-2]) # lo olH  actual -> drWolH
# print(c[::-3]) # dooe

# Immutability  
# name = "Sam"
# # name[0] = "P" # Strings are immutable
# last_letters = name[1:]
# new_name = 'P' + last_letters
# new_name *= 10
# print(new_name)

# a = 2 + 3
# b = '2' + '3'
# print(a)
# print(b)
# # print(a+b) # TypeError: unsupported operand type(s) for +: 'int' and 'str'
# name = "raZvan, frandes . zaarea"

# print(name)
# print(name.capitalize())
# print(name.upper())
# print(name.lower())
# print(name.split(", ."))

# print("This is {0} a string {0}".format("INSERTED", "MIDDLE"))
# # print("This is {} a string {}".format("INSERTED")) # IndexError: tuple index out of range
# print('The {q} {q} {f}'.format(f='fox', b='brown', q='quick'))

# result = 100/777 # 0.1287001287001287
# print("The result is {r:1.3f}".format(r=result)) # The result is 0.129

# name = "Jose"
# age = 66
# print(f"Hello, his name is {name} and he is {age} years old")

# my_list = [1, 2, 3]
# my_list2 = ["string", 100, 23.2]
# print(len(my_list2))
# print(my_list2)
# my_list2[1] = str(my_list2[1])
# print(my_list2)
# my_list2.append("four") # add to end of list
# print(my_list2)
# popped_item = my_list2.pop() # remove last element
# print(my_list2)
# print(popped_item)
# my_list2.pop(1)
# print(my_list2)
# my_list2.reverse()
# print(my_list2)

# my_list3 = {1: "one", 2: "two", 3: "three"}
# print(my_list3.items()) # dict_items([(1, 'one'), (2, 'two'), (3, 'three')])
# for key, value in my_list3.items():
#     key = key + 1
#     print(key, value)

# my_list4 = [4, 100, 50, 2, 1]
# my_list4.reverse()
# my_list4.sort()
# print(my_list4)
# my_list4.sort(reverse = True)
# print(my_list4)

# my_dict = {'key1': 'value1', 'key2': 'value2'}
# print(my_dict['key1']) 

# d = {'k1': 123, 'k2': [0, 1, 2], 'k3': {'insideKey1': 10, 'insideKey2': {'insideInsideKey': 100}}}
# print(d['k2'][1]) # 1
# print(d['k3']['insideKey1']) # 10
# print(d['k3']['insideKey2']['insideInsideKey']) # 100

# d['k4'] = 100

# print(d.keys())
# print(d.values())
# print(d.items()) # dict_items([('k1', 123), ('k2', [0, 1, 2]), ('k3', {'insideKey1': 10, 'insideKey2': {'insideInsideKey': 100}}), ('k4', 100)])

# t = (1, 2, 3, 1, 3 ,1, 1, 1)
# l = [1, 2, 3]
# print(type(t))
# print(type(l))

# print(t.count(1)) # count of 1
# print(t.index(3)) # first occurence of 3 by index

# myset = set()
# myset.add(1)
# myset.add(2)

# print(myset)

# myset.add(2)
# print(myset) # still shows {1, 2} so only unique values

# mylist = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3]
# set(mylist) 
# print(set(mylist)) # {1, 2, 3}

# with open('test.txt') as f:
#     print(f.read()) 

# with open('test2.txt', mode = 'r+') as file:
#     file.write('ABRACADABEA')
#     print(file.read())

# with open('test2.txt', mode = 'a') as file:
#     file.write('\nLAST WORDSSSS')

# with open('test2.txt', mode = 'r') as file:
#     print(file.read())

# def front_back(str):
#     if len(str) <= 1:
#         return str
#     mid = str[1:len(str)-1]
#     return str[len(str)-1] + mid + str[0]

# print(front_back("code")) # 'eodc'

# def front3(str):
#     return str[:3] * 3

# front3("code") # 'cocococode'

# mylist = [1, 2, 3]
# print(mylist)
# def myfunc(mylist):
#     mylist[0] = 4
#     return mylist
# print(myfunc(mylist))
# print(mylist)
# d = {'A': 1, 'B': 2, 'C': 3}

# print(d) # {}

# data = {'name:': 'Peter', 'age': 30}
# person = data.copy()

# print(person) # {'name:': 'Peter', 'age': 30}
# print(id(data) == id(person)) # 140707366366464

# a = 'mama'
# if a == 'Marius':
#     print('Hello Marius')
# elif a == 'Razvan':
#     print('Hello Razvan')
# elif a == 'Andrei':
#     print('Hello Andrei')
# else:
#     print('Hello stranger')

# mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# for num in mylist:
#     if num % 2 == 0:
#         print(f'Even number: {num}')
#     else:
#         print(f'Odd number: {num}')

# for _ in 'Hello':
#     print('Hello')

# tuple = [(1, 2), (3, 4), (5, 6), (7, 8)]
# for item in tuple:
#     item += item 

# for a, b in tuple:
#     print(a)
#     # print(b)

# d = {'k1': 1, 'k2': 2, 'k3': 3}
# for v in d.values():
#     print(v)

# x = 0

# while x < 5:
#     print(f'The current value of x is {x}')
#     x += 1
# else:
#     print('X is not less than 5')

# x = [1, 2, 3]
# for item in x:
#     # comment: IndentationError: expected an indented block after 'for' statement on line 198
#     pass

# string = 'Sammy'
# for letter in string:
#     if letter == 'a':
#         continue
#     print(letter)
# for letter in string:
#     if letter == 'a':
#         break
#     print(letter)

# mylist = [1, 2, 3]
# # for num in range(0, 11, 2):
# #     print(num)

# mylist2 = list(range(1, 11))
# print(mylist2) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# index_count = 0
# for letter in 'abcde':
#     print(f'At index {index_count} the letter is {letter}')
#     # index_count += 1

# index_count = 0
# word = 'abcde'
# for letter in word:
#     print(word[index_count])
#     index_count += 1

# word = 'abcde'
# for index, letter in enumerate(word):
#     print(letter)

# mylist1 = list(range(1, 6))
# mylist2 = ['a', 'b', 'c', 'd', 'e']
# for item in zip(mylist1, mylist2):
#     print(item) 

# mylist3 = [100, 200, 300]
# mylist4 = ['x', 'y', 'z', 'w', 'q']
# mylist5 = [10, 20, 30]
# for item in zip(mylist3, mylist4, mylist5):
#     print(item)
# # (100, 'x', 10)
# # (200, 'y', 20)
# # (300, 'z', 30)

# a = 'Razvan'
# if 'z' in a:
#     print('Yes')

# d = {'mykey': 345}
# if 345 in d.values():
#     print('Yes')

# mylist = [10, 20, 30, 40, 50, 60, 70, 80, 90]
# print(min(mylist))
# print(max(mylist))

# from random import shuffle
# shuffle(mylist)
# print(mylist)

# from random import randint
# mylist.append(randint(0, 100))
# print(mylist)

# result = input('Enter a number here: ')
# print(result)

# mystring = 'hello'
# print(list('hello'))

# mylist = [letter for letter in mystring]
# print(mylist)

# print([x for x in range(0, 11)])

# mylist2 = [num**2 for num in range(0, 11)]
# print(mylist2) # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# mylist3 = [x for x in range(0, 11) if x % 2 != 0]
# print(mylist3) # [0, 2, 4, 6, 8, 10]

# celcius = [0, 10, 20, 34.5]

# fahrenheit = [( (9/5) * temp + 32) for temp in celcius]
# # same shit but longer
# # fahrenheit2 = []
# # for temp in celcius:
# #     fahrenheit2.append(( (9/5) * temp + 32))

# print(fahrenheit) # [32.0, 50.0, 68.0, 94.1]

# results = [x if x % 2 == 0 else 'ODD' for x in range(0, 11)]
# print(results) # [0, 'ODD', 2, 'ODD', 4, 'ODD', 6, 'ODD', 8, 'ODD', 10]

# mylist5 = []
# for x in [2, 4, 6]:
#     for y in [1, 10, 1000]:
#         mylist5.append(x * y)

# print(mylist5) # [2, 20, 2000, 4, 40, 4000, 6, 60, 6000]
# #same shit
# mylist6 = [x * y for x in [2, 4, 6] for y in [1, 10, 1000]]
# print(mylist6)