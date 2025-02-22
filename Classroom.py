from Student import Student
from typing import List

class Classroom:
    def __init__(self, name:str, lst_students:List[Student]):
        self.name = name
        self.lst_students = lst_students

    def get_all_student_names(self):
        if len(self.lst_students) > 0:
            return [x.name for x in self.lst_students]
        else:
            return f"There is no student in the classroom {self.name}"

    def addStudent(self, new_student:Student):
        if not isinstance(new_student, Student):
            raise TypeError("Sorry, you must be student to enroll.")
        
        if new_student in self.lst_students:
            return "This student is already enrolled."

        # for student in self.lst_students:
        #     if student == new_student:
        #         return "This student is already enrolled"
            
        self.lst_students.append(new_student)

    def removeStudent(self, student_to_remove:Student):
        self.lst_students.remove(student_to_remove)
        print(f"{student_to_remove.name} is removed from classroom {self.name}")