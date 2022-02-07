from fpdf import FPDF

heading = 'CARLOS FIDEL A. ROSALES'
subheading = 'Computer Engineering Student'
FINALE = 'ROSALES_CARLOSFIDEL.pdf'

# I used FPDF module in generating my own resume

rosalesPDF = FPDF('P', 'mm', 'Letter');

rosalesPDF.add_page()

rosalesPDF.set_font('times', 'B', 23)
rosalesPDF.set_margins(12.7, 12.7, 12.7)


rosalesPDF.cell(85, 10, heading, border= False, ln= 1)
rosalesPDF.cell(85, 10, subheading, border= False)






rosalesPDF.output(FINALE)