from fastapi import (APIRouter,Depends,Request)

from app.services.student_services import studentservices
from app.models.student import Student


student_router = APIRouter(prefix="/api/student", tags=["student"])

def get_student_services(request: Request) -> studentservices:
    return request.app.state.student_service

@student_router.post("/")
def post_student(
    student: Student,
    service: studentservices = Depends(get_student_services),
):
    rows_affected = service.post_student(student)

    return {
        "message": "Student created successfully",
        "rows_affected": rows_affected,
    }