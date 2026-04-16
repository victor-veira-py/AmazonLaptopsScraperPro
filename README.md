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
Developed by / Desarrollado por **VICTOR ARMANDO DE OLIVEIRA RODRÍGUEZ**
