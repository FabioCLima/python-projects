from fpdf import FPDF
import webbrowser


class Bill:
    """[Object that contains data about a bill, such as total amount
    and period of the bill]
    """

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:
    """[Creates a flatmate person who lives in the flat and pays a shared
    of the bill.]
    """

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill):
        """[summary]

        Args:
            bill ([bill]): [instance object from bill class has amount
            property]

        Returns:
            has_to_pay[float]: [amount of each flatmate has to pay for the
            bill.]
        """
        has_to_pay = (bill.amount * self.days_in_house) / 60
        return has_to_pay


class PdfReport:
    """[Creates a Pdf file that contains data about the flatmates,
    such as their names, their due amount and the period of the bill]
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        # Add image
        pdf.image("house.png", w=30, h=30)

        # Insert title

        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt='Flatmates Bill', align="C", ln=1)

        # Insert Period label and value
        pdf.cell(w=100, h=40, txt='Period:')
        pdf.cell(w=150, h=40, txt=bill.period, ln=1)

        # Insert name and due amount of the first flatmate
        pdf.set_font(family="Times", size=15)
        pdf.cell(w=150, h=25, txt=flatmate1.name)
        pdf.cell(w=120, h=25, txt=f"R${flatmate1.pays(bill):.2f}", ln=1)

        # Insert name and due amount of the second flatmate
        pdf.cell(w=150, h=25, txt=flatmate2.name)
        pdf.cell(w=120, h=25, txt=f"R${flatmate2.pays(bill):.2f}", ln=1)

        pdf.output(self.filename)
        webbrowser.open(self.filename)
