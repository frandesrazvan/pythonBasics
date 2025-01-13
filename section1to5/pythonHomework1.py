# Numbers: Int and Float
# Strings: a chain of characters
# Lists: a collection of itmes
# Tuples: immutable collection of items
# Dictionaries: a collection of key-value pairs

# result of first expression: 44
# result of second expression: 29
# result of third expression: 34

# type of 3 + 1.5 + 4 is float

# square root of a number is the number raised to the power of 0.5
# 100 ** 0.5

# square of a number is the number raised to the power of 2
# 100 ** 2

s = 'hello'
print(s[1])

s = 'hello'
print(s[::-1])

s = 'hello'
print(s[-1])
print(s[4])

list = [0, 0 ,0]
list2 = [0] * 3
print(list)
print(list2)

list3 = [1, 2, [3, 4, 'hello']]
# list3s = list3[2]
# list3s[2] = 'goodbye'
# print(list3)
list3[2][2] = 'goodbye'
print(list3)

list4 = [5, 3, 4, 6, 1]
list4.sort()
print(list4)

list4a = [5, 3, 4, 6, 1]
print(sorted(list4a))

d = {'simple_key': 'hello'}
print(d['simple_key'])

d = {'k1': {'k2': 'hello'}}
print(d['k1']['k2'])

d = {'k1': [{'nest_key': ['this is deep', ['hello']]}]}
print(d['k1'][0]['nest_key'][1][0])

# mesaj_diana = 'eu iubeste tu'
# prim_mesaj_diana = mesaj_diana[:2]
# secund_mesaj_diana = mesaj_diana[:11]
# print(secund_mesaj_diana + prim_mesaj_diana + '+' + mesaj_diana[-2:])

d = {'k1': [1, 2, {'k2': ['this is tricky', {'tough': [1, 2, ['hello']]}]}]}
print(d['k1'][2]['k2'][1]['tough'][2][0])

# You can't sort a dictionary because a dictionary is immutable.
# Actually: normal dictionaries are mappings not a sequence

# Tuples are immutable.

# A tuple is created by ()

# A set can only contain unique elements

list5 = [1, 2, 2, 33, 4 ,4 ,11 ,22 ,3 ,3 ,2]
print(set(list5))

# 2 > 3 False
print(2 > 3)

# 3 <= 2 False
print(3 <= 2)

# 3 == 2.0 False
print(3 == 2.0)

# 3.0 == 3 False
print(3.0 == 3) # gresit, e True

# 4**0.5 != 2 False
print(4**0.5 != 2)

l_one = [1, 2, [3, 4]]
l_two = [1, 2, {'k1': 4}]

print(l_one[2][0] >= l_two[2]['k1']) # 3 >= 4 False