#
### Instantiation : Classes must be called in an instance
#

class Facade:
  pass

facade_1 = Facade()

#
### ___main___ : The class
#

class Facade:
  pass

facade_1 = Facade()
facade_1_type = type(Facade())
print(facade_1_type)
# Output: <class '__main__.Facade'> : This is the object, ___main___ indicates the object called is defined in the current file


#
### Class Variables : Call variables from inside a class
#

class Musician:
  title = "Rockstar"
 
drummer = Musician()
print(drummer.title)
# prints "Rockstar"

#
### Class Methods : Calls the function to itself
#

class Dog:
  dog_time_dilation = 7
 
  def time_explanation(self):
    print("Dogs experience {} years for every 1 human year.".format(self.dog_time_dilation))
 
pipi_pitbull = Dog()
pipi_pitbull.time_explanation()
# Prints "Dogs experience 7 years for every 1 human year."

#
### Class Methods : Calls the function with multiple variables
#

class Circle:
  pi = 3.14
  def area(self, radius):
    return Circle.pi * radius ** 2

circle = Circle()

pizza_area = circle.area(12 /2)
teaching_table_area = circle.area(36 / 2)
round_room_area = circle.area(11460 / 2)

#
### Constructors
#

#
# __init__ : This method is used to initialize a newly created object. It is called every time the class is instantiated.
#

class Circle:
  pi = 3.14
  
  # Add constructor here:
  def __init__(self, diameter):
    print("New circle with diameter: " + str(diameter))

teaching_table = Circle(36)

#
### Instance Variables : The data held by an object is referred to as an instance variable. Instance variables aren’t shared by all instances of a class — they are variables that are specific to the object they are attached to.
#

class Store:
  pass

alternative_rocks = Store()
isabelles_ices = Store()

alternative_rocks.store_name = "Alternative Rocks"
isabelles_ices.store_name = "Isabelle's Ices"

#
### Attribute Functions
# 

# getattr(object, “attribute”, default)

class NoCustomAttributes:
  pass
 
attributeless = NoCustomAttributes()
 
try:
  attributeless.fake_attribute
except AttributeError:
  print("This text gets printed!")
 
# prints "This text gets printed!"

hasattr(attributeless, "fake_attribute")
# returns False
 
getattr(attributeless, "other_fake_attribute", 800)
# returns 800, the default value

can_we_count_it = [{'s': False}, "sassafrass", 18, ["a", "c", "s", "d", "s"]]

for element in can_we_count_it:
  if hasattr(element, "count"):
    print(str(type(element)) + " has the count attribute!")
  else:
    print(str(type(element)) + " does not have the count attribute :(")
# Output:
# <class 'dict'> does not have the count attribute :(
# <class 'str'> has the count attribute!
# <class 'int'> does not have the count attribute :(
# <class 'list'> has the count attribute!

#
### Self
#

class Circle:
  pi = 3.14
  def __init__(self, diameter):
    print("Creating circle with diameter {d}".format(d=diameter))
    self.radius = diameter / 2
  def circumference(self):
    return 2 * self.pi * self.radius

medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)

print(medium_pizza.circumference())
print(teaching_table.circumference())
print(round_room.circumference())
#Output
# Creating circle with diameter 12
# Creating circle with diameter 36
# Creating circle with diameter 11460
# 37.68
# 113.04
# 35984.4

#
### Everything is an object
#

class FakeDict:
  pass
 
fake_dict = FakeDict()
fake_dict.attribute = "Cool"
 
dir(fake_dict)
# Prints ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__()', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'attribute']

#
### Review
#

class Student:
  def __init__(self, name, year):
    self.name = name
    self.year = year
    self.grades = []

  def add_grade(self, grade):
    if type(grade) is Grade:
      self.grades.append(grade)

class Grade:
  minimum_passing = 65
  def __init__(self, score):
    self.score = score

roger = Student("Roger van der Weyden", 10)
sandro = Student("Sandro Botticelli", 12)
pieter = Student("Pieter Bruegel the Elder", 8)
pieter.add_grade(Grade(100))

