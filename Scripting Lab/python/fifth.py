class Person:
    def __init__(self,name,age):
        self.name=name;
        self.age=age;
p1=Person("Supandi",14)
p2=Person("Ramu",12)
print("\nname of 1st person is",p1.name)
print("\nage of 1st person is",p1.age)
print("\nname of 2nd person is",p2.name)
print("\nage of 2nd person is",p2.age)
#modifying p2 age
p2.age=10
print("Modified age of p2 is",p2.age)