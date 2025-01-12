# Write a functionthat computes the volume of a sphere given its radiusimport math
import math

def vol(rad):
    return print(4 / 3 * math.pi * rad ** 3)

vol(5)

# Write a function that checks whether a number is in a given range (inclusive of high and low)
def ran_check(num, low, high):
    for x in range(low, high + 1):
        if num == x:
            return print(str(num) + ' is in range between ' + str(low) + ' and ' + str(high))
    return print(str(num) + ' is outside the range between ' + str(low) + ' and ' + str(high)) 
    
def ran_bool(num, low, high):
    for x in range(low, high + 1):
        if num == x:
            return True
    return False
    
ran_check(5, 2, 7)
print(ran_bool(11, 1, 10))

# Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters
def up_low(s):
    upper_characters = 0
    lower_characters = 0
    for word in s.split():
        for letter in word:
            if letter.isupper() == True:
                upper_characters += 1
            elif letter.islower() == True:
                lower_characters += 1
    
    print(f'No. of Upper case characters : {upper_characters}')  
    print(f'No. of Lower case characters : {lower_characters}')
    
string = 'Hello Mr. Rogers, how are you this fine Tuesday?'
up_low(string)

# Write a Python function that takes a list and returns a new list with unique elements of the first list
def unique_list(lst):
    new_list = []
    for x in set(lst):
        new_list.append(x)
        
    return new_list
    
mylist = ([1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5])
print(unique_list(mylist))

# Write a Python function to multiply all the numbers in a list
def multiply(numbers):
    sum = 1
    
    for x in numbers:
        sum *= x
        
    return sum

mylistnumbers = [1, 2, 3, -4]
print(multiply(mylistnumbers))

# Write a Python function that checks whether a passed string is palindrome or not
def palindrome(s):
    if s.replace(' ', '') == s[::-1]:
        return True
    return False
    
print(palindrome('helleh'))

# Write a Python function to check whether a string is pangram or not
import string

def ispanagram(str1, alphabet = string.ascii_lowercase):
    all_characters = ''
    
    for word in str1.split():
        for letter in word:
            all_characters += letter.lower()
     
    if ''.join(sorted(set(all_characters))) == alphabet:
        return True
    return False

    
mystring1 = 'The quick brown fox jumps over the lazy god'
print(ispanagram(mystring1))