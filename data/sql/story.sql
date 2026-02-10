-- Base de datos: story (SQLite)
-- Tabla de productos

CREATE TABLE IF NOT EXISTS products ( -- Crea tabla si no existe
    id INTEGER PRIMARY KEY AUTOINCREMENT, -- ID autoincremental
    name TEXT NOT NULL, -- Nombre del producto
    description TEXT, -- Descripción opcional
    price REAL NOT NULL, -- Precio
    stock INTEGER NOT NULL DEFAULT 0, -- Stock
    created_at TEXT NOT NULL DEFAULT (datetime('now')) -- Fecha de creación
); -- Fin de definición

-- Inserción de 20 productos (medicamentos)
INSERT INTO products (name, description, price, stock, created_at) VALUES -- Inserta múltiples filas
('Paracetamol 500mg', 'Analgésico y antipirético', 2.50, 120, datetime('now')), -- 1
('Ibuprofeno 400mg', 'Antiinflamatorio no esteroideo', 3.20, 80, datetime('now')), -- 2
('Amoxicilina 500mg', 'Antibiótico de amplio espectro', 5.75, 60, datetime('now')), -- 3
('Omeprazol 20mg', 'Protector gástrico', 4.10, 90, datetime('now')), -- 4
('Loratadina 10mg', 'Antihistamínico', 3.80, 70, datetime('now')), -- 5
('Cetirizina 10mg', 'Antihistamínico', 3.60, 65, datetime('now')), -- 6
('Azitromicina 500mg', 'Antibiótico macrólido', 8.90, 40, datetime('now')), -- 7
('Metformina 850mg', 'Antidiabético oral', 6.20, 55, datetime('now')), -- 8
('Losartán 50mg', 'Antihipertensivo', 7.10, 75, datetime('now')), -- 9
('Atorvastatina 20mg', 'Hipolipemiante', 9.50, 50, datetime('now')), -- 10
('Salbutamol inhalador', 'Broncodilatador', 12.00, 30, datetime('now')), -- 11
('Dexametasona 4mg', 'Corticoide', 4.95, 45, datetime('now')), -- 12
('Clotrimazol crema', 'Antifúngico tópico', 3.40, 85, datetime('now')), -- 13
('Fluconazol 150mg', 'Antifúngico sistémico', 6.80, 35, datetime('now')), -- 14
('Aciclovir 400mg', 'Antiviral', 7.60, 25, datetime('now')), -- 15
('Ranitidina 150mg', 'Antiácido', 4.00, 50, datetime('now')), -- 16
('Tramadol 50mg', 'Analgésico opioide', 10.20, 20, datetime('now')), -- 17
('Naproxeno 500mg', 'Antiinflamatorio', 4.70, 65, datetime('now')), -- 18
('Diclofenaco 50mg', 'Antiinflamatorio', 4.30, 60, datetime('now')), -- 19
('Vitamina C 1g', 'Suplemento vitamínico', 2.90, 100, datetime('now')); -- 20
