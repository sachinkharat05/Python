from app.configuration.dbconnetivity import get_db_connection



class StudentRepository:

    def post_student(self, student):
        connection = get_db_connection()
        cursor = None

        try:
            cursor = connection.cursor(dictionary=True)
            sql = (
                "INSERT INTO student "
                "(student_id, student_name) "
                "VALUES (%s, %s)"
            )
            values = (student.student_id, student.student_name)

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