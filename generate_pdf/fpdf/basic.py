from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", "B", 16)
pdf.cell(40, 10, "Hello", border=1)
pdf.cell(60, 10, 'Powered by FPDF.', 0, 1, 'C')
pdf.ln()  # line break
pdf.set_font("Arial", "", 12)
pdf.cell(30, 10, 'Cell after 2 line breaks', 0, ln=1, align='')  # ln line break
pdf.cell(30, 10, 'Cell after line break', 0, 1, 'C')
pdf.output('tuto1.pdf', 'F')  # save to file