
from app.repository import  evaluation_repo
from app.models.evaluation_criteria import EvaluationCriteria

class EvaluationServices:

    def __init__(self, repository: evaluation_repo):
        self.repository = repository

    def post_evaluation_criteria(self, evaluation_criteria: EvaluationCriteria):
        evaluation_criteria = self.repository.post_evaluation_criteria(evaluation_criteria)
        return evaluation_criteria
    
    