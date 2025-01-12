st = 'Print only the words that start with s in this sentence'
 
for word in st.split():
    if word[:1] == 's':
        print(word)

# for word in st.split():
#     if word[0] == 's':
#     # if word[0].lower() == 's':
#     # if word[0] == 's' or word[0] == 'S':
#         print(word)
        
for num in range(0, 11):
    if num % 2 == 0:
        print(num)

# for num in range(0, 11, 2):
#     print(num) 
        
print([x for x in range(1, 51) if x % 3 == 0])

stri = 'Print every word in this sentence that has an even number of letters'
for word in stri.split():
    if len(word) % 2 == 0:
        # print('The word "' + word + '" has an even ammount of letters')
        print('even!')
        
# for x in range(1, 101):
#     if x % 3 == 0:
#         if x % 5 == 0:
#             print('FizzBuzz')
#             continue
#         print('Fizz')
#         continue
#     elif x % 5 == 0:
#         print('Buzz')
#         continue
#     print(x)

for x in range(1, 101):
    if x % 3 == 0 and x % 5 == 0:
        print('FizzBuzz')
    elif x % 3 == 0:
        print('Fizz')
    elif x % 5 == 0:
        print('Buzz')
    else:
        print(x)

# Boltz    
# for num in range(1, 100):
#     if num % 7 == 0 or '7' in str(num):
#         print('Bolț')
#         continue;
#     print(num)

mystring = 'Create a list of the first letters of every word in this string'
print([letter[:1] for letter in mystring.split(' ')])

# print([letter[0] for letter in mystring.split()])
