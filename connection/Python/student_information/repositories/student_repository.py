import json

from config.database import get_connection

def get_all_students():
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("SELECT * FROM students ORDER BY id DESC")
    students = cursor.fetchall()

    cursor.close()
    connection.close()
    return students

def add_student(student):
    connection = get_connection()
    cursor = connection.cursor()

    sql = """
        INSERT INTO students
        (student_name, student_code, python_topic, evaluating_mentor, assessment_date)
        VALUES (%s, %s, %s, %s, %s)
    """

    values = (
        student["student_name"],
        student.get("student_code"),
        student["python_topic"],
        student.get("evaluating_mentor"),
        student.get("assessment_date"),
    )

    cursor.execute(sql, values)
    connection.commit()
    student_id = cursor.lastrowid

    cursor.close()
    connection.close()
    return student_id

def add_assessment(assessment):
    connection = get_connection()
    try:
        cursor = connection.cursor()
        try:
            sql = """
                INSERT INTO assessments
                (student_name, python_topic, evaluating_mentor, assessment_date,
                 scores, total_score, mentor_feedback)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            values = (
                assessment["student_name"],
                assessment["python_topic"],
                assessment["evaluating_mentor"],
                assessment["assessment_date"],
                json.dumps(assessment["scores"]),
                assessment["total_score"],
                assessment["mentor_feedback"],
            )

            cursor.execute(sql, values)
            connection.commit()
            return cursor.lastrowid
        finally:
            cursor.close()
    finally:
        connection.close()