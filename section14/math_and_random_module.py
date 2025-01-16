import math

value = 4.35
print(math.floor(value)) # 4
print(math.ceil(value)) # 5
print(round(value)) # 4

print(math.pi)

from math import pi

print(pi)
print(math.e)
print(math.inf)
print(math.nan)

# Checkout Numpy library for advanced maths

print(math.log(math.e))
print(math.log(100, 10)) # 2 -> 10 ** 2 = 100
print(math.sin(10))
print(math.degrees(pi/2))
print(math.radians(180))

import random

print(random.randint(0, 100))
# random.seed(101)
# print(random.randint(0, 100)) # ALWAYS 74
# print(random.randint(0, 100)) # always 24

mylist = list(range(0, 20))
print(random.choice(mylist))

# SAMPLE WITH REPLACEMENT
print(random.choices(population = mylist, k = 10)) # [3, 11, 15, 7, 2, 7, 16, 9, 4, 1]

# SAMPLE WITHOUT REPLACEMENT
print(random.sample(population=mylist, k=10)) # [2, 6, 5, 14, 4, 3, 11, 9, 15, 1]

random.shuffle(mylist)
print(mylist)

print(random.uniform(a = 0, b = 100))

print(random.gauss(mu = 0, sigma = 1))