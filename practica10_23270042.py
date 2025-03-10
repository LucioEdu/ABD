import mysql.connector

# Repositorio de GitHub: https://github.com/LucioEdu/ABD

def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="1301",
        database="dbtaller_23270042"
    )

def crear_profesor():
    nombre = input("Ingrese el nombre del profesor: ")
    conexion = conectar()
    cursor = conexion.cursor()
    sql = "INSERT INTO profesor (nombre) VALUES (%s)"
    try:
        cursor.execute(sql, (nombre,))
        conexion.commit()
        print("Profesor creado con éxito.")
    except mysql.connector.Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        conexion.close()

def leer_profesores():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM profesor")
    profesores = cursor.fetchall()
    print("\nProfesores registrados:")
    for profesor in profesores:
        print(profesor)
    cursor.close()
    conexion.close()

def actualizar_profesor():
    id_profesor = input("Ingrese el ID del profesor a actualizar: ")
    nuevo_nombre = input("Ingrese el nuevo nombre del profesor: ")
    conexion = conectar()
    cursor = conexion.cursor()
    sql = "UPDATE profesor SET nombre = %s WHERE id_profesor = %s"
    try:
        cursor.execute(sql, (nuevo_nombre, id_profesor))
        conexion.commit()
        print("Profesor actualizado con éxito.")
    except mysql.connector.Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        conexion.close()

def eliminar_profesor():
    id_profesor = input("Ingrese el ID del profesor a eliminar: ")
    conexion = conectar()
    cursor = conexion.cursor()
    sql = "DELETE FROM profesor WHERE id_profesor = %s"
    try:
        cursor.execute(sql, (id_profesor,))
        conexion.commit()
        print("Profesor eliminado con éxito.")
    except mysql.connector.Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        conexion.close()

def menu():
    while True:
        print("\nMenú de Profesores:")
        print("1. Crear profesor")
        print("2. Leer profesores")
        print("3. Actualizar profesor")
        print("4. Eliminar profesor")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            crear_profesor()
        elif opcion == "2":
            leer_profesores()
        elif opcion == "3":
            actualizar_profesor()
        elif opcion == "4":
            eliminar_profesor()
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, intente nuevamente.")

if __name__ == "__main__":
    menu()
