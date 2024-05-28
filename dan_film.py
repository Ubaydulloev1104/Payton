from mysql.connector import connect, Error
try:
    with connect(host="localhost", user="root", password="", database="kinostudia") 											as connection:
        insert_film_query = """
INSERT INTO film (nazv,god,rejisyor,genre,doh)
VALUES
    ("Mstiteli", 2012, "Kevin Faygi","Fantastika",730000000),
    ("Hishnik", 2018, "Djon Uidon","Boevik",200000000),
    ("Jizn za god", 2018, "Uil Smit","Drama",420000000)
"""
        with connection.cursor() as cursor:
            cursor.execute(insert_film_query)
            connection.commit()

except Error as e:
    print(e)
