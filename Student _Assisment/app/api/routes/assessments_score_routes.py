from fastapi import (APIRouter,Depends,Request)

from app.models.assessment_score import AssessmentScore

from app.services.assessment_score_services import AssessmentScoreServices



assessment_score_router = APIRouter(prefix="/api/assessment-scores", tags=["assessment-scores"])

def get_assessment_score_services(request: Request) -> AssessmentScoreServices:
    return request.app.state.assessment_score_service

@assessment_score_router.post("/")
def post_assessment_score(
    assessment_score: AssessmentScore,
    service: AssessmentScoreServices = Depends(get_assessment_score_services),
):
    rows_affected = service.post_assessment_score(assessment_score)

    return {
        "message": "Assessment score created",
        "rows_affected": rows_affected,
    }
    service: AssessmentScoreServices = Depends(get_assessment_score_services),

   