from main import (Bill, Flatmate, PdfReport)
from input_data import input_data

amount, period, flatmate1, days_in_house1, flatmate2, days_in_house2 \
    = input_data()


bill = Bill(amount=amount, period=period)  # instância da class bill
flatmate1 = Flatmate(name=flatmate1, days_in_house=days_in_house1)
flatmate2 = Flatmate(name=flatmate2, days_in_house=days_in_house2)

flatmate1_has_to_pay = flatmate1.pays(bill=bill)
print(f"The flatmate1 pays: {flatmate1.name} stayed at the flat for"
      f" {flatmate1.days_in_house} days and he has to pay for the bill",
      f" {flatmate1_has_to_pay:.2f} reais")

flatmate2_has_to_pay = flatmate2.pays(bill=bill)
print(f"The flatmate2 pays: {flatmate2.name} stayed at the flat for"
      f" {flatmate2.days_in_house} days and she has to pay for the bill",
      f" {flatmate2_has_to_pay:.2f} reais")

pdf_report = PdfReport(filename="Report1.pdf")
pdf_report.generate(flatmate1=flatmate1, flatmate2=flatmate2, bill=bill)
