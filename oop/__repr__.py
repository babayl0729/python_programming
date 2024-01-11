# class methods are methods 
# (with the @classmethod) that are not
# concerned with instances, but the class
# itself.

class User:
    active_users = 0

    @classmethod
    # cls is standard for class method
    def display_active_users(cls):
        return f"There are currently {cls.active_users} active users."

    @classmethod
    def from_string(cls,data_str):
        # this will split up the 3 pieces of data
        first,last,age = data_str.split(",")
        # and create a new user using cls
        return cls(first, last, int(age))

    def __init__(self,first,last,age):
        self.first = first
        self.last = last
        self.age = age
        User.active_users += 1
    
    # __repr__ method is one of several ways
    # to provide a nicer string representation.
    def __repr__(self):
        return f"{self.first} is {self.age}"

    def logout(self):
        User.active_users -= 1
        return f"{self.first} has logged out"
    
    def full_name(self):
        return f"{self.first} {self.last}"
    
    def intials(self):
        return f"{self.first[0]}.{self.last[0]}."
    
    def likes(self,thing):
        return f"{self.first} likes {thing}"

    def is_senior(self):
        return self.age >= 65
    
    def birthday(self):
        self.age += 1
        return f"Happy {self.age}th, {self.first}"
    
user1 = User("Joe", "Smith", 68)
user2 = User("Blanca", "Lopez", 41)
print(User.display_active_users())
user1 = User("Joe", "Smith", 68)
user2 = User("Blanca", "Lopez", 41)
print(User.display_active_users())

tom = User.from_string("Tom, Jones, 89")
print(tom.first)
print(tom.full_name())
print(tom.birthday())

j = User("Isabella", "Babay", 10)
j = str(j)
print(j)
