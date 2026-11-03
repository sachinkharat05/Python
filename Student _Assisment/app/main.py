from fastapi import FastAPI

from app.api.routes.student_routes import student_router
from app.api.routes.evaulation_criteria_routes import evaluation_router
from app.api.routes.assessments_routes import assessments_router
from app.api.routes.assessments_score_routes import assessment_score_router

from app.repository.student_repo import StudentRepository
from app.repository.evaluation_repo import EvaluationRepository
from app.repository.assessments_repo import AssessmentRepository
from app.repository.assessment_score_repo import AssessmentScoreRepository

from app.services.student_services import studentservices
from app.services.evaluation_services import EvaluationServices
from app.services.assessments_services import AssessmentServices
from app.services.assessment_score_services import AssessmentScoreServices


app = FastAPI(title="functionality API",description="Video Assessment REST API",version="1.0")

#student 
student_repository = StudentRepository()  #object creation
app.state.student_service = studentservices(student_repository)  #dependency injection
# Register API routes
app.include_router(student_router)

#evaluation criteria
evaluation_repository = EvaluationRepository()  #object creation
app.state.evaluation_service = EvaluationServices(evaluation_repository)  #dependency injection 
app.include_router(evaluation_router)

#assessments
assessments_repository = AssessmentRepository()  #object creation
app.state.assessments_service = AssessmentServices(assessments_repository)  #dependency injection
app.include_router(assessments_router)

#assessment score
assessment_score_repository = AssessmentScoreRepository()  #object creation
app.state.assessment_score_service = AssessmentScoreServices(assessment_score_repository)  #dependency injection
app.include_router(assessment_score_router) 