import mysql.connector

def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="1301",
        database="FerreteriaAlbania_23270042"
    )

def crear_categoria():
    nombre = input("Ingrese el nombre de la categoría: ")
    descripcion = input("Ingrese la descripción de la categoría: ")
    conexion = conectar()
    cursor = conexion.cursor()
    sql = "INSERT INTO Categoria (nombre, descripcion) VALUES (%s, %s)"
    try:
        cursor.execute(sql, (nombre, descripcion))
        conexion.commit()
        print("Categoría creada con éxito.")
    except mysql.connector.Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        conexion.close()

def leer_categorias():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM Categoria")
    categorias = cursor.fetchall()
    print("\nCategorías registradas:")
    for categoria in categorias:
        print(categoria)
    cursor.close()
    conexion.close()

def actualizar_categoria():
    id_categoria = input("Ingrese el ID de la categoría a actualizar: ")
    nuevo_nombre = input("Ingrese el nuevo nombre de la categoría: ")
    nueva_descripcion = input("Ingrese la nueva descripción de la categoría: ")
    conexion = conectar()
    cursor = conexion.cursor()
    sql = "UPDATE Categoria SET nombre = %s, descripcion = %s WHERE id_categoria = %s"
    try:
        cursor.execute(sql, (nuevo_nombre, nueva_descripcion, id_categoria))
        conexion.commit()
        print("Categoría actualizada con éxito.")
    except mysql.connector.Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        conexion.close()

def eliminar_categoria():
    id_categoria = input("Ingrese el ID de la categoría a eliminar: ")
    conexion = conectar()
    cursor = conexion.cursor()
    sql = "DELETE FROM Categoria WHERE id_categoria = %s"
    try:
        cursor.execute(sql, (id_categoria,))
        conexion.commit()
        print("Categoría eliminada con éxito.")
    except mysql.connector.Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        conexion.close()

def crear_proveedor():
    nombre = input("Ingrese el nombre del proveedor: ")
    contacto = input("Ingrese el contacto del proveedor: ")
    telefono = input("Ingrese el teléfono del proveedor: ")
    direccion = input("Ingrese la dirección del proveedor: ")
    conexion = conectar()
    cursor = conexion.cursor()
    sql = "INSERT INTO Proveedor (nombre, contacto, telefono, direccion) VALUES (%s, %s, %s, %s)"
    try:
        cursor.execute(sql, (nombre, contacto, telefono, direccion))
        conexion.commit()
        print("Proveedor creado con éxito.")
    except mysql.connector.Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        conexion.close()

def leer_proveedores():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM Proveedor")
    proveedores = cursor.fetchall()
    print("\nProveedores registrados:")
    for proveedor in proveedores:
        print(proveedor)
    cursor.close()
    conexion.close()

def actualizar_proveedor():
    id_proveedor = input("Ingrese el ID del proveedor a actualizar: ")
    nuevo_nombre = input("Ingrese el nuevo nombre del proveedor: ")
    nuevo_contacto = input("Ingrese el nuevo contacto del proveedor: ")
    nuevo_telefono = input("Ingrese el nuevo teléfono del proveedor: ")
    nueva_direccion = input("Ingrese la nueva dirección del proveedor: ")
    conexion = conectar()
    cursor = conexion.cursor()
    sql = "UPDATE Proveedor SET nombre = %s, contacto = %s, telefono = %s, direccion = %s WHERE id_proveedor = %s"
    try:
        cursor.execute(sql, (nuevo_nombre, nuevo_contacto, nuevo_telefono, nueva_direccion, id_proveedor))
        conexion.commit()
        print("Proveedor actualizado con éxito.")
    except mysql.connector.Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        conexion.close()

def eliminar_proveedor():
    id_proveedor = input("Ingrese el ID del proveedor a eliminar: ")
    conexion = conectar()
    cursor = conexion.cursor()
    sql = "DELETE FROM Proveedor WHERE id_proveedor = %s"
    try:
        cursor.execute(sql, (id_proveedor,))
        conexion.commit()
        print("Proveedor eliminado con éxito.")
    except mysql.connector.Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        conexion.close()

def menu():
    while True:
        print("\nMenú de Opciones:")
        print("1. Crear categoría")
        print("2. Leer categorías")
        print("3. Actualizar categoría")
        print("4. Eliminar categoría")
        print("5. Crear proveedor")
        print("6. Leer proveedores")
        print("7. Actualizar proveedor")
        print("8. Eliminar proveedor")
        print("9. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            crear_categoria()
        elif opcion == "2":
            leer_categorias()
        elif opcion == "3":
            actualizar_categoria()
        elif opcion == "4":
            eliminar_categoria()
        elif opcion == "5":
            crear_proveedor()
        elif opcion == "6":
            leer_proveedores()
        elif opcion == "7":
            actualizar_proveedor()
        elif opcion == "8":
            eliminar_proveedor()
        elif opcion == "9":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, intente nuevamente.")

if __name__ == "__main__":
    menu()
