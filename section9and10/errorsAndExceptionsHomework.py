# Problem 1
# Handle the exception thrown by the code below by using try and except blocks.

# for i in ['a', 'b', 'c']:
#     print(i ** 2)

for i in ['a', 'b', 'c']:
    try:
        print(i ** 2)
    except:
        print('The value you entered is not a number')

# Problem 2
# Handle the exception thrown by the code below by using try and except blocks. Then use a finally block to print 'All Done.

# x = 5
# y = 0

# z = x / y

x = 5
y = 0

try:
    z = x / y
except:
    print('You cannot divide a number by 0')
finally:
    print('All Done')

# Problem 3
# Write a function that asks for an integer and prints the square of it. Use a while loop with a try, except, else block to account for incorrect inputs.

# def ask():
#     pass

# ask()

