# classes in python can have a special 
# __init__ method, which gets called every
# time you create an instance of the class
# (instantiate).
# every time you make a new class you 
# need to have a __init__ method.
# A User class with 3 attributes but no methods (aside from __init__)
class User:
	def __init__(self, first, last, age):
		self.first = first
		self.last = last
		self.age = age

user1 = User("Joe","Smith", 68)
user2 = User("Blanca", "Lopez", 41)
print(user1.first, user1.last, user1.age)
print(user2.first, user2.last, user2.age)






