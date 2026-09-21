# ============================================================
# PASO 4: Organizar el código en una CLASE (POO)
# ============================================================
# Hasta ahora todo el código iba "suelto" de arriba a abajo.
# Ahora agrupamos la idea en una clase:
#
#   GeneradorCertificado  →  sabe pedir datos, dibujar y guardar
#
# También solucionamos el problema del paso 3:
# el PDF se guarda SIEMPRE en esta carpeta, no donde estés
# cuando ejecutas el programa.
# ============================================================

from pathlib import Path  # Para rutas de archivos (carpetas y nombres)
from fpdf import FPDF


class GeneradorCertificado:
    """Fábrica de certificados PDF: pide datos, dibuja y guarda."""

    def __init__(self):
        # Carpeta donde está ESTE archivo .py (no depende del cwd)
        self.carpeta = Path(__file__).resolve().parent

        # Rutas de fuentes Arial en macOS (soportan acentos)
        self.fuente_normal = "/System/Library/Fonts/Supplemental/Arial.ttf"
        self.fuente_negrita = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
        self.fuente_cursiva = "/System/Library/Fonts/Supplemental/Arial Italic.ttf"

        # Datos del certificado (empiezan vacíos)
        self.nombre = ""
        self.curso = ""
        self.fecha = ""

    def pedir_datos(self):
        """Pregunta al usuario y guarda las respuestas en el objeto."""
        print("=== Generador de certificados ===\n")
        self.nombre = input("Nombre del alumno: ")
        self.curso = input("Nombre del curso: ")
        self.fecha = input("Fecha (ej: 20 de septiembre de 2026): ")

    def crear_pdf(self):
        """Arma el PDF en memoria y lo devuelve."""
        pdf = FPDF(orientation="L", unit="mm", format="A4")
        pdf.add_page()

        # Registrar fuentes (una vez por documento)
        pdf.add_font("Arial", style="", fname=self.fuente_normal)
        pdf.add_font("Arial", style="B", fname=self.fuente_negrita)
        pdf.add_font("Arial", style="I", fname=self.fuente_cursiva)

        # Título
        pdf.set_font("Arial", style="B", size=28)
        pdf.cell(w=0, h=20, text="CERTIFICADO DE CURSO", align="C")
        pdf.ln(30)

        # Texto introductorio
        pdf.set_font("Arial", style="", size=16)
        pdf.cell(w=0, h=10, text="Se otorga el presente certificado a:", align="C")
        pdf.ln(20)

        # Nombre
        pdf.set_font("Arial", style="B", size=24)
        pdf.cell(w=0, h=12, text=self.nombre, align="C")
        pdf.ln(20)

        # Curso
        pdf.set_font("Arial", style="", size=16)
        pdf.cell(w=0, h=10, text=f"Por completar el curso de {self.curso}", align="C")
        pdf.ln(25)

        # Fecha
        pdf.set_font("Arial", style="I", size=14)
        pdf.cell(w=0, h=10, text=f"Fecha: {self.fecha}", align="C")

        return pdf

    def guardar(self, pdf, nombre_archivo="certificado_paso4.pdf"):
        """Guarda el PDF en la carpeta del proyecto (junto a este .py)."""
        ruta = self.carpeta / nombre_archivo  # Une carpeta + nombre
        pdf.output(str(ruta))
        print(f"\nListo! Se guardo en:\n{ruta}")
        return ruta

    def generar(self):
        """Orquesta todo: pedir → crear → guardar."""
        self.pedir_datos()
        pdf = self.crear_pdf()
        self.guardar(pdf)


# --- Programa principal ---
# Solo se ejecuta si corres ESTE archivo (no si lo importas desde otro).
if __name__ == "__main__":
    generador = GeneradorCertificado()  # Creamos UN objeto
    generador.generar()                 # Le pedimos que haga el trabajo
