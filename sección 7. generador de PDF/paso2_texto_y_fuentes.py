# ============================================================
# PASO 2: Más texto, tipografías y saltos de línea
# ============================================================
# En el paso 1 solo había un título.
# Ahora el certificado tendrá:
#   - título
#   - texto introductorio
#   - nombre del alumno (más grande)
#   - nombre del curso
#   - fecha
#
# Idea nueva: ln() baja el "cursor" (como pulsar Enter).
# ============================================================

from fpdf import FPDF


pdf = FPDF(orientation="L", unit="mm", format="A4")
pdf.add_page()

# --- Título ---
pdf.set_font("Helvetica", style="B", size=28)
pdf.cell(w=0, h=20, text="CERTIFICADO DE CURSO", align="C")
pdf.ln(30)  # Baja 30 mm (deja espacio debajo del título)

# --- Texto introductorio ---
# style="" = normal (sin negrita)
pdf.set_font("Helvetica", style="", size=16)
pdf.cell(w=0, h=10, text="Se otorga el presente certificado a:", align="C")
pdf.ln(20)

# --- Nombre del alumno (destacado) ---
pdf.set_font("Helvetica", style="B", size=24)
pdf.cell(w=0, h=12, text="Juan Carlos Londono", align="C")
pdf.ln(20)

# --- Nombre del curso ---
pdf.set_font("Helvetica", style="", size=16)
pdf.cell(w=0, h=10, text="Por completar el curso de Python", align="C")
pdf.ln(25)

# --- Fecha ---
pdf.set_font("Helvetica", style="I", size=14)  # I = Italic (cursiva)
pdf.cell(w=0, h=10, text="Fecha: 20 de septiembre de 2026", align="C")

# --- Guardar ---
pdf.output("certificado_paso2.pdf")

print("Listo! Se creo: certificado_paso2.pdf")
print("Abrelo y compara con el del paso 1.")
