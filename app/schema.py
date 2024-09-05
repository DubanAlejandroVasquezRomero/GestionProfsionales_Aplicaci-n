instructions = [
    """
    CREATE TABLE IF NOT EXISTS usuarios (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nombre VARCHAR(50) NOT NULL UNIQUE, 
        correo VARCHAR(100) NOT NULL UNIQUE,
        contraseña VARCHAR(200) NOT NULL,
        rol ENUM('profesional', 'cliente', 'admin') NOT NULL,
        fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS profesionales (
        id INT AUTO_INCREMENT PRIMARY KEY,
        usuario_id INT NOT NULL,
        especialidad VARCHAR(100) NOT NULL,
        FOREIGN KEY (usuario_id) REFERENCES usuarios(id) ON DELETE CASCADE
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS citas (
        id INT AUTO_INCREMENT PRIMARY KEY,
        profesional_id INT NOT NULL,
        cliente_id INT NOT NULL,
        fecha DATE NOT NULL,
        hora_inicio TIME NOT NULL,
        hora_fin TIME NOT NULL,
        estado ENUM('pendiente', 'confirmada', 'cancelada') DEFAULT 'pendiente',
        FOREIGN KEY (profesional_id) REFERENCES profesionales(id) ON DELETE CASCADE,
        FOREIGN KEY (cliente_id) REFERENCES usuarios(id) ON DELETE CASCADE
    );
    """,
    """
    CREATE TABLE IF NOT EXISTS estadisticas (
        id INT AUTO_INCREMENT PRIMARY KEY,
        profesional_id INT NOT NULL,
        fecha DATE NOT NULL,
        tipo_estadistica VARCHAR(100) NOT NULL,
        valor INT NOT NULL,
        FOREIGN KEY (profesional_id) REFERENCES profesionales(id) ON DELETE CASCADE
    );
    """
]
