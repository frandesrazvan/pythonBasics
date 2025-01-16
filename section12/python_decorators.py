'''
def func():
    return 1
    
print(func())

def hello():
    return 'Hello!'
    
print(hello())

greet = hello
print(greet())

# del hello
# hello() # error not defined
# print(greet()) # Hello!
'''

'''
def hello(name = 'Jose'):
    print('The hello() function has been executed')
    
    def greet():
        return '\t This is the greet() function inside hello()'
        
    def welcome():
        return '\t This is welcome() inside hello()'
       
    print('I am going to return a function!')
    
    if name == 'Jose':
        return greet
    return welcome
    # print(greet())
    # print(welcome())
    # print('This is the end of the hello function!')
    
my_new_func = hello()
print(my_new_func())
'''

'''
def cool():
    
    def super_cool():
        return 'I am very cool!'

    return super_cool()
    
some_func = cool()
print(some_func)
'''

'''
def hello():
    return 'Hi Jose!'
    
def other(some_def_func):
    print('Other code runs here!')
    print(some_def_func())
    
other(hello)
'''

def new_decorator(original_func):
    
    def wrap_func():
        print('Some extra code, before the original function')
        
        original_func()
        
        print('Some extra code, after the original function')
        
    return wrap_func
    
def func_needs_decorator():
    print('I want to be decorated!!!')
    
decorated_func = new_decorator(func_needs_decorator)
decorated_func()