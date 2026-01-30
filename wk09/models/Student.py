from models.person import person 

class student(person):
    def __init__(self,pid,name,age,student_id):
        super().__init__(pid,name,age)
        self.student_id = student_id
    def __str__(self):
        return f"Student_ID :{self.student_id}, Name: {self.name}, Age: {self.age}"