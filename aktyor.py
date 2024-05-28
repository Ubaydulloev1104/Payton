from mysql.connector import connect, Error
try:
    with connect(host="localhost", user="root", password="", database="kinostudia") 											as connection:
        create_aktyor_table_query = """
            CREATE TABLE aktyor(
                id_ak INT AUTO_INCREMENT PRIMARY KEY,
                fio_ak  VARCHAR(150),
                age_ak  YEAR(4),
                navik_ak  VARCHAR(100),
                films_ak  VARCHAR(150),
                premi_ak  VARCHAR(100))
                
            """
        with connection.cursor() as cursor:
            cursor.execute(create_aktyor_table_query)
            connection.commit()
except Error as e:
    print(e)
