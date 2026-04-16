# ==============================================================================
# PROYECTO: Amazon Laptops Price Scraper
# DESCRIPCIÓN: Fase 5 - Envío de Correo Automatizado y Seguridad (.env)
# DESCRIPTION: Phase 5 - Automated Email Dispatch and Security (.env)
# DESARROLLADO POR / DEVELOPED BY: VICTOR ARMANDO DE OLIVEIRA RODRÍGUEZ
# ==============================================================================

import smtplib
import os
from email.message import EmailMessage
from dotenv import load_dotenv

# Cargar las variables desde el archivo .env / Load variables from .env
load_dotenv()

def enviar_reporte_automatizado():
    """
    Envía el reporte y la gráfica por correo usando variables de entorno.
    Sends the report and chart via email using environment variables.
    """
    # 1. CONFIGURACIÓN DE SEGURIDAD / SECURITY CONFIGURATION
    remitente = os.getenv("EMAIL_USER")
    password = os.getenv("EMAIL_PASS")
    destinatario = remitente

    if not remitente or not password:
        print("❌ ERROR: No se encontraron las credenciales en el archivo .env")
        print("❌ ERROR: Credentials not found in .env file.")
        return

    # 2. CREAR EL CUERPO DEL MENSAJE / CREATE MESSAGE BODY
    msg = EmailMessage()
    msg['Subject'] = '📊 Reporte Automático: Laptops Gaming Amazon'
    msg['From'] = remitente
    msg['To'] = destinatario

    msg.set_content(
        f"Hola VICTOR ARMANDO,\n\n"
        f"El sistema ha completado el análisis de hoy.\n"
        f"Se adjunta el archivo Excel con los datos y la gráfica comparativa.\n\n"
        f"Estado: Proyecto Finalizado / Status: Project Completed."
    )

    # 3. ADJUNTAR ARCHIVOS / ATTACH FILES
    archivos = ['Reporte_Laptops_Amazon_Final.xlsx', 'grafica_precios_amazon.png']

    for nombre_archivo in archivos:
        if os.path.exists(nombre_archivo):
            with open(nombre_archivo, 'rb') as f:
                contenido = f.read()
                tipo = 'image' if nombre_archivo.endswith('.png') else 'application'
                subtipo = 'png' if nombre_archivo.endswith('.png') else 'vnd.openxmlformats-officedocument.spreadsheetml.sheet'
                msg.add_attachment(contenido, maintype=tipo, subtype=subtipo, filename=nombre_archivo)
        else:
            print(f"⚠️ Alerta: No se encontró {nombre_archivo} / Warning: File not found.")

    # 4. ENVÍO SEGURO / SECURE SENDING
    try:
        print("⏳ Conectando de forma segura / Connecting securely...")
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(remitente, password)
            smtp.send_message(msg)
        print("🚀 ¡ÉXITO! Correo enviado usando variables de entorno.")
        print("🚀 SUCCESS! Email sent using environment variables.")
    except Exception as e:
        print(f"❌ ERROR: {e}")

if __name__ == "__main__":
    enviar_reporte_automatizado()