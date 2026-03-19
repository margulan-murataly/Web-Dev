from models import Animal,Dog,Cat


an1= Animal("JustAnimal", 10, "Red")
an2= Dog("Rex", 12, "Gray","Yes")
an3= Cat("Murka", 4, "white", "Persian")

animals = [an1, an2, an3]
for anim in animals:
    print(anim)
    print(anim.eat())
    print(anim.speak())
    print()