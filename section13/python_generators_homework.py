# Problem 1: Create a generator that generates the squares of numbers up to some number N
def gensquares(N):
    
    for x in range(N):
        yield x ** 2

for x in gensquares(10):
    print(x)

# Problem 2: Create a generator that yields "n" random numbers between a low and high number(that are inputs)
import random

def rand_num(low, high, n):
    
    for _ in range(n):
        yield random.randint(low, high)
        
for num in rand_num(1, 10, 12):
    print(num)

# Problem 3: Use the iter() function to convert the string below into an iterator
s = 'hello'

for letter in iter(s):
    print(letter)

# Extra Credit! -> Generator Comprehension
my_list = [1, 2, 3, 4, 5]

gencomp = (item for item in my_list if item > 3)

for item in gencomp:
    print(item)