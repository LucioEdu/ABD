import mysql.connector

def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="1301",
        database="dbtaller_23270042"
    )

def crear_linea():
    clave_linea = input("Ingrese la clave de la línea de investigación: ")
    conexion = conectar()
    cursor = conexion.cursor()
    sql = "INSERT INTO lineaInvestigacion (clave_linea) VALUES (%s)"
    try:
        cursor.execute(sql, (clave_linea,))
        conexion.commit()
        print("Línea de investigación creada con éxito.")
    except mysql.connector.Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        conexion.close()

def leer_lineas():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM lineaInvestigacion")
    lineas = cursor.fetchall()
    print("\nLíneas de investigación registradas:")
    for linea in lineas:
        print(linea)
    cursor.close()
    conexion.close()

def actualizar_linea():
    clave_actual = input("Ingrese la clave actual de la línea de investigación: ")
    nueva_clave = input("Ingrese la nueva clave de la línea de investigación: ")
    conexion = conectar()
    cursor = conexion.cursor()
    sql = "UPDATE lineaInvestigacion SET clave_linea = %s WHERE clave_linea = %s"
    try:
        cursor.execute(sql, (nueva_clave, clave_actual))
        conexion.commit()
        print("Línea de investigación actualizada.")
    except mysql.connector.Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        conexion.close()

def eliminar_linea():
    clave_linea = input("Ingrese la clave de la línea de investigación a eliminar: ")
    conexion = conectar()
    cursor = conexion.cursor()
    sql = "DELETE FROM lineaInvestigacion WHERE clave_linea = %s"
    try:
        cursor.execute(sql, (clave_linea,))
        conexion.commit()
        print("Línea de investigación eliminada.")
    except mysql.connector.Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        conexion.close()

def menu():
    while True:
        print("\nMenú de Opciones:")
        print("1. Crear línea de investigación")
        print("2. Leer líneas de investigación")
        print("3. Actualizar línea de investigación")
        print("4. Eliminar línea de investigación")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            crear_linea()
        elif opcion == "2":
            leer_lineas()
        elif opcion == "3":
            actualizar_linea()
        elif opcion == "4":
            eliminar_linea()
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, intente nuevamente.")

if __name__ == "__main__":
    menu()