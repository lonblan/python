# ============================================================
# PASO 3: Pedir datos con input() y meterlos en el PDF
# ============================================================
# Antes el nombre, el curso y la fecha estaban "escritos a mano"
# en el código. Ahora el programa PREGUNTA y usa tus respuestas.
#
# Novedades:
#   1) input()  → lee lo que escribes en la terminal
#   2) variables → guardan esas respuestas
#   3) fuente Arial → permite acentos (á, é, ñ...). Helvetica no.
# ============================================================

from fpdf import FPDF


# --- 1. Pedir datos al usuario ---
print("=== Generador de certificados ===\n")

nombre = input("Nombre del alumno: ")
curso = input("Nombre del curso: ")
fecha = input("Fecha (ej: 20 de septiembre de 2026): ")

# --- 2. Crear el PDF (igual que en el paso 2) ---
pdf = FPDF(orientation="L", unit="mm", format="A4")
pdf.add_page()

# --- 3. Cargar Arial (soporta español con acentos) ---
# En macOS estas rutas suelen existir. Son fuentes del sistema.
pdf.add_font("Arial", style="", fname="/System/Library/Fonts/Supplemental/Arial.ttf")
pdf.add_font("Arial", style="B", fname="/System/Library/Fonts/Supplemental/Arial Bold.ttf")
pdf.add_font("Arial", style="I", fname="/System/Library/Fonts/Supplemental/Arial Italic.ttf")

# --- 4. Título ---
pdf.set_font("Arial", style="B", size=28)
pdf.cell(w=0, h=20, text="CERTIFICADO DE CURSO", align="C")
pdf.ln(30)

# --- 5. Texto introductorio ---
pdf.set_font("Arial", style="", size=16)
pdf.cell(w=0, h=10, text="Se otorga el presente certificado a:", align="C")
pdf.ln(20)

# --- 6. Nombre (lo que escribió el usuario) ---
pdf.set_font("Arial", style="B", size=24)
pdf.cell(w=0, h=12, text=nombre, align="C")  # variable, no texto fijo
pdf.ln(20)

# --- 7. Curso ---
pdf.set_font("Arial", style="", size=16)
pdf.cell(w=0, h=10, text=f"Por completar el curso de {curso}", align="C")
pdf.ln(25)

# --- 8. Fecha ---
pdf.set_font("Arial", style="I", size=14)
pdf.cell(w=0, h=10, text=f"Fecha: {fecha}", align="C")

# --- 9. Guardar ---
# Siempre el mismo nombre de archivo (si existe, se sobrescribe).
pdf.output("certificado_paso3.pdf")

print("\nListo! Se creo: certificado_paso3.pdf")
print(f"Alumno: {nombre}")
print(f"Curso:  {curso}")
