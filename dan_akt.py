from mysql.connector import connect, Error
try:
    with connect(host="localhost", user="root", password="", database="kinostudia") 											as connection:
        insert_aktyor_query = """
INSERT INTO aktyor (fio_ak, age_ak, navik_ak, films_ak,premi_ak)
VALUES
    ("Arnold Sh.Z.", 1947, "53 goda","Terminator","Mister Olimpia"),
    ("Dwayne Jonson", 1972, "28 let","Forsaj","Dorogoy akter")
"""
        with connection.cursor() as cursor:
            cursor.execute(insert_aktyor_query)
            connection.commit()

except Error as e:
    print(e)
