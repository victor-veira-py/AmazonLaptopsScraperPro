# ==============================================================================
# PROYECTO: Amazon Laptops Price Scraper
# DESCRIPCIÓN: Fase 1 - Configuración y creación de la Base de Datos SQLite
# DESCRIPTION: Phase 1 - SQLite Database Setup and Creation
# DESARROLLADO POR / DEVELOPED BY: VICTOR ARMANDO DE OLIVEIRA RODRÍGUEZ
# ==============================================================================

import sqlite3


def inicializar_db():
    """
    Crea la base de datos y la tabla necesaria para almacenar los productos.
    Creates the database and the table required to store the products.
    """
    try:
        # 1. Conexión (si no existe el archivo, lo crea automáticamente)
        # 1. Connection (if the file doesn't exist, it is created automatically)
        conexion = sqlite3.connect('amazon_monitor.db')
        cursor = conexion.cursor()

        # 2. Crear la tabla principal con SQL
        # 2. Create the main table using SQL
        # Usamos REAL para precios y TEXT para textos / We use REAL for prices and TEXT for text
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS productos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                fecha_rastreo DATETIME DEFAULT CURRENT_TIMESTAMP,
                plataforma TEXT,
                nombre_producto TEXT,
                precio REAL,
                moneda TEXT,
                enlace TEXT
            )
        ''')

        # Guardar cambios y cerrar / Save changes and close
        conexion.commit()
        conexion.close()

        print("✅ [SISTEMA] Base de datos 'amazon_monitor.db' creada y lista.")
        print("✅ [SYSTEM] Database 'amazon_monitor.db' created and ready.")

    except Exception as e:
        print(f"❌ Error al inicializar la base de datos / Database error: {e}")


if __name__ == "__main__":
    inicializar_db()