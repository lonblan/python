# ============================================================
# PASO 1: Crear tu primer PDF
# ============================================================
# Idea: un PDF es como una hoja en blanco. Nosotros:
#   1) creamos el documento
#   2) añadimos una página
#   3) escribimos un título
#   4) lo guardamos en un archivo .pdf
#
# Librería: fpdf2  (se importa como "fpdf")
#
# En esta carpeta ya hay un entorno virtual (.venv) con fpdf2.
# Para ejecutar este archivo desde la terminal:
#   cd "sección 7. generador de PDF"
#   .venv/bin/python paso1_hola_pdf.py
#
# O en Cursor: elige el intérprete .venv y pulsa Run.
# ============================================================

from fpdf import FPDF  # FPDF = la "máquina" que fabrica PDFs


# --- 1. Crear el documento ---
# orientation="L"  → horizontal (Landscape), mejor para un certificado
# unit="mm"        → medimos en milímetros
# format="A4"      → tamaño de hoja A4
pdf = FPDF(orientation="L", unit="mm", format="A4")

# --- 2. Añadir una página en blanco ---
pdf.add_page()

# --- 3. Elegir tipografía y tamaño ---
# "Helvetica" es una fuente que viene incluida (no hace falta instalar nada)
pdf.set_font("Helvetica", style="B", size=28)  # B = Bold (negrita)

# --- 4. Escribir el título ---
# cell(ancho, alto, texto, align="C")
#   ancho=0  → usa todo el ancho de la página
#   alto=20  → altura de la "celda" de texto en mm
#   align="C"→ centrado
pdf.cell(w=0, h=20, text="CERTIFICADO DE CURSO", align="C")

# --- 5. Guardar el archivo ---
# Se crea en la misma carpeta donde está este script.
pdf.output("mi_primer_certificado.pdf")

print("Listo! Se creo el archivo: mi_primer_certificado.pdf")
print("Abrelo haciendo doble clic en el archivo de la carpeta.")
