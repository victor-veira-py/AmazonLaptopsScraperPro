# 🗄️ Phase 1: SQLite Database Configuration | Fase 1: Configuración de Base de Datos

[English](#english) | [Español](#español)

---

## English
This script initializes the local storage system for the Amazon Scraper. It uses **SQLite** to ensure data persistence without the need for complex external servers.

### ✨ Key Technical Features:
* **Automated Creation:** If the database file doesn't exist, the script creates it instantly.
* **Optimized Schema:** Includes fields for timestamping, platform identification, pricing (REAL), and direct product links.
* **Data Integrity:** Configured with `IF NOT EXISTS` clauses to prevent accidental overwriting of existing tables.

---

## Español
Este script inicializa el sistema de almacenamiento local para el Scraper de Amazon. Utiliza **SQLite** para garantizar la persistencia de los datos sin necesidad de servidores externos complejos.

### ✨ Características Técnicas:
* **Creación Automatizada:** Si el archivo de la base de datos no existe, el script lo genera instantáneamente.
* **Esquema Optimizado:** Incluye campos para marca de tiempo (timestamp), identificación de plataforma, precios (REAL) y enlaces directos.
* **Integridad de Datos:** Configurado con cláusulas `IF NOT EXISTS` para evitar la sobrescritura accidental de tablas existentes.

---

---

# 🤖 Phase 2: Dynamic Web Scraper (Selenium) | Fase 2: Scraper Dinámico (Selenium)

[English](#english-f2) | [Español](#español-f2)

---

## English
This stage focuses on real-time data extraction using **Selenium WebDriver**. The bot simulates human browsing to capture prices and technical specifications.

### ✨ Key Features:
* **Smart Filtering:** Implements logic to skip accessories and irrelevant results, focusing only on real laptops.
* **Automated Persistence:** Each finding is automatically sent to the SQLite database.
* **Navigation Control:** Optimized headers (User-Agent) to improve connection stability and avoid detection.

---

## Español
Esta etapa se enfoca en la extracción de datos en tiempo real usando **Selenium WebDriver**. El bot simula la navegación humana para capturar precios y especificaciones técnicas.

### ✨ Características Técnicas:
* **Filtrado Inteligente:** Implementa lógica para saltar accesorios y resultados irrelevantes, enfocándose solo en laptops reales.
* **Persistencia Automatizada:** Cada hallazgo se envía automáticamente a la base de datos SQLite.
* **Control de Navegación:** Cabeceras optimizadas (User-Agent) para mejorar la estabilidad de la conexión y evitar detecciones.

---

---

# 📊 Phase 3: Data Analysis & Excel Reporting | Fase 3: Análisis de Datos y Reporte en Excel

[English](#english-f3) | [Español](#español-f3)

---

## English
In this phase, the system processes the collected data using **Pandas**. The raw information is cleaned and transformed into a high-level executive report.

### ✨ Key Features:
* **Smart Cleaning:** Automated filtering of irrelevant entries and text normalization for product names.
* **Business Formatting:** Generation of Excel files with custom styling (Business Blue headers and auto-adjusted columns).
* **Price Optimization:** Automated sorting to highlight the most competitive prices first.

---

## Español
En esta fase, el sistema procesa los datos recolectados utilizando **Pandas**. La información cruda se limpia y se transforma en un reporte ejecutivo de alto nivel.

### ✨ Características Técnicas:
* **Limpieza Inteligente:** Filtrado automático de entradas irrelevantes y normalización de texto para nombres de productos.
* **Formato Empresarial:** Generación de archivos Excel con estilos personalizados (encabezados en Azul Empresarial y ajuste automático de columnas).
* **Optimización de Precios:** Ordenamiento automático para resaltar los precios más competitivos primero.

---
