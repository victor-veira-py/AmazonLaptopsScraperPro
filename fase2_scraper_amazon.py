# ==============================================================================
# PROYECTO: Amazon Laptops Price Scraper
# DESCRIPCIÓN: Fase 2 - Scraper de Amazon con Selenium y filtrado inteligente
# DESCRIPTION: Phase 2 - Amazon Scraper with Selenium and smart filtering
# DESARROLLADO POR / DEVELOPED BY: VICTOR ARMANDO DE OLIVEIRA RODRÍGUEZ
# ==============================================================================

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import sqlite3

def salvar_en_db(nombre, precio, enlace):
    """
    Guarda los datos extraídos en la base de datos SQLite de la Fase 1.
    Saves the extracted data into the SQLite database from Phase 1.
    """
    conn = sqlite3.connect('amazon_monitor.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO productos (plataforma, nombre_producto, precio, moneda, enlace)
        VALUES (?, ?, ?, ?, ?)
    ''', ('Amazon', nombre, precio, 'USD', enlace))
    conn.commit()
    conn.close()

def scrapear_amazon(busqueda):
    """
    Navega en Amazon, filtra resultados y extrae datos de productos.
    Navigates Amazon, filters results, and extracts product data.
    """
    opts = Options()
    # User-Agent para evitar bloqueos básicos / User-Agent to avoid basic blocks
    opts.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
    driver = webdriver.Chrome(options=opts)

    try:
        url = f"https://www.amazon.com/s?k={busqueda.replace(' ', '+')}"
        driver.get(url)

        print("⚠️ [SISTEMA] Configura la ubicación y espera que carguen las laptops.")
        print("⚠️ [SYSTEM] Set the location and wait for laptops to load.")
        input("👉 Presiona ENTER cuando estés listo / Press ENTER when ready...")

        # Localización de los bloques de productos / Locating product blocks
        items = driver.find_elements(By.XPATH, '//div[@data-component-type="s-search-result"]')
        print(f"📦 [INFO] Analizando {len(items)} bloques... / Analyzing {len(items)} blocks...")

        conteo = 0
        for item in items:
            if conteo >= 10: break
            try:
                # 1. Extracción del Nombre / Name Extraction
                try:
                    nombre = item.find_element(By.CSS_SELECTOR, 'h2 span').text.strip()
                except:
                    nombre = item.find_element(By.CLASS_NAME, 'a-truncate-cut').text.strip()

                # --- FILTRO ANTI-BASURA / TRASH FILTER ---
                # Evita capturar accesorios o textos irrelevantes
                # Avoids capturing accessories or irrelevant texts
                if "capacidades" in nombre.lower() or len(nombre) < 15:
                    continue

                # 2. Extracción del Precio / Price Extraction
                try:
                    precio_raw = item.find_element(By.CLASS_NAME, 'a-price-whole').text
                except:
                    precio_raw = item.find_element(By.CLASS_NAME, 'a-offscreen').get_attribute('innerHTML')

                # Limpieza de datos numéricos / Numerical data cleaning
                precio_final = float(precio_raw.replace('$', '').replace(',', '').replace('\n', '').strip())

                # 3. Extracción del Enlace / Link Extraction
                try:
                    link = item.find_element(By.CSS_SELECTOR, 'h2 a').get_attribute('href')
                except:
                    link = item.find_element(By.TAG_NAME, 'a').get_attribute('href')

                if nombre and precio_final:
                    salvar_en_db(nombre, precio_final, link)
                    print(f"✅ [{conteo + 1}] Guardado: {nombre[:40]}... | ${precio_final}")
                    conteo += 1

            except Exception:
                continue

    finally:
        driver.quit()
        print(f"\n🚀 [SISTEMA] ¡Proceso terminado! Guardados: {conteo}")
        print(f"🚀 [SYSTEM] Process finished! Saved: {conteo}")

if __name__ == "__main__":
    # Búsqueda inicial de ejemplo / Initial example search
    scrapear_amazon("laptop gaming")