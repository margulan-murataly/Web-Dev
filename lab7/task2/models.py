class Animal:
    def __init__(self,name,age,color):
        self.name= name
        self.age= age
        self.color = color
    def eat(self):
        return self.name + " eat "
    def speak(self):
        return self.name + ' is speak '
    def __str__(self):
        return "Name: "+self.name + ", Age: "+ str(self.age) + ", Color: "+ self.color
    
class Dog(Animal):
    def __init__(self, name, age, color, stray):
        super().__init__(name, age, color)
        self.stray = stray
    
    def eat(self):
        return self.name + " eat bone"
    
    def speak(self):
        return self.name + " barks"
    
    

    
    
class Cat(Animal):
    def __init__(self, name, age, color, breed):
        super().__init__(name, age, color)
        self.breed = breed
    
    def eat(self):
        return self.name + " eat fish"
    
    def speak(self):
        return self.name + " meow"