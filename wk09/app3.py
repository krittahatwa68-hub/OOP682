from models.classroom import ClassRoom
from models.Student import student

oop = ClassRoom("OOP")
oop.add_student(student(1,"Alice",20,"S001"))
oop.add_student(student(2,"John",80,"S002"))
print(f'{oop.name} registered {len(oop)} students')
oop.add_student(student(3,"Charlie",21,"S003"))
print(len(oop))
print('Students in the class:')
for i in range(len(oop)):
    print(oop[i])