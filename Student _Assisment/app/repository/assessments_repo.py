from app.configuration.dbconnetivity import get_db_connection


class AssessmentRepository:

    def post_assessments(self, assessments):
        connection = get_db_connection()
        cursor = None

        try:
            cursor = connection.cursor(dictionary=True)
            sql = (
                "INSERT INTO assessments "
                "(assessment_id, student_id,topic,assessment_date,mentor_name,mentor_feedback,total_score) "
                "VALUES (%s, %s, %s, %s, %s, %s, %s)"
            )
            values = (assessments.assessment_id, assessments.student_id, assessments.topic, assessments.assessment_date, 
                      assessments.mentor_name, assessments.mentor_feedback, assessments.total_score)

            cursor.execute(sql, values)
            connection.commit()
            return cursor.rowcount
        except Exception:
            connection.rollback()
            raise
        finally:
            if cursor is not None:
                cursor.close()
            connection.close()