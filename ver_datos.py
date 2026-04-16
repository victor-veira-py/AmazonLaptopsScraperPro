import sqlite3


def leer_inventario():
    conn = sqlite3.connect('amazon_monitor.db')
    cursor = conn.cursor()

    # El comando SELECT * significa: "Selecciona TODO de la tabla productos"
    cursor.execute("SELECT * FROM productos")
    filas = cursor.fetchall()

    print(f"{'ID':<3} | {'FECHA':<20} | {'NOMBRE':<40} | {'PRECIO':<10}")
    print("-" * 80)

    for fila in filas:
        # fila[0] es ID, [1] es fecha, [3] es nombre, [4] es precio
        print(f"{fila[0]:<3} | {fila[1]:<20} | {fila[3][:38]:<40} | ${fila[4]:<10}")

    conn.close()


if __name__ == "__main__":
    leer_inventario()