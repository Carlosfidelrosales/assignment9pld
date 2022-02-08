from fpdf import FPDF

heading = 'CARLOS FIDEL A. ROSALES'
subheading = 'Personal Details'
finalpdf = 'ROSALES_CARLOSFIDEL.pdf'
jsonfile = 'primarydetails.json'

# I used FPDF module in generating my own resume
class PDF(FPDF):
    def header(self):
        self.image('design1.jpg', -1, 0, 230, 60)
        self.image('2x2 ROSALES.png', 160, 4, 40, 0)
        self.set_font('times', 'B', 25)
        self.cell(180, 20, heading, ln = 1, align = 'C'); 
        self.cell(180, 20, subheading, align = 'C')
        self.ln(14) 
        #self.image('rectangle.png', 0, 0, 45, 370)
        

    def body_json(self, name):
        with open(jsonfile) as obj: 
            chr = obj.read() 
        self.set_font("helvetica", "B", 15) 
        self.multi_cell(0, 5, chr)
        

    def chapterOpt(self, num, title, name): 
        self.add_page()
        self.body_json(name)



rosalesPDF = PDF('P', 'mm', 'Legal')
rosalesPDF.set_auto_page_break(margin = 0.5, auto = True) 
rosalesPDF.chapterOpt(1, "", jsonfile)


rosalesPDF.output(finalpdf)