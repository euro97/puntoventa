CREATE TABLE productos (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    precio NUMERIC(10,2) NOT NULL,
    marca VARCHAR(100),
    cantidad INT NOT NULL,
    tamano VARCHAR(50)
);

INSERT INTO productos (nombre, precio, marca, cantidad, tamano) VALUES
('Coca Cola', 18.50, 'Coca Cola', 25, 600),
('Pepsi', 17.00, 'Pepsi', 30, 600),
('Sabritas Original', 15.00, 'Sabritas', 40, 45),
('Doritos Nacho', 16.50, 'Doritos', 35, 55),
('Gansito', 20.00, 'Marinela', 15, 50),
('Chocorroles', 19.00, 'Marinela', 12, 60),
('Leche Entera', 28.00, 'Lala', 18, 1),
('Yogurt Fresa', 12.50, 'Danone', 22, 250),
('Atún en Agua', 24.00, 'Herdez', 50, 140),
('Arroz', 32.00, 'SOS', 20, 1),
('Frijoles Refritos', 18.00, 'Isadora', 28, 430),
('Aceite Vegetal', 45.00, 'Nutrioli', 10, 1),
('Jabón de Tocador', 14.00, 'Palmolive', 40, 120),
('Pasta Dental', 35.00, 'Colgate', 16, 100),
('Shampoo', 65.00, 'Head & Shoulders', 8, 400);

select * from productos;


CREATE TABLE ventas (
    id_venta SERIAL PRIMARY KEY,
    fecha TIMESTAMP NOT NULL DEFAULT NOW(),
    total NUMERIC(10,2) NOT NULL CHECK (total >= 0),
    metodo_pago VARCHAR(50) NOT NULL,
    cliente VARCHAR(100),
    id_usuario INT,
    
    CONSTRAINT ventas_metodo_pago_check 
        CHECK (metodo_pago IN ('Efectivo', 'Tarjeta', 'Transferencia'))
);

ALTER TABLE ventas
ADD CONSTRAINT fk_usuario
FOREIGN KEY (id_usuario)
REFERENCES usuarios(id_usuario)
ON DELETE SET NULL;



CREATE TABLE detalle_venta (
    id_detalle SERIAL PRIMARY KEY,
    id_venta INT NOT NULL,
    id_producto INT NOT NULL,
    cantidad INT NOT NULL CHECK (cantidad > 0),
    precio_unitario NUMERIC(10,2) NOT NULL CHECK (precio_unitario >= 0),

    CONSTRAINT fk_venta
        FOREIGN KEY (id_venta) REFERENCES ventas(id_venta)
        ON DELETE CASCADE,

    CONSTRAINT fk_producto
        FOREIGN KEY (id_producto) REFERENCES productos(id_producto)
        ON DELETE RESTRICT
);

CREATE TABLE usuarios (
    id_usuario SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    correo VARCHAR(150) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    rol VARCHAR(50) NOT NULL DEFAULT 'Cajero',
    activo BOOLEAN NOT NULL DEFAULT TRUE,
    fecha_creacion TIMESTAMP NOT NULL DEFAULT NOW(),

    CONSTRAINT usuarios_rol_check
        CHECK (rol IN ('Admin', 'Cajero'))
);