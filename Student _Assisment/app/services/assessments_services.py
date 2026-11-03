
from app.repository import assessments_repo
from app.models.assessments import Assessments

class AssessmentServices:

    def __init__(self, repository: assessments_repo):
        self.repository = repository

    def post_assessment(self, assessment: Assessments):
        assessment = self.repository.post_assessment(assessment)
        return assessment
    
    