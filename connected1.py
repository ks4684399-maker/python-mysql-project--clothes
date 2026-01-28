import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",        # apna username
    password="MySqlKhushi@123",    # apna password
    database="clothes"   # apna database
)

if conn.is_connected():
    print("Connected ✅")
else:
    print("Not Connected ❌")

conn.close()