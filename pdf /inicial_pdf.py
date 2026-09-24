from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", "B", 16)
pdf.cell(w=0, h=20, text="CERTIFICADO DE CURSO", align="C")
pdf.output("mi_primer_certificado.pdf")


print("PDF creado correctamente")