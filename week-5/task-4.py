class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    def role(self):
        return "Employee"

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self,value):
        if value>0:
            self._salary=value
        else:
            self._salary=0

class Manager(Employee):
    def __init__(self,name,salary):
        super().__init__(name,salary)
        self.bonus=0.1

    @property
    def salary(self):
        s=self._salary
        return s+s*self.bonus

    @salary.setter
    def salary(self, value):
        if value > 0:
            self._salary = value
        else:
            self._salary = 0

    def role(self):
        return "Manager"

E1=Employee("Bob",100)
M1=Manager("Anna",100)

list_of_employees=[E1,M1]

for i in list_of_employees:
    print(f"Name:{i.name} | Role:{i.role()} | Salary:{i.salary} $")
