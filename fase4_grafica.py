# ==============================================================================
# PROYECTO: Amazon Laptops Price Scraper
# DESCRIPCIÓN: Fase 4 - Visualización de Datos con Matplotlib
# DESCRIPTION: Phase 4 - Data Visualization with Matplotlib
# DESARROLLADO POR / DEVELOPED BY: VICTOR ARMANDO DE OLIVEIRA RODRÍGUEZ
# ==============================================================================

import pandas as pd
import sqlite3
import matplotlib.pyplot as plt


def crear_grafica_profesional():
    """
    Genera una gráfica de barras con los precios de las laptops.
    Generates a bar chart with laptop prices.
    """
    try:
        # 1. Cargar datos / Load data
        conn = sqlite3.connect('amazon_monitor.db')
        df = pd.read_sql_query("SELECT nombre_producto, precio FROM productos ORDER BY id DESC LIMIT 20", conn)
        conn.close()

        if df.empty:
            print("❌ Base de datos vacía / Database is empty.")
            return

        # --- LIMPIEZA QUIRÚRGICA / SURGICAL CLEANING ---
        df = df[~df['nombre_producto'].str.contains("capacidad", case=False)]
        df = df[df['nombre_producto'].str.len() > 25]
        df = df.drop_duplicates(subset=['nombre_producto'])

        # Ordenamos para la gráfica / Sorting for the chart
        df = df.sort_values(by='precio', ascending=True).tail(10)
        df['nombre_corto'] = df['nombre_producto'].str.slice(0, 35) + "..."

        # 2. Configurar la Estética / Setup Aesthetics
        plt.figure(figsize=(12, 8))

        # Color Azul Empresarial / Business Blue Color
        barras = plt.barh(df['nombre_corto'], df['precio'], color='#1F4E78', edgecolor='black')

        # Etiquetas y Título / Labels and Title
        plt.xlabel('Precio en USD ($) / Price in USD ($)', fontsize=12, fontweight='bold')
        plt.title('Top 10 Laptops - Amazon Price Ranking', fontsize=16, pad=25, fontweight='bold')

        # Rejilla técnica / Technical grid
        plt.grid(axis='x', linestyle='--', alpha=0.6)

        # Añadir valores a las barras / Add values to bars
        for barra in barras:
            width = barra.get_width()
            plt.text(width + 20, barra.get_y() + barra.get_height() / 2,
                     f'${int(width)}', va='center', fontweight='bold', fontsize=11)

        # 3. Guardar y Mostrar / Save and Show
        plt.tight_layout()
        nombre_archivo = 'grafica_precios_amazon.png'
        plt.savefig(nombre_archivo, dpi=300)

        print(f"✅ ¡Gráfica generada!: {nombre_archivo}")
        print(f"✅ Chart generated!: {nombre_archivo}")
        plt.show()

    except Exception as e:
        print(f"❌ Error al crear gráfica / Error creating chart: {e}")


if __name__ == "__main__":
    crear_grafica_profesional()