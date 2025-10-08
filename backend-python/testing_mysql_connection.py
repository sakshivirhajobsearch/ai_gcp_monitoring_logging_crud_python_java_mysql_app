import mysql.connector
from config import MYSQL_CONFIG

try:
    conn = mysql.connector.connect(**MYSQL_CONFIG)
    if conn.is_connected():
        print("✅ MySQL connection successful!")
    conn.close()
except mysql.connector.Error as err:
    print(f"❌ MySQL connection error: {err}")
