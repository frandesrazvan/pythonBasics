'''
def create_cubes(n):
    for x in range(n):
        yield x ** 3
    
print(list(create_cubes(10))) 
    
for x in create_cubes(10):
    print(x)
    
def gen_fibon(n):
    a = 1
    b = 1
    
    for i in range(n):
        yield a
        a, b = b, a + b
        
for x in gen_fibon(10):
    print(x)
'''

def simple_gen():
    for x in range(3):
        yield x
        
for num in simple_gen():
    print(num)
    
g = simple_gen()

print(next(g)) # 0
print(next(g)) # 1
print(next(g)) # 2
# print(next(g)) # error StopIteration

s = 'hello'
for letter in s:
    print(letter)
    
# print(next(s)) # TypeError: 'str' object is not an iterator
s_iter = iter(s)
print(next(s_iter)) # h
print(next(s_iter)) # e