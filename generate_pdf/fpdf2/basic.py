from fpdf import FPDF

pdf = FPDF("P", "mm", "A4")
pdf.add_page()
pdf.set_font("Arial", "B", 16)
pdf.cell(40, 10, "Hello", border=1)
pdf.cell(60, 10, 'Powered by FPDF.', 0, 1, 'C')
pdf.ln()  # line break
pdf.set_font("Arial", "", 12)
pdf.cell(30, 10, 'Cell after 2 line breaks', 0, ln=1, align='')  # ln line break
pdf.cell(30, 10, 'Cell after line break', 0, 1, 'C')

long_txt = "safdasf asfsdgh  sdgsdg asfsd sd efr dsf sedr sdf ser ar a wrf e ff a w daw dwa dwa dawd awd a rgdfg ; ';ld;lfsdl ja;k woajdk ;alk [wp da;lkd a;lw pa['f aofopepofik l;s,; qawp[' olopew gkjlsdmf'alwd;lw;a kfdoa;kf "

pdf.multi_cell(180, 10, long_txt, 0, "L", ln=1)


pdf.cell(30, 10, 'Some next cell', 0, 1, 'C')

# two columns:
top = pdf.y
offset = pdf.x + 40
pdf.multi_cell(40, 10,'Hello World!,how are you today',1,0)

# Reset y coordinate
pdf.y = top
# Move to computed offset
pdf.x = offset
pdf.multi_cell(100,10,'This cell needs to beside the other',1,0)


pdf.output('basic.pdf', 'F')  # save to file

# pdf_str = pdf.output("", "S")
#
# with open("basic2.txt", "w") as f:
#     f.write(pdf_str)
#
# pdf_str_enc = pdf_str.encode("")
#
# with open("basic3.pdf", "wb") as f:
#     f.write(pdf_str_enc)
