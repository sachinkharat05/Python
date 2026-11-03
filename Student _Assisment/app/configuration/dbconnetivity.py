import mysql.connector

def get_db_connection():
    dbconnection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="sakshi1805",
        database="video_assessment")
    return dbconnection