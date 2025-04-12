-- Lucio Eduardo Santiago Moreno - S5A
-- No de control: 23270042
-- dbFerreteriaAlbania

DROP DATABASE IF EXISTS ferreteriaalbania_23270042;

CREATE DATABASE ferreteriaalbania_23270042;

USE ferreteriaalbania_23270042;

-- Tabla de Categorías
CREATE TABLE categoria (
    id_categoria INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    descripcion TEXT
);

-- Tabla de Clientes
CREATE TABLE cliente (
    id_cliente INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    telefono VARCHAR(15),
    email VARCHAR(100),
    RFC VARCHAR(13),
    direccion VARCHAR(100)
);

-- Tabla de Empleados
CREATE TABLE empleado (
    id_empleado INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    puesto VARCHAR(50),
    salario DECIMAL(10,2),
    telefono VARCHAR(10)
);

-- Tabla de Ventas
CREATE TABLE venta (
    id_venta INT AUTO_INCREMENT PRIMARY KEY,
    fecha DATE NULL,
    total DECIMAL(10,2) NOT NULL,
    cliente_id_cliente INT NOT NULL,
    empleado_id_empleado INT NOT NULL,
    FOREIGN KEY (cliente_id_cliente) REFERENCES cliente(id_cliente),
    FOREIGN KEY (empleado_id_empleado) REFERENCES empleado(id_empleado)
);

-- Tabla de Artículos
CREATE TABLE articulo (
    id_articulo INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    descripcion VARCHAR(100),
    precio DECIMAL(10,2) NOT NULL,
    id_categoria INT NULL,
    id_proveedor INT NULL,
    FOREIGN KEY (id_categoria) REFERENCES categoria(id_categoria)
);

-- Tabla de Detalle de Ventas
CREATE TABLE detalleventa (
    nombre_articulo VARCHAR(100) NOT NULL,
    cantidad INT NOT NULL,
    precio_unitario DECIMAL(10,2) NOT NULL,
    venta_id_venta INT NOT NULL,
    articulo_id_articulo INT NOT NULL,
    PRIMARY KEY (venta_id_venta, articulo_id_articulo),
    FOREIGN KEY (venta_id_venta) REFERENCES venta(id_venta),
    FOREIGN KEY (articulo_id_articulo) REFERENCES articulo(id_articulo)
);

-- Tabla de Proveedores
CREATE TABLE proveedor (
    id_proveedor INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    telefono CHAR(10),
    email VARCHAR(100),
    direccion VARCHAR(100),
    ciudad VARCHAR(100),
    estado VARCHAR(100),
    pais VARCHAR(100)
);

-- Tabla de Compras
CREATE TABLE compra (
    id_compra INT AUTO_INCREMENT PRIMARY KEY,
    total DECIMAL(10,2) NOT NULL,
    fecha DATE NULL,
    proveedor_id_proveedor INT NOT NULL,
    FOREIGN KEY (proveedor_id_proveedor) REFERENCES proveedor(id_proveedor)
);

-- Tabla de Detalle de Compras
CREATE TABLE detallecompra (
    nombre_articulo VARCHAR(100) NOT NULL,
    cantidad INT NOT NULL,
    precio_unitario DECIMAL(10,2) NOT NULL,
    articulo_id_articulo INT NOT NULL,
    compra_id_compra INT NOT NULL,
    PRIMARY KEY (articulo_id_articulo, compra_id_compra),
    FOREIGN KEY (articulo_id_articulo) REFERENCES articulo(id_articulo),
    FOREIGN KEY (compra_id_compra) REFERENCES compra(id_compra)
);
