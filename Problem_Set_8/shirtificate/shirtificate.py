from fpdf import FPDF


class PDF(FPDF):
    def header(self):
        self.image("./shirtificate.png", 15, 70, 190)
        self.set_font("helvetica", "",30)
        # Printing title:
        self.cell(150, 10, "CS50 Shirtificate", border=0, align="C")
     

def main():
    name = input("Name: ")
    pdf = PDF()
    pdf.add_page(orientation="portrait", format="a4")
    pdf.set_font("helvetica", size=24)
    pdf.set_text_color(255,255,255)
    pdf.cell(-100, 213, f"{name} took CS50", align="C")
    pdf.output("shirtificate.pdf")

if __name__ == '__main__':
    main()