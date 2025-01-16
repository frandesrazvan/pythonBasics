'''
from collections import Counter

mylist = [1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 3, 3]
print(Counter(mylist))

mylist2 = ['a', 'a', 10, 10, 10]
print(Counter(mylist2))

print(Counter('aaaabdsgadgsdgsdgsgsd'))

sentence = 'How many times does each word show up in this sentence with a word'
print(Counter(sentence.lower().split()))

letters = 'asdaaaaaaasssssssdddd'
c = Counter(letters)
print(c)
print(c.most_common())
print(c.most_common(1))

print(list(c)) # list of unique values
'''

'''
from collections import defaultdict

d = {'a': 10}

print(d['a'])
# print(d['WRONG']) # error

e = defaultdict(lambda: 0)
e['correct'] = 100
print(e['correct']) 
print(e['WRONG KEY']) # 0
'''

mytuple = (10, 20, 30)
print(mytuple[0])

from collections import namedtuple

Dog = namedtuple('Dog', ['age', 'breed', 'name'])
sammy = Dog(age = 5, breed = 'Husky', name = 'Sam')

print(sammy)
print(sammy.age) # 5
print(sammy[0]) # 5