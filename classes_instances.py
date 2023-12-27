class User:
    # classes in python can have a special 
    # __init__ method, which gets called every
    # time you create an instance of the class
    # (instantiate).
    # every time you make a new class you 
    # need to have a __init__ method.
    # Well.. almost every time.
    # There are some special cases. You might
    # define a class that only holds methods
    # and no data. You wouldn't need an 
    # __init__ methods in that case(rare!).

    # self keyword refers to specific instance of 
    # the class. 
    # Technically, the parameter deosn't have to be
    # called self, but it is the standard and pretty
    # much the only thing you'll see.
    def __init__(self,first,last,age):
        self.first = first
        self.last = last
        self.age = age


user1 = User("Joe", "Smith", 68)
user2 = User("Blanca", "Lopez", 41)
print(user1.first, user1.last, user1.age)
print(user2.first, user2.last, user2.age)




