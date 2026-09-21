# ============================================================
# PASO 5: Guardar y ABRIR el PDF automáticamente
# ============================================================
# Es el mismo generador del paso 4, más un método nuevo:
#
#   abrir_pdf(ruta)  →  abre el archivo con la app por defecto
#
# En macOS el comando del sistema es: open
# (como hacer doble clic en el Finder)
# ============================================================

import platform
import subprocess
from pathlib import Path
from fpdf import FPDF


class GeneradorCertificado:
    """Fábrica de certificados PDF: pide datos, dibuja, guarda y abre."""

    def __init__(self):
        self.carpeta = Path(__file__).resolve().parent

        self.fuente_normal = "/System/Library/Fonts/Supplemental/Arial.ttf"
        self.fuente_negrita = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
        self.fuente_cursiva = "/System/Library/Fonts/Supplemental/Arial Italic.ttf"

        self.nombre = ""
        self.curso = ""
        self.fecha = ""

    def pedir_datos(self):
        """Pregunta al usuario y guarda las respuestas en el objeto."""
        print("=== Generador de certificados ===\n")
        self.nombre = input("Nombre del alumno: ")
        self.curso = input("Nombre del curso: ")
        self.fecha = input("Fecha (ej: 21 de septiembre de 2026): ")

    def crear_pdf(self):
        """Arma el PDF en memoria y lo devuelve."""
        pdf = FPDF(orientation="L", unit="mm", format="A4")
        pdf.add_page()

        pdf.add_font("Arial", style="", fname=self.fuente_normal)
        pdf.add_font("Arial", style="B", fname=self.fuente_negrita)
        pdf.add_font("Arial", style="I", fname=self.fuente_cursiva)

        pdf.set_font("Arial", style="B", size=28)
        pdf.cell(w=0, h=20, text="CERTIFICADO DE CURSO", align="C")
        pdf.ln(30)

        pdf.set_font("Arial", style="", size=16)
        pdf.cell(w=0, h=10, text="Se otorga el presente certificado a:", align="C")
        pdf.ln(20)

        pdf.set_font("Arial", style="B", size=24)
        pdf.cell(w=0, h=12, text=self.nombre, align="C")
        pdf.ln(20)

        pdf.set_font("Arial", style="", size=16)
        pdf.cell(w=0, h=10, text=f"Por completar el curso de {self.curso}", align="C")
        pdf.ln(25)

        pdf.set_font("Arial", style="I", size=14)
        pdf.cell(w=0, h=10, text=f"Fecha: {self.fecha}", align="C")

        return pdf

    def guardar(self, pdf, nombre_archivo="certificado_final.pdf"):
        """Guarda el PDF en la carpeta del proyecto y devuelve la ruta."""
        ruta = self.carpeta / nombre_archivo
        pdf.output(str(ruta))
        print(f"\nListo! Se guardo en:\n{ruta}")
        return ruta

    def abrir_pdf(self, ruta):
        """Abre el PDF con el visor por defecto del sistema."""
        sistema = platform.system()  # "Darwin" = macOS, "Windows", "Linux"

        if sistema == "Darwin":
            subprocess.run(["open", str(ruta)])  # macOS
        elif sistema == "Windows":
            subprocess.run(["start", str(ruta)], shell=True)
        else:
            subprocess.run(["xdg-open", str(ruta)])  # Linux

        print("Abriendo el PDF...")

    def generar(self):
        """Orquesta todo: pedir → crear → guardar → abrir."""
        self.pedir_datos()
        pdf = self.crear_pdf()
        ruta = self.guardar(pdf)
        self.abrir_pdf(ruta)


# --- Programa principal ---
if __name__ == "__main__":
    generador = GeneradorCertificado()
    generador.generar()
