#del function to delete attributes of an object and an object itself
class Person:
    def __init__(self,name,age):
        self.name=name;
        self.age=age;
p1=Person("Supandi",14)
print("\n name is",p1.name)
print("\n age is",p1.age)

print("After deleting age attribute for p1")
del p1.age
print("\nName of person is",p1.name)
del p1