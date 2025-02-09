import requests
import pdfplumber
from tabulate import tabulate

def scrapeData():
    URL = "https://www.vch.ca/en/Documents/VCH-beach-gmean.pdf"
    local_pdf = "beach_report.pdf"

    #download pdf
    response = requests.get(URL)
    with open(local_pdf, "wb") as f:
        f.write(response.content)
    print("pdf downloaded")

    beach_data = [] #make beach data master list

    with pdfplumber.open(local_pdf) as pdf: #read pdf
        for page in pdf.pages: #loop through pages
            tables = page.extract_tables() #get all tables on page
            for table in tables: #loop through tables
                for row in table: #loop through rows
                    if (row[0] != "Geometric Mean\nArea Beach (Ecoli MPN/100mL) Calculated On"): #remove Geometric Mean rows

                        #add beach data to master list
                        beach_data.append({
                            "name": row[1].strip(),
                            "ecoli_level": row[2].strip(),
                            "sample_date": row[3].strip()
                        })

    return beach_data

#print(tabulate(beach_data, headers="keys", tablefmt="grid"))
