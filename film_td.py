from mysql.connector import connect, Error
try:
    with connect(host="localhost", user="root", password="", database="kinostudia") 											as connection:
        create_film_table_query = """
            CREATE TABLE film(
                id INT AUTO_INCREMENT PRIMARY KEY,
                nazv VARCHAR(100),
                god YEAR(4),
                rejisyor VARCHAR(100),
                genre VARCHAR(100),
                doh INT)
            """
        with connection.cursor() as cursor:
            cursor.execute(create_film_table_query)
            connection.commit()
except Error as e:
    print(e)
