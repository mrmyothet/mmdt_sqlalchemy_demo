from Student import Student
from Classroom import Classroom

s1 = Student("Sat Paing", 18, 2025)
s2 = Student("A Thet", 19, 2025)
s3 = Student("Myo Thet", 38, 2025)

cs = Classroom("Computer Science", [])
print(cs.get_all_student_names())

# cs.addStudent("Student Name")

cs.addStudent(s1)
cs.addStudent(s2)
cs.addStudent(s3)

print(cs.get_all_student_names())

cs.removeStudent(s1)
print(cs.get_all_student_names())