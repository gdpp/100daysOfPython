from fpdf import FPDF

pdf = FPDF()

pdf.add_page()
pdf.set_font("Arial", size=14)

pdf.cell(200, 10, txt="Hola mundo en pdf", ln=True, align="C")
pdf.cell(200, 10, txt="PDF generado con python", ln=True, align="C")

pdf.output("test.pdf")