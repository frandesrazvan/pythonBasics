def lesser_of_two_evens(a, b):
    if a % 2 == 0 and b % 2 == 0:
        if a < b:
            return a
        return b
    elif a % 2 != 0 or b % 2 != 0:
        if a < b:
            return b
        return a
        
print(lesser_of_two_evens(20, 6))

def animal_crackers(text):
    if len(text.split()) != 2:
        return 'You need to enter 2 words'
    else:
        if text.split()[0][:1].lower() == text.split()[1][:1].lower():
            return True
        return False
        
print(animal_crackers('a yuku'))

# Given a value, return a value that is twice as far away on the other side of 7
def other_side_of_seven(num):
    return 7 + (7 - num) * 2
    
print(other_side_of_seven(4)) # 13
print(other_side_of_seven(12)) # -3

# Write a function that capitalizes the first and fourth letters of a name
def old_macdonald(name):
    if len(name) > 3:
        return name[:3].capitalize() + name[3:].capitalize()
    return 'Name is too short'
    
print(old_macdonald('macdonald')) 

# Given a sentence, return a sentence with the words reversed
def master_yoda(text):
    yoda_speech_list = []
    for word in text.split(' '):
        yoda_speech_list.insert(0, word)
        
    yoda_speech = ''
    for word in yoda_speech_list:
        yoda_speech += word + ' '
        
    return yoda_speech
    
print(master_yoda('We are ready'))
print(master_yoda('I am home'))

# Given an integer n, return True if n is within 10 of either 100 or 200
def almost_there(n):
    if (abs(n) <= 110 and abs(n) >= 90) or (abs(n) <= 210 and abs(n) >= 190):
        return True
    return False
    
print(almost_there(90))
print(almost_there(104))
print(almost_there(150))
print(almost_there(209))
    
# Write a function that counts the number of times a given pattern appears in a string, inclding overlap
def laughter(pattern, text):
    count = 0
    for i in range(len(text)):
        if text[i:i + len(pattern)] == pattern:
            print(text[i:i + len(pattern)])
            count += 1
    return count

print(laughter('hah', 'hahahah'))

# Given a string, return a string where for every character in the original there are three characters
def paper_doll(text):
    triple_word = ''
    for letter in text:
        triple_word += letter * 3
    return triple_word
        
print(paper_doll('Miami'))

# Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. 
# If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'
def blackjack(a, b, c):
    bj = a + b + c
    if bj <= 21:
        return bj
        
    elif bj > 21: 
        if a == 11 or b == 11 or c == 11:
            bj -= 10
            
            return bj
        
        return 'BUST'
        
print(blackjack(5, 6, 7))
print(blackjack(9, 9, 9))
print(blackjack(9, 9, 11))

# Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 9
# (every 6 will be followed by at least one 9). Return 0 for no numbers
def summer_69(arr):
    total = 0
    add = True
    for num in arr:
        while add:
            if num != 6:
                total += num
                break
            else:
                add = False
        while not add:
            if num != 9:
                break
            else:
                add = True
                break
    return total    
        
print(summer_69([1, 3, 5]))
print(summer_69([4, 5, 6, 7, 8, 9]))
print(summer_69([2, 1, 6, 9, 11]))

# Write a function that takes a list of integers and returns True if it contains 007 in order
def spy_game(nums):
    agent = ''
    for num in nums:
        if num == 0:
            agent += str(num)
        elif num == 7:
            agent += str(num)
            
    print(agent)
    if agent == '007':
        return True
    return False
    
print(spy_game([1, 2, 4, 0, 0, 7, 5]))
print(spy_game([1, 0, 2, 4, 0, 5, 7]))
print(spy_game([1, 7, 2, 0, 4, 5, 0]))

# Write a function that returns the number of prime numbers that exist up to and including a given number
def count_primes(num):
    primes = []
    for n in range(2, num + 1):
        for i in range(2, n):
            if n % i == 0:
                break
        else:
            primes.append(n)
    return len(primes)
    
print(count_primes(100))

# Write a function that takes a single letter and returns a 5x5 representation of that letter
def print_big(letter):
    patterns = {1: '  *  ', 2: ' * * ', 3: '*****', 4: '*   *', 5: '**** '}
    alphabet = {'A': [1, 2, 3, 4, 4], 'B': [5, 4, 5, 4, 5], 'C': [3, 4, 4, 4, 3], 'D': [5, 4, 4, 4, 5], 'E': [3, 4, 3, 4, 3]}
    for pattern in alphabet[letter.upper()]:
        print(patterns[pattern])

print_big('d')