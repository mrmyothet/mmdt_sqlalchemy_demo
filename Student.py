class Student:
    def __init__(self, name, age, academic_year):
        self.name = name
        self.age = age
        self.acedemic_year = academic_year

    def setFullName(self, full_name):
        self.name = full_name

    def getName(self):
        return self.name
    
    def getAge(self):
        return self.age
    
    def getAcademicYear(self):
        return self.acedemic_year
