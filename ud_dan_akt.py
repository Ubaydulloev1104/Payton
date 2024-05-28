from mysql.connector import connect, Error
try:
    with connect(host="localhost", user="root", password="", database="kinostudia") 											as connection:
        insert_aktyor_query = """
delete from aktyor
 where  id_ak=7
"""
        with connection.cursor() as cursor:
            cursor.execute(insert_aktyor_query)
            connection.commit()

except Error as e:
    print(e)
