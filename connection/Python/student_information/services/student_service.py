from datetime import date

from repositories.student_repository import (
    add_assessment,
    add_student,
    get_all_students,
)

def list_students():
    return get_all_students()

def create_student(student):
    if not student.get("student_name"):
        raise ValueError("Student name is required.")

    if not student.get("python_topic"):
        raise ValueError("Python topic is required.")

    return add_student(student)

def create_assessment(assessment):
    student = assessment.get("student")
    if not isinstance(student, dict):
        raise ValueError("Student details are required.")

    name = student.get("name")
    if not isinstance(name, str) or not name.strip():
        raise ValueError("Student name is required.")
    if len(name.strip()) > 100:
        raise ValueError("Student name must be 100 characters or fewer.")

    topic = student.get("topic", "")
    mentor = student.get("mentor", "")
    if not isinstance(topic, str) or len(topic) > 150:
        raise ValueError("Python topic must be 150 characters or fewer.")
    if not isinstance(mentor, str) or len(mentor) > 100:
        raise ValueError("Evaluating mentor must be 100 characters or fewer.")

    assessment_date = student.get("date") or None
    if assessment_date is not None:
        if not isinstance(assessment_date, str):
            raise ValueError("Assessment date must use YYYY-MM-DD format.")
        try:
            parsed_date = date.fromisoformat(assessment_date)
        except ValueError:
            raise ValueError("Assessment date must use YYYY-MM-DD format.") from None
        if parsed_date.isoformat() != assessment_date:
            raise ValueError("Assessment date must use YYYY-MM-DD format.")

    scores = assessment.get("scores")
    if (
        not isinstance(scores, list)
        or len(scores) != 10
        or any(type(score) is not int or score < 0 or score > 10 for score in scores)
    ):
        raise ValueError("Provide exactly 10 whole-number scores from 0 to 10.")

    total = assessment.get("total")
    if type(total) is not int or total != sum(scores):
        raise ValueError("Total score must match the sum of the 10 scores.")

    feedback = assessment.get("feedback", "")
    if not isinstance(feedback, str):
        raise ValueError("Mentor feedback must be text.")

    return add_assessment({
        "student_name": name.strip(),
        "python_topic": topic,
        "evaluating_mentor": mentor,
        "assessment_date": assessment_date,
        "scores": scores,
        "total_score": total,
        "mentor_feedback": feedback,
    })