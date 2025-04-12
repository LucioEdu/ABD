import sys
import mysql.connector
from PyQt6.QtWidgets import (
    QApplication, QWidget, QMainWindow, QVBoxLayout, QHBoxLayout, QLabel, QPushButton,
    QLineEdit, QTableWidget, QTableWidgetItem, QStackedWidget, QComboBox, QHeaderView, QMessageBox
)
from PyQt6.QtCore import Qt

# ------------------ Conexión MySQL ------------------

conexion = mysql.connector.connect(
    host='localhost',
    user='root',
    password='1301',
    database='ferreteriaalbania_23270042'
)

# ------------------ Funciones MySQL ------------------

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

# ------------------ CRUD Cliente ------------------

class ClienteCRUD(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout()

        self.titulo = QLabel("Formulario Cliente")
        self.titulo.setStyleSheet("font-size: 18px; font-weight: bold;")
        self.layout.addWidget(self.titulo)

        # Agregar campos para RFC y Dirección
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

        # Fila con botones de Agregar, Actualizar y Eliminar
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
        self.tabla.setColumnCount(6)  # Ahora son 6 columnas
        self.tabla.setHorizontalHeaderLabels(["ID", "Nombre", "Teléfono", "Email", "RFC", "Dirección"])
        self.tabla.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.tabla.verticalHeader().setVisible(False)  # Ocultar la columna de numeración
        self.tabla.setEditTriggers(QTableWidget.EditTrigger.DoubleClicked)  # Permitir edición de celdas
        self.layout.addWidget(self.tabla)

        # Botones de navegación
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

# ------------------ CRUD Proveedor ------------------

class ProveedorCRUD(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout()

        self.titulo = QLabel("Formulario Proveedor")
        self.titulo.setStyleSheet("font-size: 18px; font-weight: bold;")
        self.layout.addWidget(self.titulo)

        # Campos para los proveedores
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

        # Fila con botones de Agregar, Actualizar y Eliminar
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
        self.tabla.setColumnCount(8)  # Son 8 columnas
        self.tabla.setHorizontalHeaderLabels(["ID", "Nombre", "Teléfono", "Email", "Dirección", "Ciudad", "Estado", "País"])
        self.tabla.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.tabla.verticalHeader().setVisible(False)  # Ocultar la columna de numeración
        self.tabla.setEditTriggers(QTableWidget.EditTrigger.DoubleClicked)  # Permitir edición de celdas
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

# ------------------ Main Window ------------------

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sistema de Gestión Ferretería")
        self.setGeometry(100, 100, 800, 600)

        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        # Ventanas de cliente y proveedor
        self.cliente_window = ClienteCRUD()
        self.proveedor_window = ProveedorCRUD()

        # Añadir las ventanas al stacked widget
        self.stacked_widget.addWidget(self.cliente_window)
        self.stacked_widget.addWidget(self.proveedor_window)

        # Crear el menú principal
        self.menu_layout = QHBoxLayout()

        self.btn_clientes = QPushButton("Clientes")
        self.btn_clientes.clicked.connect(self.mostrar_clientes)
        self.menu_layout.addWidget(self.btn_clientes)

        self.btn_proveedores = QPushButton("Proveedores")
        self.btn_proveedores.clicked.connect(self.mostrar_proveedores)
        self.menu_layout.addWidget(self.btn_proveedores)

        # Crear el layout para el menú
        menu_widget = QWidget()
        menu_widget.setLayout(self.menu_layout)

        self.setMenuWidget(menu_widget)

    def mostrar_clientes(self):
        self.stacked_widget.setCurrentWidget(self.cliente_window)

    def mostrar_proveedores(self):
        self.stacked_widget.setCurrentWidget(self.proveedor_window)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
