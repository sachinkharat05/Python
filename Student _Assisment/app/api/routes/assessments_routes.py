from fastapi import (APIRouter,Depends,Request)

from app.models.assessments import Assessments

from app.services.assessments_services import  AssessmentServices



assessments_router = APIRouter(prefix="/api/assessments", tags=["assessments"])

def get_assessments_services(request: Request) -> AssessmentServices:
    return request.app.state.assessments_service

@assessments_router.post("/")
def post_assessment(
    assessment: Assessments,
    service: AssessmentServices = Depends(get_assessments_services),
):
    rows_affected = service.post_assessment(assessment)

    return {
        "message": "Assessment created",
        "rows_affected": rows_affected,
    }
    service: AssessmentServices = Depends(get_assessments_services),

   