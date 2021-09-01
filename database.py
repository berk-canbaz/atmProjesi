import sqlite3 as s

connection = s.connect("customers.db")

cursor = connection.execute("select * from info")

data = cursor.fetchall()

connection.close()


def update_customer(yeni_deger, kart_no):
    connection = s.connect("customers.db")

    connection.execute("update info set balance = " + str(yeni_deger) + " where cardno = " + kart_no)

    connection.commit()
    connection.close()
