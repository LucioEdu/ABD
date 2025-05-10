import sys
import mysql.connector
from PyQt6.QtWidgets import (
    QApplication, QWidget, QDoubleSpinBox, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QDateEdit, QFormLayout,
    QLineEdit, QTableWidget, QTableWidgetItem, QStackedWidget, QComboBox, QHeaderView, QMessageBox, QSpinBox
)
from PyQt6.QtCore import Qt

# ----------- Conexión MySQL -----------

conexion = mysql.connector.connect(
    host='localhost',
    user='root',
    password='1301',
    database='ferreteriaalbania_23270042'
)

# ----------- Funciones MySQL -----------

# Funciones Cliente
def obtener_clientes():
    cursor = conexion.cursor()
    cursor.execute("SELECT id_cliente, nombre, telefono, email, rfc, direccion FROM cliente")
    return cursor.fetchall()

def insertar_cliente(nombre, telefono, email, rfc, direccion):
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO cliente (nombre, telefono, email, rfc, direccion) VALUES (%s, %s, %s, %s, %s)", 
                   (nombre, telefono, email, rfc, direccion))
    conexion.commit()

def actualizar_cliente(id_cliente, nombre, telefono, email, rfc, direccion):
    cursor = conexion.cursor()
    cursor.execute("UPDATE cliente SET nombre = %s, telefono = %s, email = %s, rfc = %s, direccion = %s WHERE id_cliente = %s", 
                   (nombre, telefono, email, rfc, direccion, id_cliente))
    conexion.commit()

def eliminar_cliente(id_cliente):
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM cliente WHERE id_cliente = %s", (id_cliente,))
    conexion.commit()

# Funciones Proveedor
def obtener_proveedores():
    cursor = conexion.cursor()
    cursor.execute("SELECT id_proveedor, nombre, telefono, email, direccion, ciudad, estado, pais FROM proveedor")
    return cursor.fetchall()

def insertar_proveedor(nombre, telefono, email, direccion, ciudad, estado, pais):
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO proveedor (nombre, telefono, email, direccion, ciudad, estado, pais) VALUES (%s, %s, %s, %s, %s, %s, %s)", 
                   (nombre, telefono, email, direccion, ciudad, estado, pais))
    conexion.commit()

def actualizar_proveedor(id_proveedor, nombre, telefono, email, direccion, ciudad, estado, pais):
    cursor = conexion.cursor()
    cursor.execute("UPDATE proveedor SET nombre = %s, telefono = %s, email = %s, direccion = %s, ciudad = %s, estado = %s, pais = %s WHERE id_proveedor = %s", 
                   (nombre, telefono, email, direccion, ciudad, estado, pais, id_proveedor))
    conexion.commit()

def eliminar_proveedor(id_proveedor):
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM proveedor WHERE id_proveedor = %s", (id_proveedor,))
    conexion.commit()

# Funciones Artículo
def obtener_articulos():
    cursor = conexion.cursor()
    cursor.execute("SELECT id_articulo, nombre, descripcion, precio, id_categoria, id_proveedor, stock FROM articulo")
    return cursor.fetchall()

def insertar_articulo(nombre, descripcion, precio, id_categoria, id_proveedor, stock):
    cursor = conexion.cursor()
    cursor.execute(
        "INSERT INTO articulo (nombre, descripcion, precio, id_categoria, id_proveedor, stock) VALUES (%s, %s, %s, %s, %s, %s)",
        (nombre, descripcion, precio, id_categoria, id_proveedor, stock)
    )
    conexion.commit()

def actualizar_articulo(id_articulo, nombre, descripcion, precio, id_categoria, id_proveedor, stock):
    cursor = conexion.cursor()
    cursor.execute(
        "UPDATE articulo SET nombre = %s, descripcion = %s, precio = %s, id_categoria = %s, id_proveedor = %s, stock = %s WHERE id_articulo = %s",
        (nombre, descripcion, precio, id_categoria, id_proveedor, stock, id_articulo)
    )
    conexion.commit()

def eliminar_articulo(id_articulo):
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM articulo WHERE id_articulo = %s", (id_articulo,))
    conexion.commit()

# Funciones Categoría
def obtener_categorias():
    cursor = conexion.cursor()
    cursor.execute("SELECT id_categoria, nombre FROM categoria")
    return cursor.fetchall()

def insertar_categoria(nombre):
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO categoria (nombre) VALUES (%s)", (nombre,))
    conexion.commit()

def actualizar_categoria(id_categoria, nombre):
    cursor = conexion.cursor()
    cursor.execute("UPDATE categoria SET nombre = %s WHERE id_categoria = %s", (nombre, id_categoria))
    conexion.commit()

def eliminar_categoria(id_categoria):
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM categoria WHERE id_categoria = %s", (id_categoria,))
    conexion.commit()

# Funciones Empleados
def obtener_empleados():
    cursor = conexion.cursor()
    cursor.execute("SELECT id_empleado, nombre, puesto, salario, telefono FROM empleado")
    return cursor.fetchall()

def insertar_empleado(nombre, puesto, salario, telefono):
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO empleado (nombre, puesto, salario, telefono) VALUES (%s, %s, %s, %s)",
                   (nombre, puesto, salario, telefono))
    conexion.commit()

def actualizar_empleado(id_empleado, nombre, puesto, salario, telefono):
    cursor = conexion.cursor()
    cursor.execute("UPDATE empleado SET nombre = %s, puesto = %s, salario = %s, telefono = %s WHERE id_empleado = %s",
                   (nombre, puesto, salario, telefono, id_empleado))
    conexion.commit()

def eliminar_empleado(id_empleado):
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM empleado WHERE id_empleado = %s", (id_empleado,))
    conexion.commit()

# Funciones Compra y Detalle Compra
def obtener_compras():
    cursor = conexion.cursor()
    cursor.execute("SELECT id_compra, total, fecha, proveedor_id_proveedor FROM compra")
    return cursor.fetchall()

def insertar_compra(total, fecha, proveedor_id_proveedor):
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO compra (total, fecha, proveedor_id_proveedor) VALUES (%s, %s, %s)", 
                   (total, fecha, proveedor_id_proveedor))
    conexion.commit()
    return cursor.lastrowid

def insertar_detalle_compra(compra_id_compra, articulo_id_articulo, cantidad, precio_unitario):
    cursor = conexion.cursor()

    cursor.execute("SELECT nombre FROM articulo WHERE id_articulo = %s", (articulo_id_articulo,))
    articulo_nombre = cursor.fetchone()

    if articulo_nombre:
        articulo_nombre = articulo_nombre[0]
    else:
        raise ValueError("Artículo no encontrado")

    cursor.execute("""
        INSERT INTO detallecompra (nombre_articulo, cantidad, precio_unitario, articulo_id_articulo, compra_id_compra)
        VALUES (%s, %s, %s, %s, %s)
    """, (articulo_nombre, cantidad, precio_unitario, articulo_id_articulo, compra_id_compra))

    conexion.commit()

def actualizar_stock(articulo_id_articulo, cantidad):
    cursor = conexion.cursor()
    cursor.execute("UPDATE articulo SET stock = stock + %s WHERE id_articulo = %s", (cantidad, articulo_id_articulo))
    conexion.commit()

# Funciones Venta y Detalle Venta
def obtener_ventas():
    cursor = conexion.cursor()
    cursor.execute("""
        SELECT id_venta, total, fecha, cliente_id_cliente, empleado_id_empleado
        FROM venta
    """)
    return cursor.fetchall()

def insertar_venta(total, fecha, cliente_id_cliente, empleado_id_empleado):
    cursor = conexion.cursor()
    cursor.execute("""
        INSERT INTO venta (total, fecha, cliente_id_cliente, empleado_id_empleado)
        VALUES (%s, %s, %s, %s)
    """, (total, fecha, cliente_id_cliente, empleado_id_empleado))
    conexion.commit()
    return cursor.lastrowid

def insertar_detalle_venta(venta_id_venta, articulo_id_articulo, cantidad, precio_unitario):
    cursor = conexion.cursor()

    cursor.execute("SELECT nombre FROM articulo WHERE id_articulo = %s", (articulo_id_articulo,))
    articulo_nombre = cursor.fetchone()

    if articulo_nombre:
        articulo_nombre = articulo_nombre[0]
    else:
        raise ValueError("Artículo no encontrado")

    cursor.execute("""
        INSERT INTO detalleventa (nombre_articulo, cantidad, precio_unitario, articulo_id_articulo, venta_id_venta)
        VALUES (%s, %s, %s, %s, %s)
    """, (articulo_nombre, cantidad, precio_unitario, articulo_id_articulo, venta_id_venta))

    conexion.commit()

def descontar_stock(articulo_id_articulo, cantidad):
    cursor = conexion.cursor()
    cursor.execute("UPDATE articulo SET stock = stock - %s WHERE id_articulo = %s", (cantidad, articulo_id_articulo))
    conexion.commit()

def obtener_id_cliente_por_nombre(nombre_cliente):
    cursor = conexion.cursor()
    cursor.execute("SELECT id_cliente FROM cliente WHERE nombre = %s", (nombre_cliente,))
    resultado = cursor.fetchone()
    if resultado:
        return resultado[0]
    return None 

def obtener_id_empleado_por_nombre(nombre_empleado):
    cursor = conexion.cursor()
    cursor.execute("SELECT id_empleado FROM empleado WHERE nombre = %s", (nombre_empleado,))
    resultado = cursor.fetchone()
    if resultado:
        return resultado[0] 
    return None

def obtener_id_articulo_por_nombre(nombre_articulo):
    cursor = conexion.cursor()
    cursor.execute("SELECT id_articulo FROM articulo WHERE nombre = %s", (nombre_articulo,))
    resultado = cursor.fetchone()
    if resultado:
        return resultado[0]
    return None 

# ----------- CRUD Cliente -----------

class ClienteCRUD(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout()

        self.titulo = QLabel("Formulario Cliente")
        self.titulo.setStyleSheet("font-size: 18px; font-weight: bold;")
        self.layout.addWidget(self.titulo)

        self.nombre_input = QLineEdit()
        self.nombre_input.setPlaceholderText("Nombre")

        self.telefono_input = QLineEdit()
        self.telefono_input.setPlaceholderText("Teléfono")

        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("Email")

        self.rfc_input = QLineEdit()
        self.rfc_input.setPlaceholderText("RFC")

        self.direccion_input = QLineEdit()
        self.direccion_input.setPlaceholderText("Dirección")

        self.boton_layout = QHBoxLayout()

        self.btn_agregar = QPushButton("Agregar")
        self.btn_agregar.clicked.connect(self.agregar_cliente)
        self.boton_layout.addWidget(self.btn_agregar)

        self.btn_actualizar = QPushButton("Actualizar")
        self.btn_actualizar.clicked.connect(self.actualizar_cliente)
        self.boton_layout.addWidget(self.btn_actualizar)

        self.btn_eliminar = QPushButton("Eliminar")
        self.btn_eliminar.clicked.connect(self.eliminar_cliente)
        self.boton_layout.addWidget(self.btn_eliminar)

        self.layout.addWidget(self.nombre_input)
        self.layout.addWidget(self.telefono_input)
        self.layout.addWidget(self.email_input)
        self.layout.addWidget(self.rfc_input)
        self.layout.addWidget(self.direccion_input)
        self.layout.addLayout(self.boton_layout)

        self.label_lista = QLabel("Lista de Clientes")
        self.label_lista.setStyleSheet("font-size: 16px; font-weight: bold;")
        self.layout.addWidget(self.label_lista)

        self.tabla = QTableWidget()
        self.tabla.setColumnCount(6)
        self.tabla.setHorizontalHeaderLabels(["ID", "Nombre", "Teléfono", "Email", "RFC", "Dirección"])
        self.tabla.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.tabla.verticalHeader().setVisible(False)
        self.tabla.setEditTriggers(QTableWidget.EditTrigger.DoubleClicked)
        self.layout.addWidget(self.tabla)

        self.nav_layout = QHBoxLayout()

        self.btn_inicio = QPushButton("Inicio")
        self.nav_layout.addWidget(self.btn_inicio)

        self.btn_anterior = QPushButton("Anterior")
        self.nav_layout.addWidget(self.btn_anterior)

        self.btn_siguiente = QPushButton("Siguiente")
        self.nav_layout.addWidget(self.btn_siguiente)

        self.btn_final = QPushButton("Final")
        self.nav_layout.addWidget(self.btn_final)

        self.layout.addLayout(self.nav_layout)

        self.setLayout(self.layout)
        self.actualizar_tabla()

    def actualizar_tabla(self):
        datos = obtener_clientes()
        self.tabla.setRowCount(0)
        for fila_num, fila_datos in enumerate(datos):
            self.tabla.insertRow(fila_num)
            for col, valor in enumerate(fila_datos):
                self.tabla.setItem(fila_num, col, QTableWidgetItem(str(valor)))

    def agregar_cliente(self):
        nombre = self.nombre_input.text()
        telefono = self.telefono_input.text()
        email = self.email_input.text()
        rfc = self.rfc_input.text()
        direccion = self.direccion_input.text()

        if nombre:
            insertar_cliente(nombre, telefono, email, rfc, direccion)
            self.nombre_input.clear()
            self.telefono_input.clear()
            self.email_input.clear()
            self.rfc_input.clear()
            self.direccion_input.clear()
            self.actualizar_tabla()

    def actualizar_cliente(self):
        fila_seleccionada = self.tabla.currentRow()
        if fila_seleccionada == -1:
            QMessageBox.warning(self, "Advertencia", "Selecciona un cliente para actualizar.")
            return

        id_cliente = self.tabla.item(fila_seleccionada, 0).text()
        nombre = self.tabla.item(fila_seleccionada, 1).text()
        telefono = self.tabla.item(fila_seleccionada, 2).text()
        email = self.tabla.item(fila_seleccionada, 3).text()
        rfc = self.tabla.item(fila_seleccionada, 4).text()
        direccion = self.tabla.item(fila_seleccionada, 5).text()

        if nombre and telefono and email and rfc and direccion:
            actualizar_cliente(id_cliente, nombre, telefono, email, rfc, direccion)
            self.actualizar_tabla()
        else:
            QMessageBox.warning(self, "Advertencia", "Llena todos los campos para actualizar.")

    def eliminar_cliente(self):
        fila_seleccionada = self.tabla.currentRow()
        if fila_seleccionada == -1:
            QMessageBox.warning(self, "Advertencia", "Selecciona un cliente para eliminar.")
            return

        id_cliente = self.tabla.item(fila_seleccionada, 0).text()

        confirmacion = QMessageBox.question(
            self, "Confirmación", "¿Estás seguro de eliminar este cliente?", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        if confirmacion == QMessageBox.StandardButton.Yes:
            eliminar_cliente(id_cliente)
            self.actualizar_tabla()

# ----------- CRUD Proveedor -----------

class ProveedorCRUD(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout()

        self.titulo = QLabel("Formulario Proveedor")
        self.titulo.setStyleSheet("font-size: 18px; font-weight: bold;")
        self.layout.addWidget(self.titulo)

        self.nombre_input = QLineEdit()
        self.nombre_input.setPlaceholderText("Nombre")

        self.telefono_input = QLineEdit()
        self.telefono_input.setPlaceholderText("Teléfono")

        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("Email")

        self.direccion_input = QLineEdit()
        self.direccion_input.setPlaceholderText("Dirección")

        self.ciudad_input = QLineEdit()
        self.ciudad_input.setPlaceholderText("Ciudad")

        self.estado_input = QLineEdit()
        self.estado_input.setPlaceholderText("Estado")

        self.pais_input = QLineEdit()
        self.pais_input.setPlaceholderText("País")

        self.boton_layout = QHBoxLayout()

        self.btn_agregar = QPushButton("Agregar")
        self.btn_agregar.clicked.connect(self.agregar_proveedor)
        self.boton_layout.addWidget(self.btn_agregar)

        self.btn_actualizar = QPushButton("Actualizar")
        self.btn_actualizar.clicked.connect(self.actualizar_proveedor)
        self.boton_layout.addWidget(self.btn_actualizar)

        self.btn_eliminar = QPushButton("Eliminar")
        self.btn_eliminar.clicked.connect(self.eliminar_proveedor)
        self.boton_layout.addWidget(self.btn_eliminar)

        self.layout.addWidget(self.nombre_input)
        self.layout.addWidget(self.telefono_input)
        self.layout.addWidget(self.email_input)
        self.layout.addWidget(self.direccion_input)
        self.layout.addWidget(self.ciudad_input)
        self.layout.addWidget(self.estado_input)
        self.layout.addWidget(self.pais_input)
        self.layout.addLayout(self.boton_layout)

        self.label_lista = QLabel("Lista de Proveedores")
        self.label_lista.setStyleSheet("font-size: 16px; font-weight: bold;")
        self.layout.addWidget(self.label_lista)

        self.tabla = QTableWidget()
        self.tabla.setColumnCount(8)
        self.tabla.setHorizontalHeaderLabels(["ID", "Nombre", "Teléfono", "Email", "Dirección", "Ciudad", "Estado", "País"])
        self.tabla.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.tabla.verticalHeader().setVisible(False)
        self.tabla.setEditTriggers(QTableWidget.EditTrigger.DoubleClicked)
        self.layout.addWidget(self.tabla)

        self.setLayout(self.layout)
        self.actualizar_tabla()

    def actualizar_tabla(self):
        datos = obtener_proveedores()
        self.tabla.setRowCount(0)
        for fila_num, fila_datos in enumerate(datos):
            self.tabla.insertRow(fila_num)
            for col, valor in enumerate(fila_datos):
                self.tabla.setItem(fila_num, col, QTableWidgetItem(str(valor)))

    def agregar_proveedor(self):
        nombre = self.nombre_input.text()
        telefono = self.telefono_input.text()
        email = self.email_input.text()
        direccion = self.direccion_input.text()
        ciudad = self.ciudad_input.text()
        estado = self.estado_input.text()
        pais = self.pais_input.text()

        if nombre:
            insertar_proveedor(nombre, telefono, email, direccion, ciudad, estado, pais)
            self.nombre_input.clear()
            self.telefono_input.clear()
            self.email_input.clear()
            self.direccion_input.clear()
            self.ciudad_input.clear()
            self.estado_input.clear()
            self.pais_input.clear()
            self.actualizar_tabla()

    def actualizar_proveedor(self):
        fila_seleccionada = self.tabla.currentRow()
        if fila_seleccionada == -1:
            QMessageBox.warning(self, "Advertencia", "Selecciona un proveedor para actualizar.")
            return

        id_proveedor = self.tabla.item(fila_seleccionada, 0).text()
        nombre = self.tabla.item(fila_seleccionada, 1).text()
        telefono = self.tabla.item(fila_seleccionada, 2).text()
        email = self.tabla.item(fila_seleccionada, 3).text()
        direccion = self.tabla.item(fila_seleccionada, 4).text()
        ciudad = self.tabla.item(fila_seleccionada, 5).text()
        estado = self.tabla.item(fila_seleccionada, 6).text()
        pais = self.tabla.item(fila_seleccionada, 7).text()

        if nombre and telefono and email and direccion and ciudad and estado and pais:
            actualizar_proveedor(id_proveedor, nombre, telefono, email, direccion, ciudad, estado, pais)
            self.actualizar_tabla()
        else:
            QMessageBox.warning(self, "Advertencia", "Llena todos los campos para actualizar.")

    def eliminar_proveedor(self):
        fila_seleccionada = self.tabla.currentRow()
        if fila_seleccionada == -1:
            QMessageBox.warning(self, "Advertencia", "Selecciona un proveedor para eliminar.")
            return

        id_proveedor = self.tabla.item(fila_seleccionada, 0).text()

        confirmacion = QMessageBox.question(
            self, "Confirmación", "¿Estás seguro de eliminar este proveedor?", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        if confirmacion == QMessageBox.StandardButton.Yes:
            eliminar_proveedor(id_proveedor)
            self.actualizar_tabla()

# ----------- CRUD Artículo -----------

class ArticuloCRUD(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()

        self.titulo = QLabel("Formulario Artículo")
        self.titulo.setStyleSheet("font-size: 18px; font-weight: bold;")
        self.layout.addWidget(self.titulo)

        self.nombre_input = QLineEdit()
        self.nombre_input.setPlaceholderText("Nombre")

        self.descripcion_input = QLineEdit()
        self.descripcion_input.setPlaceholderText("Descripción")

        self.precio_input = QLineEdit()
        self.precio_input.setPlaceholderText("Precio")

        self.id_categoria_input = QLineEdit()
        self.id_categoria_input.setPlaceholderText("ID Categoría")

        self.id_proveedor_input = QLineEdit()
        self.id_proveedor_input.setPlaceholderText("ID Proveedor")

        self.stock_input = QLineEdit()
        self.stock_input.setPlaceholderText("Stock")

        self.boton_layout = QHBoxLayout()

        self.btn_agregar = QPushButton("Agregar")
        self.btn_agregar.clicked.connect(self.agregar_articulo)
        self.boton_layout.addWidget(self.btn_agregar)

        self.btn_actualizar = QPushButton("Actualizar")
        self.btn_actualizar.clicked.connect(self.actualizar_articulo)
        self.boton_layout.addWidget(self.btn_actualizar)

        self.btn_eliminar = QPushButton("Eliminar")
        self.btn_eliminar.clicked.connect(self.eliminar_articulo)
        self.boton_layout.addWidget(self.btn_eliminar)

        self.layout.addWidget(self.nombre_input)
        self.layout.addWidget(self.descripcion_input)
        self.layout.addWidget(self.precio_input)
        self.layout.addWidget(self.id_categoria_input)
        self.layout.addWidget(self.id_proveedor_input)
        self.layout.addWidget(self.stock_input)
        self.layout.addLayout(self.boton_layout)

        self.label_lista = QLabel("Lista de Artículos")
        self.label_lista.setStyleSheet("font-size: 16px; font-weight: bold;")
        self.layout.addWidget(self.label_lista)

        self.tabla = QTableWidget()
        self.tabla.setColumnCount(7)
        self.tabla.setHorizontalHeaderLabels([
            "ID", "Nombre", "Descripción", "Precio",
            "ID Categoría", "ID Proveedor", "Stock"
        ])
        self.tabla.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.tabla.verticalHeader().setVisible(False)
        self.tabla.setEditTriggers(QTableWidget.EditTrigger.DoubleClicked)
        self.layout.addWidget(self.tabla)

        self.setLayout(self.layout)
        self.actualizar_tabla()

    def actualizar_tabla(self):
        datos = obtener_articulos()
        self.tabla.setRowCount(0)
        for fila_num, fila_datos in enumerate(datos):
            self.tabla.insertRow(fila_num)
            for col, valor in enumerate(fila_datos):
                self.tabla.setItem(fila_num, col, QTableWidgetItem(str(valor)))

    def agregar_articulo(self):
        nombre = self.nombre_input.text()
        descripcion = self.descripcion_input.text()
        precio = self.precio_input.text()
        id_categoria = self.id_categoria_input.text()
        id_proveedor = self.id_proveedor_input.text()
        stock = self.stock_input.text()

        if nombre and descripcion and precio and id_categoria and id_proveedor and stock:
            try:
                insertar_articulo(
                    nombre, descripcion, float(precio),
                    int(id_categoria), int(id_proveedor), int(stock)
                )
                self.nombre_input.clear()
                self.descripcion_input.clear()
                self.precio_input.clear()
                self.id_categoria_input.clear()
                self.id_proveedor_input.clear()
                self.stock_input.clear()
                self.actualizar_tabla()
            except ValueError:
                QMessageBox.warning(self, "Error", "Precio, ID Categoría, ID Proveedor y Stock deben ser números.")
        else:
            QMessageBox.warning(self, "Advertencia", "Por favor, llena todos los campos.")

    def actualizar_articulo(self):
        fila_seleccionada = self.tabla.currentRow()
        if fila_seleccionada == -1:
            QMessageBox.warning(self, "Advertencia", "Selecciona un artículo para actualizar.")
            return

        id_articulo = self.tabla.item(fila_seleccionada, 0).text()
        nombre = self.tabla.item(fila_seleccionada, 1).text()
        descripcion = self.tabla.item(fila_seleccionada, 2).text()
        precio = self.tabla.item(fila_seleccionada, 3).text()
        id_categoria = self.tabla.item(fila_seleccionada, 4).text()
        id_proveedor = self.tabla.item(fila_seleccionada, 5).text()
        stock = self.tabla.item(fila_seleccionada, 6).text()

        if nombre and descripcion and precio and id_categoria and id_proveedor and stock:
            try:
                actualizar_articulo(
                    int(id_articulo), nombre, descripcion,
                    float(precio), int(id_categoria), int(id_proveedor), int(stock)
                )
                self.actualizar_tabla()
            except ValueError:
                QMessageBox.warning(self, "Error", "Precio, ID Categoría, ID Proveedor y Stock deben ser números.")

    def eliminar_articulo(self):
        fila_seleccionada = self.tabla.currentRow()
        if fila_seleccionada == -1:
            QMessageBox.warning(self, "Advertencia", "Selecciona un artículo para eliminar.")
            return

        id_articulo = self.tabla.item(fila_seleccionada, 0).text()

        confirmacion = QMessageBox.question(
            self, "Confirmación", "¿Estás seguro de eliminar este artículo?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        if confirmacion == QMessageBox.StandardButton.Yes:
            eliminar_articulo(id_articulo)
            self.actualizar_tabla()

# ----------- CRUD Categoría -----------

class CategoriaCRUD(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()

        self.titulo = QLabel("Formulario Categoría")
        self.titulo.setStyleSheet("font-size: 18px; font-weight: bold;")
        self.layout.addWidget(self.titulo)

        self.nombre_input = QLineEdit()
        self.nombre_input.setPlaceholderText("Nombre de la Categoría")
        self.layout.addWidget(self.nombre_input)

        self.boton_layout = QHBoxLayout()

        self.btn_agregar = QPushButton("Agregar")
        self.btn_agregar.clicked.connect(self.agregar_categoria)
        self.boton_layout.addWidget(self.btn_agregar)

        self.btn_actualizar = QPushButton("Actualizar")
        self.btn_actualizar.clicked.connect(self.actualizar_categoria)
        self.boton_layout.addWidget(self.btn_actualizar)

        self.btn_eliminar = QPushButton("Eliminar")
        self.btn_eliminar.clicked.connect(self.eliminar_categoria)
        self.boton_layout.addWidget(self.btn_eliminar)

        self.layout.addLayout(self.boton_layout)

        self.label_lista = QLabel("Lista de Categorías")
        self.label_lista.setStyleSheet("font-size: 16px; font-weight: bold;")
        self.layout.addWidget(self.label_lista)

        self.tabla = QTableWidget()
        self.tabla.setColumnCount(2)
        self.tabla.setHorizontalHeaderLabels(["ID", "Nombre"])
        self.tabla.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.tabla.verticalHeader().setVisible(False)
        self.tabla.setEditTriggers(QTableWidget.EditTrigger.DoubleClicked)
        self.layout.addWidget(self.tabla)

        self.setLayout(self.layout)
        self.actualizar_tabla()

    def actualizar_tabla(self):
        datos = obtener_categorias()
        self.tabla.setRowCount(0)
        for fila_num, fila_datos in enumerate(datos):
            self.tabla.insertRow(fila_num)
            for col, valor in enumerate(fila_datos):
                self.tabla.setItem(fila_num, col, QTableWidgetItem(str(valor)))

    def agregar_categoria(self):
        nombre = self.nombre_input.text()
        if nombre:
            insertar_categoria(nombre)
            self.nombre_input.clear()
            self.actualizar_tabla()

    def actualizar_categoria(self):
        fila_seleccionada = self.tabla.currentRow()
        if fila_seleccionada == -1:
            QMessageBox.warning(self, "Advertencia", "Selecciona una categoría para actualizar.")
            return

        id_categoria = self.tabla.item(fila_seleccionada, 0).text()
        nombre = self.tabla.item(fila_seleccionada, 1).text()

        if nombre:
            actualizar_categoria(id_categoria, nombre)
            self.actualizar_tabla()

    def eliminar_categoria(self):
        fila_seleccionada = self.tabla.currentRow()
        if fila_seleccionada == -1:
            QMessageBox.warning(self, "Advertencia", "Selecciona una categoría para eliminar.")
            return

        id_categoria = self.tabla.item(fila_seleccionada, 0).text()

        confirmacion = QMessageBox.question(
            self, "Confirmación", "¿Estás seguro de eliminar esta categoría?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        if confirmacion == QMessageBox.StandardButton.Yes:
            eliminar_categoria(id_categoria)
            self.actualizar_tabla()

# ----------- CRUD Empleado -----------

class EmpleadoCRUD(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()

        self.titulo = QLabel("Formulario Empleado")
        self.titulo.setStyleSheet("font-size: 18px; font-weight: bold;")
        self.layout.addWidget(self.titulo)

        self.nombre_input = QLineEdit()
        self.nombre_input.setPlaceholderText("Nombre")

        self.puesto_input = QLineEdit()
        self.puesto_input.setPlaceholderText("Puesto")

        self.salario_input = QLineEdit()
        self.salario_input.setPlaceholderText("Salario")

        self.telefono_input = QLineEdit()
        self.telefono_input.setPlaceholderText("Teléfono")

        self.boton_layout = QHBoxLayout()

        self.btn_agregar = QPushButton("Agregar")
        self.btn_agregar.clicked.connect(self.agregar_empleado)
        self.boton_layout.addWidget(self.btn_agregar)

        self.btn_actualizar = QPushButton("Actualizar")
        self.btn_actualizar.clicked.connect(self.actualizar_empleado)
        self.boton_layout.addWidget(self.btn_actualizar)

        self.btn_eliminar = QPushButton("Eliminar")
        self.btn_eliminar.clicked.connect(self.eliminar_empleado)
        self.boton_layout.addWidget(self.btn_eliminar)

        self.layout.addWidget(self.nombre_input)
        self.layout.addWidget(self.puesto_input)
        self.layout.addWidget(self.salario_input)
        self.layout.addWidget(self.telefono_input)
        self.layout.addLayout(self.boton_layout)

        self.label_lista = QLabel("Lista de Empleados")
        self.label_lista.setStyleSheet("font-size: 16px; font-weight: bold;")
        self.layout.addWidget(self.label_lista)

        self.tabla = QTableWidget()
        self.tabla.setColumnCount(5)
        self.tabla.setHorizontalHeaderLabels(["ID", "Nombre", "Puesto", "Salario", "Teléfono"])
        self.tabla.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.tabla.verticalHeader().setVisible(False)
        self.tabla.setEditTriggers(QTableWidget.EditTrigger.DoubleClicked)
        self.layout.addWidget(self.tabla)

        self.setLayout(self.layout)
        self.actualizar_tabla()

    def actualizar_tabla(self):
        datos = obtener_empleados()
        self.tabla.setRowCount(0)
        for fila_num, fila_datos in enumerate(datos):
            self.tabla.insertRow(fila_num)
            for col, valor in enumerate(fila_datos):
                self.tabla.setItem(fila_num, col, QTableWidgetItem(str(valor)))

    def agregar_empleado(self):
        nombre = self.nombre_input.text()
        puesto = self.puesto_input.text()
        salario = self.salario_input.text()
        telefono = self.telefono_input.text()

        if nombre and puesto and salario and telefono:
            try:
                insertar_empleado(nombre, puesto, float(salario), telefono)
                self.nombre_input.clear()
                self.puesto_input.clear()
                self.salario_input.clear()
                self.telefono_input.clear()
                self.actualizar_tabla()
            except ValueError:
                QMessageBox.warning(self, "Error", "El salario debe ser un número.")

    def actualizar_empleado(self):
        fila = self.tabla.currentRow()
        if fila == -1:
            QMessageBox.warning(self, "Advertencia", "Selecciona un empleado para actualizar.")
            return

        id_empleado = self.tabla.item(fila, 0).text()
        nombre = self.tabla.item(fila, 1).text()
        puesto = self.tabla.item(fila, 2).text()
        salario = self.tabla.item(fila, 3).text()
        telefono = self.tabla.item(fila, 4).text()

        if nombre and puesto and salario and telefono:
            try:
                actualizar_empleado(id_empleado, nombre, puesto, float(salario), telefono)
                self.actualizar_tabla()
            except ValueError:
                QMessageBox.warning(self, "Error", "El salario debe ser un número.")

    def eliminar_empleado(self):
        fila = self.tabla.currentRow()
        if fila == -1:
            QMessageBox.warning(self, "Advertencia", "Selecciona un empleado para eliminar.")
            return

        id_empleado = self.tabla.item(fila, 0).text()
        confirmacion = QMessageBox.question(
            self, "Confirmación", "¿Estás seguro de eliminar este empleado?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        if confirmacion == QMessageBox.StandardButton.Yes:
            eliminar_empleado(id_empleado)
            self.actualizar_tabla()

# ----------- CRUD Compra -----------

class CompraCRUD(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout()
        self.setWindowTitle("Formulario de Compra")

        self.fecha_input = QDateEdit()
        self.fecha_input.setDisplayFormat("yyyy-MM-dd")

        self.proveedor_input = QComboBox()
        self.cargar_proveedores()

        self.articulo_input = QComboBox()
        self.cargar_articulos()

        self.cantidad_input = QSpinBox()
        self.cantidad_input.setMinimum(1)

        self.precio_input = QLineEdit()
        self.precio_input.setPlaceholderText("Precio Unitario")

        self.total_input = QLineEdit()
        self.total_input.setPlaceholderText("Total")
        self.total_input.setReadOnly(True)

        self.boton_layout = QHBoxLayout()

        self.btn_agregar = QPushButton("Agregar Compra")
        self.btn_agregar.clicked.connect(self.agregar_compra)
        self.boton_layout.addWidget(self.btn_agregar)

        self.tabla_compras = QTableWidget()
        self.tabla_compras.setColumnCount(4)
        self.tabla_compras.setHorizontalHeaderLabels(["ID Compra", "Fecha", "Proveedor", "Total"])
        self.tabla_compras.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.tabla_compras.verticalHeader().setVisible(False)
        self.tabla_compras.setEditTriggers(QTableWidget.EditTrigger.DoubleClicked)
        self.layout.addWidget(self.fecha_input)
        self.layout.addWidget(self.proveedor_input)
        self.layout.addWidget(self.articulo_input)
        self.layout.addWidget(self.cantidad_input)
        self.layout.addWidget(self.precio_input)
        self.layout.addWidget(self.total_input)
        self.layout.addLayout(self.boton_layout)
        self.layout.addWidget(self.tabla_compras)

        self.setLayout(self.layout)

        self.cargar_compras()

    def cargar_proveedores(self):
        cursor = conexion.cursor()
        cursor.execute("SELECT id_proveedor, nombre FROM proveedor")
        proveedores = cursor.fetchall()
        for proveedor in proveedores:
            self.proveedor_input.addItem(proveedor[1], proveedor[0])

    def cargar_articulos(self):
        cursor = conexion.cursor()
        cursor.execute("SELECT id_articulo, nombre FROM articulo")
        articulos = cursor.fetchall()
        for articulo in articulos:
            self.articulo_input.addItem(articulo[1], articulo[0])

    def agregar_compra(self):
        fecha = self.fecha_input.text()
        proveedor_id_proveedor = self.proveedor_input.currentData()
        articulo_id_articulo = self.articulo_input.currentData()
        cantidad = self.cantidad_input.value()
        precio_unitario = float(self.precio_input.text())

        if fecha and proveedor_id_proveedor and articulo_id_articulo and cantidad and precio_unitario:
            total = cantidad * precio_unitario
            self.total_input.setText(f"{total:.2f}")

            compra_id_compra = insertar_compra(total, fecha, proveedor_id_proveedor)

            insertar_detalle_compra(compra_id_compra, articulo_id_articulo, cantidad, precio_unitario)

            self.cantidad_input.setValue(1)
            self.precio_input.clear()

            self.cargar_compras()

            QMessageBox.information(self, "Éxito", "Compra registrada correctamente.")
        else:
            QMessageBox.warning(self, "Advertencia", "Por favor llena todos los campos.")

    def cargar_compras(self):
        cursor = conexion.cursor()
        cursor.execute("SELECT c.id_compra, c.fecha, p.nombre, c.total FROM compra c JOIN proveedor p ON c.proveedor_id_proveedor = p.id_proveedor")
        compras = cursor.fetchall()

        self.tabla_compras.setRowCount(0)

        for row_number, row_data in enumerate(compras):
            self.tabla_compras.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tabla_compras.setItem(row_number, column_number, QTableWidgetItem(str(data)))

# ----------- CRUD Venta -----------

class VentaCRUD(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Registro de Venta")
        layout = QVBoxLayout(self)

        form_layout = QFormLayout()
        self.fecha_input = QLineEdit()
        self.fecha_input.setPlaceholderText("YYYY-MM-DD")

        self.total_input = QLineEdit()
        self.total_input.setReadOnly(True)

        self.cliente_combo = QComboBox()
        self.cliente_combo.addItems([row[1] for row in obtener_clientes()])

        self.empleado_combo = QComboBox()
        self.empleado_combo.addItems([row[1] for row in obtener_empleados()])

        form_layout.addRow("Fecha:", self.fecha_input)
        form_layout.addRow("Total:", self.total_input)
        form_layout.addRow("Cliente:", self.cliente_combo)
        form_layout.addRow("Empleado:", self.empleado_combo)

        self.articulo_combo = QComboBox()
        self.articulo_combo.addItems([a[1] for a in obtener_articulos()])

        self.articulo_combo.currentIndexChanged.connect(self.actualizar_precio)

        self.cantidad_input = QSpinBox()
        self.cantidad_input.setRange(1, 1000)
        self.cantidad_input.valueChanged.connect(self.calcular_total)

        form_layout.addRow("Artículo:", self.articulo_combo)
        form_layout.addRow("Cantidad:", self.cantidad_input)

        self.btn_guardar = QPushButton("Registrar Venta")
        self.btn_guardar.clicked.connect(self.agregar_venta)

        layout.addLayout(form_layout)
        layout.addWidget(self.btn_guardar)

        self.tabla_ventas = QTableWidget()
        layout.addWidget(self.tabla_ventas)
        self.tabla_ventas.setColumnCount(5)
        self.tabla_ventas.setHorizontalHeaderLabels(["ID", "Total", "Fecha", "Cliente", "Empleado"])
        self.tabla_ventas.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.mostrar_ventas()

        self.precio_unitario = 0.0

    def actualizar_precio(self):
        articulo_nombre = self.articulo_combo.currentText()
        precio = self.obtener_precio_articulo(articulo_nombre)
        self.precio_unitario = precio
        self.calcular_total()

    def obtener_precio_articulo(self, nombre_articulo):
        cursor = conexion.cursor()
        cursor.execute("SELECT precio FROM articulo WHERE nombre = %s", (nombre_articulo,))
        resultado = cursor.fetchone()
        if resultado:
            return resultado[0]
        return 0.0

    def calcular_total(self):
        cantidad = self.cantidad_input.value()
        total = cantidad * self.precio_unitario
        self.total_input.setText(f"{total:.2f}")

    def agregar_venta(self):
        fecha = self.fecha_input.text()
        total = float(self.total_input.text())
        cliente_nombre = self.cliente_combo.currentText()
        empleado_nombre = self.empleado_combo.currentText()

        cliente_id = obtener_id_cliente_por_nombre(cliente_nombre)
        empleado_id = obtener_id_empleado_por_nombre(empleado_nombre)

        if not cliente_id or not empleado_id:
            print("Error: Cliente o Empleado no encontrado.")
            return

        venta_id = insertar_venta(total, fecha, cliente_id, empleado_id)

        articulo_nombre = self.articulo_combo.currentText()
        articulo_id = obtener_id_articulo_por_nombre(articulo_nombre)

        if not articulo_id:
            print("Error: Artículo no encontrado.")
            return

        cantidad = self.cantidad_input.value()

        insertar_detalle_venta(venta_id, articulo_id, cantidad, self.precio_unitario)
        self.mostrar_ventas()

    def mostrar_ventas(self):
        datos = obtener_ventas()
        self.tabla_ventas.setRowCount(len(datos))
        for row_idx, row_data in enumerate(datos):
            for col_idx, value in enumerate(row_data):
                self.tabla_ventas.setItem(row_idx, col_idx, QTableWidgetItem(str(value)))

# ----------- Ventana Principal -----------

class VentanaPrincipal(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sistema Ferretería La Albania")
        self.setGeometry(100, 100, 1000, 600)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.stack = QStackedWidget()
        self.cliente_crud = ClienteCRUD()
        self.proveedor_crud = ProveedorCRUD()
        self.articulo_crud = ArticuloCRUD()
        self.categoria_crud = CategoriaCRUD()
        self.empleado_crud = EmpleadoCRUD()

        self.compra_detalle_crud = CompraCRUD()

        self.venta_crud = VentaCRUD()

        self.stack.addWidget(self.cliente_crud)
        self.stack.addWidget(self.proveedor_crud)
        self.stack.addWidget(self.articulo_crud)
        self.stack.addWidget(self.categoria_crud)
        self.stack.addWidget(self.empleado_crud)
        self.stack.addWidget(self.compra_detalle_crud)
        self.stack.addWidget(self.venta_crud)

        self.botones_menu = QHBoxLayout()

        self.btn_clientes = QPushButton("Clientes")
        self.btn_clientes.clicked.connect(lambda: self.stack.setCurrentWidget(self.cliente_crud))
        self.botones_menu.addWidget(self.btn_clientes)

        self.btn_proveedores = QPushButton("Proveedores")
        self.btn_proveedores.clicked.connect(lambda: self.stack.setCurrentWidget(self.proveedor_crud))
        self.botones_menu.addWidget(self.btn_proveedores)

        self.btn_articulos = QPushButton("Artículos")
        self.btn_articulos.clicked.connect(lambda: self.stack.setCurrentWidget(self.articulo_crud))
        self.botones_menu.addWidget(self.btn_articulos)

        self.btn_categorias = QPushButton("Categorías")
        self.btn_categorias.clicked.connect(lambda: self.stack.setCurrentWidget(self.categoria_crud))
        self.botones_menu.addWidget(self.btn_categorias)

        self.btn_empleados = QPushButton("Empleados")
        self.btn_empleados.clicked.connect(lambda: self.stack.setCurrentWidget(self.empleado_crud))
        self.botones_menu.addWidget(self.btn_empleados)

        self.btn_compras = QPushButton("Compras")
        self.btn_compras.clicked.connect(lambda: self.stack.setCurrentWidget(self.compra_detalle_crud))
        self.botones_menu.addWidget(self.btn_compras)

        self.btn_ventas = QPushButton("Ventas")
        self.btn_ventas.clicked.connect(lambda: self.stack.setCurrentWidget(self.venta_crud))
        self.botones_menu.addWidget(self.btn_ventas)

        self.layout.addLayout(self.botones_menu)
        self.layout.addWidget(self.stack)


# ----------- Main -----------

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec())