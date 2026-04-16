# ==============================================================================
# PROYECTO: Amazon Laptops Price Scraper
# DESCRIPCIÓN: Fase 3 - Análisis de datos con Pandas y Reporte Profesional Excel
# DESCRIPTION: Phase 3 - Data Analysis with Pandas and Professional Excel Report
# DESARROLLADO POR / DEVELOPED BY: VICTOR ARMANDO DE OLIVEIRA RODRÍGUEZ
# ==============================================================================

import pandas as pd
import sqlite3

def analizar_y_exportar_limpio():
    """
    Analiza los datos de la DB y genera un reporte Excel con formato profesional.
    Analyzes DB data and generates an Excel report with professional formatting.
    """
    try:
        # 1. Conexión y Carga (Últimos 10 registros)
        # 1. Connection and Loading (Last 10 records)
        conn = sqlite3.connect('amazon_monitor.db')
        df = pd.read_sql_query("SELECT * FROM productos ORDER BY id DESC LIMIT 10", conn)
        conn.close()

        if df.empty:
            print("❌ La base de datos está vacía / The database is empty.")
            return

        # --- LIMPIEZA DE DATOS / DATA CLEANING ---
        # Filtro de seguridad y ordenamiento por precio
        # Security filter and price sorting
        df = df[~df['nombre_producto'].str.contains("capacidades", case=False)]
        df = df.sort_values(by='precio', ascending=True)

        # Acortamos el nombre para estética / Shorten name for aesthetics
        df['nombre_producto'] = df['nombre_producto'].str.slice(0, 70)

        # 2. Exportación con Formato (Estética Profesional)
        # 2. Export with Formatting (Professional Aesthetics)
        nombre_excel = "Reporte_Laptops_Amazon_Final.xlsx"

        with pd.ExcelWriter(nombre_excel, engine='xlsxwriter') as writer:
            df.to_excel(writer, sheet_name='Resultados', index=False)

            workbook = writer.book
            worksheet = writer.sheets['Resultados']

            # FORMATOS / FORMATTING
            formato_encabezado = workbook.add_format({
                'bold': True,
                'text_wrap': True,
                'valign': 'vcenter',
                'align': 'center',
                'fg_color': '#1F4E78',  # Azul Empresarial / Business Blue
                'font_color': 'white',
                'border': 1
            })

            formato_centrado = workbook.add_format({'align': 'center', 'valign': 'vcenter'})

            # Aplicar estilo a encabezados / Apply style to headers
            for col_num, value in enumerate(df.columns.values):
                worksheet.write(0, col_num, value, formato_encabezado)

            # AJUSTE DE COLUMNAS / COLUMN ADJUSTMENT
            worksheet.set_column('A:A', 6, formato_centrado)   # ID
            worksheet.set_column('B:B', 18, formato_centrado)  # Fecha
            worksheet.set_column('C:C', 12, formato_centrado)  # Plataforma
            worksheet.set_column('D:D', 65)                    # Nombre
            worksheet.set_column('E:E', 15, formato_centrado)  # Precio
            worksheet.set_column('F:F', 10, formato_centrado)  # Moneda
            worksheet.set_column('G:G', 50)                    # Enlace

        print(f"✅ ¡Reporte Impecable Generado!: {nombre_excel}")
        print(f"✅ Professional Report Generated!: {nombre_excel}")

    except Exception as e:
        print(f"❌ Error en el análisis / Analysis error: {e}")

if __name__ == "__main__":
    analizar_y_exportar_limpio()