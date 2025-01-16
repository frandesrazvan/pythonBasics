'''
def func1(n):
    return [str(num) for num in range(n)]

print(func1(10))

def func2(n):
    return list(map(str, range(n)))

print(func2(10))

import time

# CURRENT TIME BEFORE
start_time1 = time.time()

# RUN CODE
result1 = func1(10000)

# CURRENT TIME AFTER
end_time1 = time.time()

# ELAPSED TIME
elapsed_time1 = end_time1 - start_time1
print(elapsed_time1)

# CURRENT TIME BEFORE
start_time2 = time.time()

# RUN CODE
result2 = func2(10000)

# CURRENT TIME AFTER
end_time2 = time.time()

# ELAPSED TIME
elapsed_time2 = end_time2 - start_time2
print(elapsed_time2)

# COMPARRISON
print(f'func1 took {elapsed_time1} while func2 took {elapsed_time2}')
'''

import timeit

stmt = '''
func1(100)
'''

setup = '''
def func1(n):
    return [str(num) for num in range(n)]
'''

print(timeit.timeit(stmt, setup, number=1000000))

stmt2 = '''
func2(100)
'''

setup2 = '''
def func2(n):
    return list(map(str, range(n)))
'''

print(timeit.timeit(stmt2, setup2, number=1000000))
