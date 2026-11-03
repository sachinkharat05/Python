from dataclasses import dataclass

@dataclass

class AssessmentScore:
    score_id :int
    assessment_id :int
    criteria_id :int
    marks_obtained:int