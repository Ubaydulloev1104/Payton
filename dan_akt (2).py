from mysql.connector import connect, Error
try:
    with connect(host="localhost", user="root", password="", database="kinostudia") 											as connection:
        insert_aktyor_query = """
INSERT INTO aktyor (fio_ak, age_ak, navik_ak, films_ak,premi_ak)
VALUES
    ("Arnold Sh.Z.", 1947, "53 goda","Terminator","Mister Olimpia"),
    ("Dwayne Jonson", 1972, "28 let","Forsaj","Dorogoy akter"),
    ("Silvester Stalone", 1946, "50 let","Neuderjimie","Oscar"),
    ("Robert D.Jr.", 1965, "52 goda","Iron Man","Zolotoy Globus"),
    ("Tolibov M.Z.", 2003, "4 goda","Jo Reil","Zolotaya Malina")
"""
        with connection.cursor() as cursor:
            cursor.execute(insert_aktyor_query)
            connection.commit()

except Error as e:
    print(e)
