from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font('Arial', 'B', 20)
pdf.cell(180, 10, 'Hello World!',1,0,'C')
pdf.ln()
pdf.ln()
pdf.cell(180, 10, 'Formato pdf!',0,0,'C')
pdf.output('tuto1.pdf', 'F')