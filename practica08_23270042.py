import mysql.connector

config = {
    "host": "localhost", 
    "user": "root",
    "password": "1301",
    "database": "dbtaller_23270042"
}

try:
    conexion = mysql.connector.connect(**config)

    if conexion.is_connected():
        print("Conexión exitosa a MySQL")
    
    conexion.close()

except mysql.connector.Error as e:
    print(f"Error al conectar a MySQL: {e}")
