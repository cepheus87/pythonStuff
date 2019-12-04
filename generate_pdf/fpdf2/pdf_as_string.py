from fpdf import FPDF

pdf = FPDF("P", "mm", "A4")
pdf.add_page()
pdf.set_font("Arial", "B", 16)
pdf.cell(40, 10, "Hello", border=1)

pdf_str = pdf.output("", "S")  # save to file

with open("from_str.pdf", "wb") as f:
    f.write(pdf_str)
