from dataclasses import dataclass
from datetime import date

@dataclass
class Assessments:
    assessment_id: int
    student_id: int
    topic:str
    assessment_date:date
    mentor_name :str
    mentor_feedback:str
    total_score:int 
    