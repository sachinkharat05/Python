from app.configuration.dbconnetivity import get_db_connection


class EvaluationRepository:

    def post_evaluation_criteria(self, evaluation_criteria):
        connection = get_db_connection()
        cursor = None

        try:
            cursor = connection.cursor(dictionary=True)
            sql = (
                "INSERT INTO evaluation_criteria "
                "(criteria_id, criteria_name,max_marks) "
                "VALUES (%s, %s ,%s)"
            )
            values = (evaluation_criteria.criteria_id, evaluation_criteria.criteria_name, evaluation_criteria.max_marks)

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
        