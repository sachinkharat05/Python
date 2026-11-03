from app.configuration.dbconnetivity import get_db_connection


class AssessmentScoreRepository:

    def post_assessment_score(self, assessment_score):
        connection = get_db_connection()
        cursor = None

        try:
            cursor = connection.cursor(dictionary=True)
            sql = (
                "INSERT INTO assessment_score "
                "(score_id, assessment_id,criteria_id,marks_obtained) "
                "VALUES (%s, %s, %s %s)"
            )
            values = (assessment_score.score_id, assessment_score.assessment_id,
                      assessment_score.criteria_id, assessment_score.marks_obtained)

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