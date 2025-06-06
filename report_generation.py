import csv
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

# Load data from CSV file
csv_file = 'employee_data.csv'
data = []

with open(csv_file, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        data.append(row)

# Create PDF document
pdf_file = 'employee_report.pdf'
document = SimpleDocTemplate(pdf_file, pagesize=A4)
styles = getSampleStyleSheet()
elements = []

# Add title
title = Paragraph("Employee Report", styles['Title'])
elements.append(title)
elements.append(Spacer(1, 12))

# Create table
table = Table(data)
table_style = TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.orange),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
    ('FONTSIZE', (0, 0), (-1, -1), 10),
    ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
])
table.setStyle(table_style)

elements.append(table)

# Build the PDF
document.build(elements)

print(f"PDF report '{pdf_file}' generated successfully.")
