# _name - it signify something is for 
# internal use. pure convention.
# __name - it's not conventional, it changes name
# it's called name mangling.
# __name__ - it's a convention it's used for
# python specific methods like __init__

class Person:
    def __init__(self):
        self.name = "Tony"
        self._secret = "hi!"
        self.__msg = "I like dogs!"
        self.__lol = "HEHEHE"

p = Person()
print(p.name)
print(p._secret)
print(dir(p))
print(p._secret)
print(p._Person__msg)
print(p._Person__lol)