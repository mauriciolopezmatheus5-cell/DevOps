-- Base de datos: story (PostgreSQL)
-- Tabla de productos

CREATE TABLE IF NOT EXISTS products ( -- Crea tabla si no existe
    id SERIAL PRIMARY KEY, -- ID autoincremental
    name VARCHAR(120) NOT NULL, -- Nombre del producto
    description VARCHAR(255), -- Descripción opcional
    price NUMERIC NOT NULL, -- Precio
    stock INTEGER NOT NULL DEFAULT 0, -- Stock
    created_at TIMESTAMP NOT NULL DEFAULT NOW() -- Fecha de creación
); -- Fin de definición

-- Inserción de 20 productos (medicamentos)
INSERT INTO products (name, description, price, stock) VALUES -- Inserta múltiples filas
('Paracetamol 500mg', 'Analgésico y antipirético', 2.50, 120), -- 1
('Ibuprofeno 400mg', 'Antiinflamatorio no esteroideo', 3.20, 80), -- 2
('Amoxicilina 500mg', 'Antibiótico de amplio espectro', 5.75, 60), -- 3
('Omeprazol 20mg', 'Protector gástrico', 4.10, 90), -- 4
('Loratadina 10mg', 'Antihistamínico', 3.80, 70), -- 5
('Cetirizina 10mg', 'Antihistamínico', 3.60, 65), -- 6
('Azitromicina 500mg', 'Antibiótico macrólido', 8.90, 40), -- 7
('Metformina 850mg', 'Antidiabético oral', 6.20, 55), -- 8
('Losartán 50mg', 'Antihipertensivo', 7.10, 75), -- 9
('Atorvastatina 20mg', 'Hipolipemiante', 9.50, 50), -- 10
('Salbutamol inhalador', 'Broncodilatador', 12.00, 30), -- 11
('Dexametasona 4mg', 'Corticoide', 4.95, 45), -- 12
('Clotrimazol crema', 'Antifúngico tópico', 3.40, 85), -- 13
('Fluconazol 150mg', 'Antifúngico sistémico', 6.80, 35), -- 14
('Aciclovir 400mg', 'Antiviral', 7.60, 25), -- 15
('Ranitidina 150mg', 'Antiácido', 4.00, 50), -- 16
('Tramadol 50mg', 'Analgésico opioide', 10.20, 20), -- 17
('Naproxeno 500mg', 'Antiinflamatorio', 4.70, 65), -- 18
('Diclofenaco 50mg', 'Antiinflamatorio', 4.30, 60), -- 19
('Vitamina C 1g', 'Suplemento vitamínico', 2.90, 100); -- 20
