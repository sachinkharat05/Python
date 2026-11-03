from fastapi import (APIRouter,Depends,Request)

from app.models.evaluation_criteria import EvaluationCriteria
from app.services.evaluation_services import EvaluationServices



evaluation_router = APIRouter(prefix="/api/evaluation", tags=["evaluation"])

def get_evaluation_services(request: Request) -> EvaluationServices:
    return request.app.state.evaluation_service

@evaluation_router.post("/")
def post_evaluation_criteria(
    evaluation_criteria: EvaluationCriteria,
    service: EvaluationServices = Depends(get_evaluation_services),
):
    rows_affected = service.post_evaluation_criteria(evaluation_criteria)

    return {
        "message": "Evaluation criteria created successfully",
        "rows_affected": rows_affected,
    }