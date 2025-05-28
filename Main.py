from course import Course
from student import Student

math = Course("Algebra I")
language = Course("Spanish I")
science = Course("Earth Science")
history = Course("U.S. History I")
phys_ed = Course("Physical Education I")

orchestra = Course("Honors Chamber Orchestra")
art = Course("Drawing & Design")

test_student = Student("Jill", "Sample")
test_student.add_course(math)
test_student.add_course(language)
test_student.add_course(science)
test_student.add_course(history)

test_student2 = Student("Bill", "Sample")
test_student2.add_course(math)
test_student2.add_course(phys_ed)
test_student2.add_course(science)
test_student2.add_course(history)

test_student3 = Student("Sally", "Sample")
test_student3.add_course(art)
test_student3.add_course(orchestra)
test_student3.add_course(language)
test_student3.add_course(math)

allStudents = []
allStudents.append(test_student)
allStudents.append(test_student2)
allStudents.append(test_student3)

print(allStudents)

print(test_student)
print(test_student2)
print(test_student3)

#Only Name Code

"""
from course import Course
from student import Student

math = Course("Algebra I")
language = Course("Spanish I")
science = Course("Earth Science")
history = Course("U.S. History I")
phys_ed = Course("Physical Education I")

orchestra = Course("Honors Chamber Orchestra")
art = Course("Drawing & Design")

test_student = Student("Jill", "James")
test_student.add_course(math)
test_student.add_course(language)
test_student.add_course(science)
test_student.add_course(history)

test_student2 = Student("Bill", "Bob")
test_student2.add_course(math)
test_student2.add_course(phys_ed)
test_student2.add_course(science)
test_student2.add_course(history)

test_student3 = Student("Sally", "Sample")
test_student3.add_course(art)
test_student3.add_course(orchestra)
test_student3.add_course(language)
test_student3.add_course(math)

allStudents = []
allStudents.append(test_student)
allStudents.append(test_student2)
allStudents.append(test_student3)

#print(allStudents)

print(test_student.get_name())
print(test_student2.get_name())
print(test_student3.get_name())
"""
