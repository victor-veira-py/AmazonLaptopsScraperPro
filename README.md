# 🗄️ Phase 1: SQLite Database Configuration | Fase 1: Configuración de Base de Datos

[English](#en-amz-f1) | [Español](#es-amz-f1)

---

<div id="en-amz-f1"></div>

## English
This script initializes the local storage system for the Amazon Scraper. It uses **SQLite** to ensure data persistence without the need for complex external servers.

### ✨ Key Technical Features:
* **Automated Creation:** If the database file doesn't exist, the script creates it instantly.
* **Optimized Schema:** Includes fields for timestamping, platform identification, pricing (REAL), and direct product links.
* **Data Integrity:** Configured with `IF NOT EXISTS` clauses to prevent accidental overwriting of existing tables.

<br>
<hr>
<br>

<div id="es-amz-f1"></div>

## Español
Este script inicializa el sistema de almacenamiento local para el Scraper de Amazon. Utiliza **SQLite** para garantizar la persistencia de los datos sin necesidad de servidores externos complejos.

### ✨ Características Técnicas:
* **Creación Automatizada:** Si el archivo de la base de datos no existe, el script lo genera instantáneamente.
* **Esquema Optimizado:** Incluye campos para marca de tiempo (timestamp), identificación de plataforma, precios (REAL) y enlaces directos.
* **Integridad de Datos:** Configurado con cláusulas `IF NOT EXISTS` para evitar la sobrescritura accidental de tablas existentes.

---

# 🤖 Phase 2: Dynamic Web Scraper (Selenium) | Fase 2: Scraper Dinámico (Selenium)

[English](#en-amz-f2) | [Español](#es-amz-f2)

---

<div id="en-amz-f2"></div>

## English
This stage focuses on real-time data extraction using **Selenium WebDriver**. The bot simulates human browsing to capture prices and technical specifications.

### ✨ Key Features:
* **Smart Filtering:** Implements logic to skip accessories and irrelevant results, focusing only on real laptops.
* **Automated Persistence:** Each finding is automatically sent to the SQLite database.
* **Navigation Control:** Optimized headers (User-Agent) to improve connection stability and avoid detection.

<br>
<hr>
<br>

<div id="es-amz-f2"></div>

## Español
Esta etapa se enfoca en la extracción de datos en tiempo real usando **Selenium WebDriver**. El bot simula la navegación humana para capturar precios y especificaciones técnicas.

### ✨ Características Técnicas:
* **Filtrado Inteligente:** Implementa lógica para saltar accesorios y resultados irrelevantes, enfocándose solo en laptops reales.
* **Persistencia Automatizada:** Cada hallazgo se envía automáticamente a la base de datos SQLite.
* **Control de Navegación:** Cabeceras optimizadas (User-Agent) para mejorar la estabilidad de la conexión y evitar detecciones.

---

# 📊 Phase 3: Data Analysis & Excel Reporting | Fase 3: Análisis de Datos y Reporte en Excel

[English](#en-amz-f3) | [Español](#es-amz-f3)

---

<div id="en-amz-f3"></div>

## English
In this phase, the system processes the collected data using **Pandas**. The raw information is cleaned and transformed into a high-level executive report.

### ✨ Key Features:
* **Smart Cleaning:** Automated filtering of irrelevant entries and text normalization for product names.
* **Business Formatting:** Generation of Excel files with custom styling (Business Blue headers and auto-adjusted columns).
* **Price Optimization:** Automated sorting to highlight the most competitive prices first.

<br>
<hr>
<br>

<div id="es-amz-f3"></div>

## Español
En esta fase, el sistema procesa los datos recolectados utilizando **Pandas**. La información cruda se limpia y se transforma en un reporte ejecutivo de alto nivel.

### ✨ Características Técnicas:
* **Limpieza Inteligente:** Filtrado automático de entradas irrelevantes y normalización de texto para nombres de productos.
* **Formato Empresarial:** Generación de archivos Excel con estilos personalizados (encabezados en Azul Empresarial y ajuste automático de columnas).
* **Optimización de Precios:** Ordenamiento automático para resaltar los precios más competitivos primero.

<img width="1366" height="736" alt="exce_amazon" src="https://github.com/user-attachments/assets/3e75b573-6310-46ae-a2da-6c9a4d897557" />

---

# 📈 Phase 4: Data Visualization | Fase 4: Visualización de Datos

[English](#en-amz-f4) | [Español](#es-amz-f4)

---

<div id="en-amz-f4"></div>

## English
This module transforms processed data into visual insights using **Matplotlib**. It generates a high-resolution bar chart for quick price comparison.

### ✨ Key Features:
* **Professional Aesthetics:** Custom styling using Business Blue and clean typography.
* **Data Labeling:** Precise price indicators on each bar for better readability.
* **Automated Export:** Saves a high-quality (300 DPI) PNG image for presentations.

<br>
<hr>
<br>

<div id="es-amz-f4"></div>

## Español
Este módulo transforma los datos procesados en información visual utilizando **Matplotlib**. Genera una gráfica de barras de alta resolución para una comparación rápida de precios.

### ✨ Características Técnicas:
* **Estética Profesional:** Estilo personalizado utilizando Azul Empresarial y tipografía limpia.
* **Etiquetado de Datos:** Indicadores de precio precisos en cada barra para una mejor legibilidad.
* **Exportación Automatizada:** Guarda una imagen PNG de alta calidad (300 DPI) para presentaciones.

<img width="3600" height="2400" alt="grafica_precios_amazon" src="https://github.com/user-attachments/assets/97d04dd4-c6ee-4dbd-9787-f0bb430078e3" />

---

# 📧 Phase 5: Automated Email & Security | Fase 5: Envío de Correo y Seguridad

[English](#en-amz-f5) | [Español](#es-amz-f5)

---

<div id="en-amz-f5"></div>

## English
The final stage of the project integrates an **automated notification system** with professional security standards. It uses environment variables to protect sensitive credentials while delivering reports.

### ✨ Key Features:
* **Environment Security:** Uses `.env` files to keep email credentials out of the public source code.
* **SSL Encryption:** Implements secure communication with Gmail servers via port 465.
* **Integrated Reporting:** Automatically attaches both the Excel dataset and the visualization chart.

<br>
<hr>
<br>

<div id="es-amz-f5"></div>

## Español
La etapa final del proyecto integra un **sistema de notificación automatizado** con estándares de seguridad profesionales. Utiliza variables de entorno para proteger credenciales sensibles durante la entrega de reportes.

### ✨ Características Técnicas:
* **Seguridad de Envío:** Usa archivos `.env` para mantener las credenciales de correo fuera del código fuente público.
* **Cifrado SSL:** Implementa comunicación segura con los servidores de Gmail a través del puerto 465.
* **Reporte Integrado:** Adjunta automáticamente tanto el conjunto de datos en Excel como la gráfica de visualización.

---

### 🛠️ Extra Utilities | Utilidades Extra
* **ver_datos.py:** A quick-access script to preview the SQLite database directly from the terminal. | Un script de acceso rápido para previsualizar la base de datos SQLite directamente desde la terminal.

---

## 👨‍💻 Developed by / Desarrollado por
**VICTOR ARMANDO DE OLIVEIRA RODRÍGUEZ**
*Security Professional & Python Developer*
