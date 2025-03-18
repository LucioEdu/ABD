import mysql.connector

# Repositorio de GitHub: https://github.com/LucioEdu/ABD

def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="1301",
        database="dbtaller_23270042"
    )

def crear_tipo():
    tipo = input("Ingrese el tipo de proyecto: ")
    conexion = conectar()
    cursor = conexion.cursor()
    sql = "INSERT INTO tipoProyecto (tipo) VALUES (%s)"
    try:
        cursor.execute(sql, (tipo,))
        conexion.commit()
        print("Tipo de proyecto creado con éxito.")
    except mysql.connector.Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        conexion.close()

def leer_tipos():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM tipoProyecto")
    tipos = cursor.fetchall()
    print("\nTipos de proyecto registrados:")
    for tipo in tipos:
        print(tipo)
    cursor.close()
    conexion.close()

def actualizar_tipo():
    id_actual = input("Ingrese el ID actual del tipo de proyecto: ")
    nuevo_tipo = input("Ingrese el nuevo tipo de proyecto: ")
    conexion = conectar()
    cursor = conexion.cursor()
    sql = "UPDATE tipoProyecto SET tipo = %s WHERE id_tipo = %s"
    try:
        cursor.execute(sql, (nuevo_tipo, id_actual))
        conexion.commit()
        print("Tipo de proyecto actualizado.")
    except mysql.connector.Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        conexion.close()

def eliminar_tipo():
    id_tipo = input("Ingrese el ID del tipo de proyecto a eliminar: ")
    conexion = conectar()
    cursor = conexion.cursor()
    sql = "DELETE FROM tipoProyecto WHERE id_tipo = %s"
    try:
        cursor.execute(sql, (id_tipo,))
        conexion.commit()
        print("Tipo de proyecto eliminado.")
    except mysql.connector.Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        conexion.close()

def menu():
    while True:
        print("\nMenú de Opciones:")
        print("1. Crear tipo de proyecto")
        print("2. Leer tipos de proyecto")
        print("3. Actualizar tipo de proyecto")
        print("4. Eliminar tipo de proyecto")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            crear_tipo()
        elif opcion == "2":
            leer_tipos()
        elif opcion == "3":
            actualizar_tipo()
        elif opcion == "4":
            eliminar_tipo()
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, intente nuevamente.")

if __name__ == "__main__":
    menu()
