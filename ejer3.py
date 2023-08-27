from fpdf import FPDF

class PDF(FPDF):

    def tabla(self):
        #encabezado
        self.set_fill_color(100,100,100)
        self.cell(20,10,"Codigo",1,0,'C',1)
        self.cell(50,10,"Producto",1,0,'C',1)
        self.cell(20,10,"Precio",1,0,'C',1)
        self.ln()
        #valores de tabla
        self.cell(20,10,"10",1,0,'C',0)
        self.cell(50,10,"Televisor",1,0,'C',0)
        self.cell(20,10,"120000",1,0,'C',0)

pdf=PDF()

pdf.add_page()
pdf.set_font('Arial','B',12)
pdf.tabla()
pdf.output("tabla.pdf",'F')
