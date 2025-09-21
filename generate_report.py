from fpdf import FPDF
from datetime import datetime

summary_file = "analysis_summary.txt"

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 15)
        self.cell(0, 10, 'SaturnX Industrial Asset Monitoring Report', 0, 1, 'C')
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

def generate_pdf():
    pdf = PDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    with open(summary_file, 'r') as file:
        for line in file:
            pdf.cell(0, 10, txt=line.strip(), ln=True)

    filename = f"Asset_Report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
    pdf.output(filename)
    print(f"PDF report generated: {filename}")

if __name__ == "__main__":
    generate_pdf()
