from mysql.connector import connect, Error
try:
    with connect(host="localhost", user="root", password="", database="kinostudia") 											as connection:
        select_aktyor_query = """
        select * from aktyor 
            order By age_ak
            FROM movies
            ORDER BY collection_in_mil DESC
"""
        with connection.cursor() as cursor:
            cursor.execute(select_aktyor_query)
            for aktyor in cursor.fetchmany(size=5):
                print(aktyor)
            cursor.fetchall()
except Error as e:
    print(e)
