__author__ = 'Wilro - https://github.com/SciWilro'
# Not a good example of the code
# Tutorial: https://pyfpdf.github.io/fpdf2/Tutorial.html

# TODO Rewrite this whole script - It's bad

from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        # Setting font: helvetica bold 48
        self.set_font("helvetica", "B", 48)
        # width=0 fills whole horizontal area
        # h=pdf.eph/8 devides the variable for 'effective page hight' by 8
        self.cell(w=0, h=self.eph/6, txt="CS50 Shirtificate", border=0, new_x="LEFT", new_y="NEXT", align="C")
        # Performing a line break:
        self.ln(20)
        
    def set_auto_page_break(self, auto, margin=0):
        self.auto_page_break = False
        self.b_margin = margin

def print_shirt(name: str):
    pdf = PDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    # Header inherited from subclass defined above
    # Add image - width equal to the page
    pdf.image(name="./shirtificate.png", w=pdf.epw)
    # Adding name
    # Font + colour (grayscale (black = 0 -> white = 255))
    pdf.set_font("helvetica", "B", 22)
    pdf.set_text_color(255)
    # Dummy cell - to position cursor - I hate working with PDFs
    pdf.cell(w=0, txt="", new_x="LEFT", new_y="TMARGIN")
    pdf.cell(w=0, h=250, txt=f"{name} took CS50", align="C")
    pdf.output("./shirtificate.pdf")

def main():
    name = input("What name do you want printed")
    print_shirt(name)
    
    
if __name__ == '__main__':
    main()
