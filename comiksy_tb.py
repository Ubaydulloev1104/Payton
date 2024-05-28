from mysql.connector import connect, Error
try:
    with connect(host="localhost", user="root", password="", database="kinostudia") 											as connection:
        create_comiksy_table_query = """
            CREATE TABLE comiksy(
                idcom INT AUTO_INCREMENT PRIMARY KEY,
                nazcom VARCHAR(100),
                godcom YEAR(4),
                proizcom VARCHAR(100),
                pisatelcom VARCHAR(100),
                hudojcom VARCHAR(100))
            """
        with connection.cursor() as cursor:
            cursor.execute(create_comiksy_table_query)
            connection.commit()
except Error as e:
    print(e)
