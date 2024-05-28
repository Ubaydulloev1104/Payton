from mysql.connector import connect, Error
try:
    with connect(host="localhost", user="root", password="", database="kinostudia") 											as connection:
        insert_comiksy_query = """
INSERT INTO comiksy (nazcom,godcom,proizcom,pisatelcom,hudojcom)
VALUES
    ("Chelovek Pauk", 2022, "Marvel","Kevin Faygi","Hiruzen Kagawi"),
    ("Superman", 2022, "DC","Djon Uik","Kianu Rivz"),
    ("Boruto", 2022, "FPO","Itachi Uchiha","Madara Uchiha")
"""
        with connection.cursor() as cursor:
            cursor.execute(insert_comiksy_query)
            connection.commit()

except Error as e:
    print(e)
