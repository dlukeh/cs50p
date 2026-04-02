from fpdf import FPDF


# Inherit directly from FPDF
class PDF(FPDF):
    def __init__(self, name):
        # Initialize the parent FPDF class
        super().__init__()
        self.add_page()

        # 1. Header Logic
        self.set_font("helvetica", "B", 45)
        self.cell(0, 60, "CS50 Shirtificate", align="C", new_x="LMARGIN", new_y="NEXT")

        # 2. Image Logic (Centering automatically)
        # Using self.epw for width is smart!
        # To center it, we calculate the x offset
        x_offset = (self.w - self.epw) / 2
        self.image("shirtificate.png", x=x_offset, y=70, w=self.epw)

        # 3. Text Overlay Logic
        self.set_font("helvetica", "B", 25)
        self.set_text_color(255, 255, 255)

        # Move the 'cursor' to the middle of the shirt
        self.set_y(140)
        self.cell(0, 10, f"{name} took CS50", align="C")


def main():
    name = input("Name: ")
    pdf = PDF(name)
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
