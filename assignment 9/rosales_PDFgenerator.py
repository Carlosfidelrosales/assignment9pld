#   PDF Resume Creator
# 	Create a python program that will create your personal resume in PDF format
# 	All personal details are stored in a JSON file
# 	Your program should read the JSON file and write the details in the PDF
# 	The output file should be: LASTNAME_FIRSTNAME.pdf

import os as access
from fpdf import FPDF
import json

heading = 'CARLOS FIDEL A. ROSALES'
subheading = 'Computer Engineering Student'
finalpdf = 'ROSALES_CARLOSFIDEL.pdf'


subh1 = 'Personal Details'
subh2 = 'Contact Details'
subh3 = 'Educational Background'
subh4 = 'Achievements / Awards'
subh5 = 'Experience and Skills'
subh6 = 'Character Reference'

jsonfile = "primarydetails.json"

rosalesPDF = FPDF('P', 'mm', 'Legal') 
with open(jsonfile, "r") as obj: 
    charac = json.loads(obj.read()) 
rosalesPDF.add_page()


def header(rosalesPDF):
    rosalesPDF.image('design1.jpg', -1, 0, 230, 60)
    rosalesPDF.image('design2.jpg', -1, 299, 230, 60)
    rosalesPDF.image('2x2 ROSALES.png', 165, 28, 43, 0)
    rosalesPDF.set_font('times', 'b', 25)
    rosalesPDF.set_text_color(0, 0, 0)
    rosalesPDF.cell(180, 75, heading, ln = 1, align = 'C')
    rosalesPDF.set_font('times', 'b', 20)
    rosalesPDF.cell(180, -55, subheading, ln = 1, align = 'C')
    rosalesPDF.ln(25) 
    rosalesPDF.set_text_color(0, 0, 0)

def body1_json(rosalesPDF): 
    rosalesPDF.ln(10) 
    rosalesPDF.set_font("times", "B", 22) 
    rosalesPDF.cell(90, 10, subh1) 
    rosalesPDF.ln(10) 
    rosalesPDF.set_font("courier", "B", 11) 
    rosalesPDF.cell(40, 6, "Full Name       :  " + str(charac["personalIdentity"][0]["Full Name"]), ln = 10)
    rosalesPDF.cell(40, 6, "Sex             :  " + str(charac["personalIdentity"][0]["Sex"]), ln = 10)
    rosalesPDF.cell(40, 6, "Age             :  " + str(charac["personalIdentity"][0]["Age"]), ln = 10)
    rosalesPDF.cell(40, 6, "Address         :  " + str(charac["personalIdentity"][0]["Address"]), ln = 10)
    rosalesPDF.cell(40, 6, "Height          :  " + str(charac["personalIdentity"][0]["Height"]), ln = 10)
    rosalesPDF.cell(40, 6, "Weight          :  " + str(charac["personalIdentity"][0]["Weight"]), ln = 10)
    rosalesPDF.ln(8)

def body2_json(rosalesPDF): 
    rosalesPDF.set_font("times", "B", 22) 
    rosalesPDF.cell(90, 0, subh2) 
    rosalesPDF.ln(5) 
    rosalesPDF.set_font("courier", "B", 11) 
    rosalesPDF.cell(40, 6, "E-mail              :  " + str(charac["contactDetails"][0]["E-mail"]), ln = 10)
    rosalesPDF.cell(40, 6, "Phone Number        :  " + str(charac["contactDetails"][0]["Phone Number"]), ln = 10)
    rosalesPDF.cell(40, 6, "Facebook Account    :  " + str(charac["contactDetails"][0]["Facebook Account"]), ln = 10)
    rosalesPDF.ln(8) 

def body3_json(rosalesPDF): 
    rosalesPDF.set_font("times", "B", 22) 
    rosalesPDF.cell(90, 0, subh3) 
    rosalesPDF.ln(5) 
    rosalesPDF.set_font("courier", "B", 11) 
    rosalesPDF.cell(40, 6, "Elementary               :  " + str(charac["academicBackground"][0]["Elementary"]), ln = 10)
    rosalesPDF.cell(40, 6, "Junior High School       :  " + str(charac["academicBackground"][0]["Junior High School"]), ln = 10)
    rosalesPDF.cell(40, 6, "Senior High School       :  " + str(charac["academicBackground"][0]["Senior High School"]), ln = 10)
    rosalesPDF.cell(40, 6, "College                  :  " + str(charac["academicBackground"][0]["College"]), ln = 10)
    rosalesPDF.ln(8) 

def body4_json(rosalesPDF): 
    rosalesPDF.set_font("times", "B", 22) 
    rosalesPDF.cell(90, 0, subh4) 
    rosalesPDF.ln(5) 
    rosalesPDF.set_font("courier", "B", 11) 
    rosalesPDF.cell(40, 6, "*  " + str(charac["achievementsAward"][0]), ln = 10)
    rosalesPDF.cell(40, 6, "*  " + str(charac["achievementsAward"][1]), ln = 10)
    rosalesPDF.ln(0) 
    rosalesPDF.cell(40, 6, "*  " + str(charac["achievementsAward"][2]), ln = 10)
    rosalesPDF.cell(40, 6, "*  " + str(charac["achievementsAward"][3]), ln = 10)
    rosalesPDF.ln(0) 
    rosalesPDF.cell(40, 6, "*  " + str(charac["achievementsAward"][4]), ln = 10)
    rosalesPDF.cell(40, 6, "*  " + str(charac["achievementsAward"][5]), ln = 10)
    rosalesPDF.ln(0) 
    rosalesPDF.cell(40, 6, "*  " + str(charac["achievementsAward"][6]), ln = 10)
    rosalesPDF.ln(8) 

def body5_json(rosalesPDF): 
    rosalesPDF.image('bar1.png', 138, 250, 43, 0)
    rosalesPDF.image('bar2.png', 138, 255, 43, 0)
    rosalesPDF.image('bar3.png', 138, 261, 43, 0)
    rosalesPDF.image('bar4.png', 138, 267, 43, 0)
    rosalesPDF.set_font("times", "B", 22) 
    rosalesPDF.cell(90, 0, subh5) 
    rosalesPDF.ln(5) 
    rosalesPDF.set_font("courier", "B", 11) 
    rosalesPDF.cell(40, 6, "> Electronic Sports        :  " + str(charac["Skills"][0]["E-Sports"]), ln = 10)
    rosalesPDF.cell(40, 6, "> Photo Editing            :  " + str(charac["Skills"][0]["Photo Editing"]), ln = 10)
    rosalesPDF.cell(40, 6, "> Video Editing            :  " + str(charac["Skills"][0]["Video Editing"]), ln = 10)
    rosalesPDF.cell(40, 6, "> Hardware Service         :  " + str(charac["Skills"][0]["Hardware Service"]), ln = 10)
    rosalesPDF.ln(8) 

def body6_json(rosalesPDF): 
    rosalesPDF.set_font("times", "B", 22) 
    rosalesPDF.cell(90, 0, subh6) 
    rosalesPDF.ln(5) 
    rosalesPDF.set_font("courier", "B", 11) 
    rosalesPDF.cell(40, 6, "" + str(charac["characterReference"][0]), ln = 10)
    rosalesPDF.cell(40, 6, "" + str(charac["characterReference"][1]), ln = 10)
    rosalesPDF.cell(40, 6, "" + str(charac["characterReference"][2]), ln = 10)
    rosalesPDF.cell(40, 6, "" + str(charac["characterReference"][3]), ln = 10)
    rosalesPDF.cell(40, 6, "" + str(charac["characterReference"][4]), ln = 10)
    rosalesPDF.ln(8) 

def generatePDF():
    header(rosalesPDF) 
    body1_json(rosalesPDF) 
    body2_json(rosalesPDF)
    body3_json(rosalesPDF) 
    body4_json(rosalesPDF) 
    body5_json(rosalesPDF) 
    body6_json(rosalesPDF) 
    
generatePDF()


rosalesPDF.set_auto_page_break(margin = 0.5, auto = True) 
rosalesPDF.output(finalpdf)
access.startfile(finalpdf)




