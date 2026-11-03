
from app.repository import student_repo
from app.models.student import Student 

class studentservices:

    def __init__(self, repository: student_repo):
        self.repository = repository

    def post_student(self,student: Student):
        student = self.repository.post_student(student)
        return student
    
    