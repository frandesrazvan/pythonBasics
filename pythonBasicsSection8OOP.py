class Dog():
    
    # Class Object Attribute
    species = 'mammal'
    
    # CONSTRUCTOR
    def __init__(self, breed, name, spots):
        self.breed = breed
        self.name = name
        
        # Expect boolean True/False
        self.spots = spots
        
    def bark(self, number):
        print(f'{self.name} said: Auf Auf Auf {number} times')

my_dog = Dog(breed = 'Lab', name = 'Rascal', spots = True)
my_dog2 = Dog('Terrier', 'Pedro', False)
print(my_dog.breed + my_dog.name + str(my_dog.spots) + my_dog.species)
my_dog.bark(3)
print(my_dog2.breed + my_dog2.name + str(my_dog2.spots) + my_dog.species)

class Circle():
    
    pi = 3.14
    
    def __init__(self, radius = 1):
        self.radius = radius
        self.area = radius * radius * self.pi
        # self.area = radius * radius * Circle.pi
        
    def get_circumference(self):
        return self.radius * self.pi * 2
        
my_circle = Circle()
my_circle2 = Circle(5)

print(my_circle.get_circumference())
print(my_circle2.get_circumference())
print(my_circle.area)
print(my_circle2.area)

class Animal():
    
    def __init__(self):
        print('ANIMAL CREATED')
        
    def who_am_i(self):
        print('I am an animal')
        
    def eat(self):
        print('I am eating')
        
class Dog2(Animal):
    
    def __init__(self):
        Animal.__init__(self)
        print('DOG CREATED')
        
    def who_am_i(self):
        print('I am a dog')
        
    def bark(self):
        print('WOOF!')
        
my_dog = Dog2()
my_dog.who_am_i()
my_dog.eat()
my_dog.bark()

class Dog3():
    
    def __init__(self, name):
        self.name = name
        
    def speak(self):
        return self.name + ' says WOOF!'
        
class Cat3():
    
    def __init__(self, name):
        self.name = name
        
    def speak(self):
        return self.name + ' says MEOW!'
        
mydog = Dog3('Niko')
mycat = Cat3('Fifi')

print(mydog.speak())
print(mycat.speak())

for pet in [mydog, mycat]:
    print(type(pet))
    print(pet.speak())
    
def pet_speak(pet):
    print(pet.speak())
    
pet_speak(mydog)
pet_speak(mycat)

class Animal2():
    
    def __init__(self, name):
        self.name = name
        
    def speak(self):
        raise NotImplementedError('Subclass must implement this abstract method')
        
myanimal2 = Animal2('Fred')

class Dog4(Animal2):
    
    def speak(self):
        return self.name + ' says WOOF!'
        
class Cat4(Animal2):
    
    def speak(self):
        return self.name + ' says MEOW!'
        
mydog4 = Dog4('Namor')
mycat4 = Cat4('Bubu')

print(mydog4.speak())
print(mycat4.speak())

class Book():
    
    def __init__(self, title, author, pages): 
        self.title = title
        self.author = author
        self.pages = pages
        
    def __str__(self):
        return f"\"{self.title}\" by {self.author} and has {self.pages} pages"
        
    def __len__(self):
        return self.pages
        
    def __del__(self):
        print('A book object has been deleted')
        
b = Book('Python rocks', 'Jose', 200)
print(b)
print(len(b))

del b
print(b)