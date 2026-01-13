class Person:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,value):
        if value == "Vi":
            print("name \"Vi\" in not available")
            self.__name="Default Name"
        else:
            self.__name=value

    def hello(self):
        print(f"Hello, my name is {self.name}, i am {self.age} years old, my gender is {self.gender}")

class Student(Person):
    def __init__(self,name,age,gender,student_ID):
        super().__init__(name,age,gender)
        self.student_ID=student_ID

    def hello(self):
        print(f"Hello, my name is {self.name}, i am {self.age} years old, my gender is {self.gender},as well as my student ID is {self.student_ID}")

person=Person("Vi",22,"F")
student=Student("Devid",18,"M", "148852ABC")

person.hello()
student.hello()