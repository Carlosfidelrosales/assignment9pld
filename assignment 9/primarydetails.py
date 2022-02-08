import json

my_resume = {

    "personalIdentity": [
        {
            "Full Name": "Carlos Fidel A. Rosales",
            "Sex": "Male",
            "Age": "18 Years Old",
            "Address": "#123 Backdoor Street, Bambang, Taguig City",
            "Height": "5'5",
            "Weight": "90 kg"
        }
    ],
    "contactDetails": [
        {
            "E-mail": "carlitofudelito302@gmail.com",
            "Phone Number": "0921-335-6789",
            "Facebook Account": "Carlito Pidel"
        }
    ],
    "academicBackground": [
        {
        "Kindergarten": "Pacita Complex Day Care Center",
        "Elementary": "Taguig Integrated School",
        "Junior High School)": "Bagumbayan National High School",
        "Senior High School (11th to 12th Grade)": "Bagumbayan National High School",
        "College": "Oxford University"
        }
    ],
    "kindergartenAwards": [
        "Best in English",
        "Cutest Student",
        "Most Diligent"
    ],
    "elementaryAwards": [
        "Top 8 of the Section (Grades 4 to 5)",
        "Katangi-tanging Student Award"
    ],
    "juniorHighAwards": [
        "Academic Excellence Awardee (With Honors)"
    ],
    "seniorHighAwards": [
        "Academic Excellence Awardee (With High Honors)"
    ],
    "collegeAwards": [
        "N/A"
    ],
    "identityReference": [
        "Jett Diffe",
        "Businesswoman",
        "University of the Philippines Diliman",
        "0912-345-6789",
        "jettdiffe23@up.edu.ph"
    ],
    "personalExperience": [
        {
        "E-Sports": "Radiant - VALORANT",
        "Photo Editing": "Photoshop",
        "Video Editing": "Wondershare Filmora",
        "Hardware Service": "Computer Technician"
        }
    ]
}
json_file = json.dumps(my_resume, indent=2)
with open("primarydetails.json", "w") as resume: 
    resume.write(json_file)