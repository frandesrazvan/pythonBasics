def add(n1, n2):
    try:
        print(n1 + n2)
    except:
        print('Hey it looks like you aren\'t adding correctly!')
    else:
        print('Add went well!')
    
add(10, 20)

number1 = 10
number2 = input('Please provide a number: ')

add(number1, number2)
print('Something happened')

try:
    f = open('test3.txt', 'w') # change to 'r' to see the OSError
    f.write("Write a test line")
except TypeError:
    print('There was a type error!')
except OSError:
    print('Hey, you have an OS Error!')
except:
    print('All other exceptions!')
finally:
    print('I always run')

def ask_for_int():
    
    while True:
        try:
            result = int(input('Please provide a number: '))
        except:
            print('Whoops! That is not a number!')
            continue
        else:
            print('Thank you!')
            break
        finally:
            print('I\'m going to ask you again')
        
ask_for_int()

def ask():
    
    while True:
        try:
            result = int(input('Please enter a number: '))
        except:
            print('You did not enter a number')
            continue
        else:
            square = result ** 2
            print(f'The square of {result} is {square} \n')
            break
        finally:
            print('A G A I N !')
        
ask()