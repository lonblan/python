# ============================================================
# PASO 6: Varios certificados de una sola vez
# ============================================================
# Idea: un colegio tiene una LISTA de alumnos.
# Recorremos la lista con un for y, por cada alumno,
# creamos UN PDF con su nombre (sin sobrescribir los demás).
#
# No usamos input(): los datos ya vienen en la lista.
# (Más adelante se podrían leer desde un Excel/CSV.)
# ============================================================

from pathlib import Path
from fpdf import FPDF


class GeneradorCertificado:
    """Fábrica de certificados PDF para uno o varios alumnos."""

    def __init__(self):
        self.carpeta = Path(__file__).resolve().parent
        # Subcarpeta solo para los PDFs de este paso
        self.carpeta_salida = self.carpeta / "certificados_lote"
        self.carpeta_salida.mkdir(exist_ok=True)  # La crea si no existe

        self.fuente_normal = "/System/Library/Fonts/Supplemental/Arial.ttf"
        self.fuente_negrita = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
        self.fuente_cursiva = "/System/Library/Fonts/Supplemental/Arial Italic.ttf"

        self.nombre = ""
        self.curso = ""
        self.fecha = ""

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

    def nombre_archivo_seguro(self, nombre_alumno):
        """
        Convierte el nombre en algo usable como nombre de archivo.
        Ejemplo: "Ana Pérez" → "Ana_Perez.pdf"
        (evita espacios y caracteres raros en el nombre del archivo)
        """
        seguro = (
            nombre_alumno
            .replace(" ", "_")
            .replace("á", "a").replace("é", "e").replace("í", "i")
            .replace("ó", "o").replace("ú", "u").replace("ñ", "n")
            .replace("Á", "A").replace("É", "E").replace("Í", "I")
            .replace("Ó", "O").replace("Ú", "U").replace("Ñ", "N")
        )
        return f"certificado_{seguro}.pdf"

    def guardar(self, pdf, nombre_archivo):
        """Guarda el PDF dentro de certificados_lote/."""
        ruta = self.carpeta_salida / nombre_archivo
        pdf.output(str(ruta))
        return ruta

    def generar_lote(self, alumnos, fecha):
        """
        Recibe una LISTA de diccionarios y crea un PDF por cada uno.

        alumnos = [
            {"nombre": "Ana Pérez", "curso": "Python"},
            ...
        ]
        """
        print(f"=== Generando {len(alumnos)} certificados ===\n")

        for alumno in alumnos:  # Misma idea que un for sobre una lista
            self.nombre = alumno["nombre"]
            self.curso = alumno["curso"]
            self.fecha = fecha

            pdf = self.crear_pdf()
            archivo = self.nombre_archivo_seguro(self.nombre)
            ruta = self.guardar(pdf, archivo)
            print(f"OK → {ruta.name}  ({self.nombre})")

        print(f"\nListo! Revisa la carpeta:\n{self.carpeta_salida}")


# --- Lista de ejemplo (como un colegio con 10 alumnos) ---
ALUMNOS = [
    {"nombre": "Ana Pérez", "curso": "Python"},
    {"nombre": "Luis Gómez", "curso": "Python"},
    {"nombre": "Sofía Ruiz", "curso": "Python"},
    {"nombre": "Carlos Mendoza", "curso": "Python"},
    {"nombre": "María López", "curso": "Python"},
    {"nombre": "Juan Torres", "curso": "Python"},
    {"nombre": "Elena Vargas", "curso": "Python"},
    {"nombre": "Pedro Sánchez", "curso": "Python"},
    {"nombre": "Laura Jiménez", "curso": "Python"},
    {"nombre": "Diego Ramírez", "curso": "Python"},
]

FECHA = "21 de septiembre de 2026"


if __name__ == "__main__":
    generador = GeneradorCertificado()
    generador.generar_lote(ALUMNOS, FECHA)
