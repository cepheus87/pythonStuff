from fpdf import FPDF
import numpy as np
import matplotlib.pyplot as plt
import os
import tempfile

pdf = FPDF("P", "mm", "A4")
pdf.add_page()
pdf.set_font("Arial", "B", 16)
pdf.cell(10, 10, "Title", 0, 1, "C")
pdf.set_font("Arial", "", 12)
pdf.cell(30, 10, 'Some Cell ', 0, ln=1, align='')  # ln line break


fig_file = "fig.png"

if not os.path.exists(fig_file):
    gaus = np.random.normal(10, 2, 100)
    fig = plt.hist(gaus)
    plt.savefig(fig_file)


pdf.image(fig_file)
pdf.image(fig_file, w=100, h=100)


gaus2 = np.random.normal(20, 5, 100)
fig = plt.hist(gaus2)
temp_file = tempfile.NamedTemporaryFile("w+b", suffix=".png")
temp_file_name = str(temp_file.name)

plt.savefig(temp_file.name, format="png")
pdf.image(temp_file.name)

pdf.output('image.pdf', 'F')  # save to file

