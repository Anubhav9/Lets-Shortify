import mysql.connector
from mysql.connector import Error
import os
import logging
import constants

logging.basicConfig(level=logging.INFO)

def connect_to_db():
    try:
        connection=mysql.connector.connect(
            host=constants.DB_HOST,
            user=constants.DB_USER,
            password=os.environ.get("MYSQL_ROOT_PASSWORD"),
            port=constants.DB_PORT,
            database=constants.DB_NAME
        )
        if(connection.is_connected()):
            logging.info("Connection is successful with the database")
            return connection
    except Error as e:
        logging.error("Error in connecting to database with Error as ",e)

    return connection

def insert_hashed_url_into_db(user_input,hashed_output):
    connection=connect_to_db()
    cursor = connection.cursor()
    sql_query_to_insert="INSERT into url_mapping (actual_url,hashed_url) VALUES (%s,%s)"
    values=(user_input,hashed_output)
    try:
        cursor.execute(sql_query_to_insert,values)
        connection.commit()
    except Error as e:
        logging.error("Cannot execute the statement with Error as ",e)
    cursor.close()
    connection.close()


def get_actual_url_from_hashed_url_db(hashed_url):
    connection=connect_to_db()
    cursor = connection.cursor(dictionary=True)
    sql_query="SELECT actual_url from url_mapping WHERE hashed_url=%s"
    value=hashed_url
    try:
        cursor.execute(sql_query,(hashed_url),)
        result=cursor.fetchall()
    except Error as e:
        logging.error("Cannot execute the statement with error as ",e)

    cursor.close()
    connection.close()
    return result

def check_record_exists_in_db(actual_url):
    connection=connect_to_db()
    cursor=connection.cursor()
    sql_query="SELECT COUNT(*) from url_mapping where actual_url=%s"
    value=actual_url
    cursor.execute(sql_query,(value,))
    result=cursor.fetchone()
    result_count=result[0]
    return result_count
