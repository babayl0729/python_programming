class Aquatic:
    def __init__(self,name):
        print("AQUATIC INIT")
        self.name = name
    
    def swim(self):
        return f"{self.name} is swimming"
    
    def greet(self):
        return f"I am {self.name} of the sea!"
    
class Ambulatory:
    def __init__(self,name):
        print("AMBULATORY INIT")
        self.name = name
    
    def walk(self):
        return f"{self.name} is walking"
    
    def greet(self):
        return f"I am {self.name} of the land!"
    
class Penguin(Aquatic,Ambulatory):
    def __init__(self,name):
        super().__init__(name=name)

jaws = Aquatic("Jaws")
lassie =  Ambulatory("Lassie")
captain_cook = Penguin("Captain Cook")

print(captain_cook.swim())
print(captain_cook.walk())
print(captain_cook.greet())