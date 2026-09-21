# ============================================================
# PASO 8: Borde decorativo en el certificado
# ============================================================
# Hasta ahora el PDF era texto sobre hoja blanca.
# Ahora dibujamos un MARCO (doble borde) alrededor.
#
# Novedades de fpdf2:
#   set_draw_color(r, g, b)  → color de la línea
#   set_line_width(mm)       → grosor
#   rect(x, y, w, h)         → dibuja un rectángulo
#
# Coordenadas en mm (hoja horizontal A4 = 297 x 210):
#   x = desde la izquierda
#   y = desde arriba
# ============================================================

from pathlib import Path
from fpdf import FPDF


class GeneradorCertificado:
    """Certificado con borde decorativo."""

    def __init__(self):
        self.carpeta = Path(__file__).resolve().parent
        self.fuente_normal = "/System/Library/Fonts/Supplemental/Arial.ttf"
        self.fuente_negrita = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
        self.fuente_cursiva = "/System/Library/Fonts/Supplemental/Arial Italic.ttf"
        self.nombre = ""
        self.curso = ""
        self.fecha = ""

    def pedir_datos(self):
        print("=== Certificado con borde ===\n")
        self.nombre = input("Nombre del alumno: ")
        self.curso = input("Nombre del curso: ")
        self.fecha = input("Fecha: ")

    def dibujar_borde(self, pdf):
        """Dibuja un doble marco alrededor de la página."""
        # Ancho y alto útiles de la página (A4 horizontal)
        ancho = pdf.w   # ~297 mm
        alto = pdf.h    # ~210 mm

        # --- Borde exterior (más grueso, color azul oscuro) ---
        pdf.set_draw_color(25, 55, 110)  # RGB
        pdf.set_line_width(1.8)
        margen_ext = 10  # mm desde el borde del papel
        pdf.rect(
            x=margen_ext,
            y=margen_ext,
            w=ancho - 2 * margen_ext,
            h=alto - 2 * margen_ext,
        )

        # --- Borde interior (más fino) ---
        pdf.set_draw_color(25, 55, 110)
        pdf.set_line_width(0.6)
        margen_int = 14
        pdf.rect(
            x=margen_int,
            y=margen_int,
            w=ancho - 2 * margen_int,
            h=alto - 2 * margen_int,
        )

    def crear_pdf(self):
        pdf = FPDF(orientation="L", unit="mm", format="A4")
        pdf.add_page()

        # 1) Primero el marco (queda "detrás" del texto)
        self.dibujar_borde(pdf)

        # 2) Luego el texto (igual que en pasos anteriores)
        pdf.add_font("Arial", style="", fname=self.fuente_normal)
        pdf.add_font("Arial", style="B", fname=self.fuente_negrita)
        pdf.add_font("Arial", style="I", fname=self.fuente_cursiva)

        pdf.set_y(40)  # Bajamos un poco para no pegar al borde

        pdf.set_font("Arial", style="B", size=28)
        pdf.cell(w=0, h=20, text="CERTIFICADO DE CURSO", align="C")
        pdf.ln(28)

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

    def guardar(self, pdf, nombre_archivo="certificado_con_borde.pdf"):
        ruta = self.carpeta / nombre_archivo
        pdf.output(str(ruta))
        print(f"\nListo! Se guardo en:\n{ruta}")
        return ruta

    def generar(self):
        self.pedir_datos()
        pdf = self.crear_pdf()
        self.guardar(pdf)


if __name__ == "__main__":
    generador = GeneradorCertificado()
    generador.generar()
