from mysql.connector import connect, Error
try:
    with connect(host="localhost",user="root",password="") as connection:
        #print(connection)
        create_db_query = "CREATE DATABASE kinostudia"
        with connection.cursor() as cursor:
            cursor.execute(create_db_query)
except Error as e:
    print(e)
