
from app.repository import assessment_score_repo
from app.models.assessment_score import AssessmentScore

class AssessmentScoreServices:

    def __init__(self, repository: assessment_score_repo):
        self.repository = repository

    def post_assessment_score(self, assessment_score: AssessmentScore):
        assessment_score = self.repository.post_assessment_score(assessment_score)
        return assessment_score
    
    