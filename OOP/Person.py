class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Employee(Person):
    def  __init__(self, name, age, salary):
       super().__init__(name, age)
       self.salary = salary
    def infoEmployee(self):
       print(f"name: {self.name} age: {self.age} salary: {self.salary}")


class Talaba:
    def __init__(self,name,age,type):
        self.name=name
        self.age=age
        self.type=type
class Abiturient(Talaba):
    def __init__(self, name, age, type,salary):
        super().__init__(name, age, type)
        self.salary=salary
    def Gap(self):
        print(12345)

