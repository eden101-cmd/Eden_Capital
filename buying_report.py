import pandas as pd
#multiple files can be a clue for list
import glob
from fpdf import FPDF
from pathlib import Path
import shutil #built in model in python
import datetime


def make_pdf(csv_file):
    global columns
    current_date = datetime.date.today()
    formatted_date = current_date.strftime("%Y-%m-%d")
    # Replace the paths below with the actual file paths for your Excel file and the new copy
    # original_file_path = "invoices/10001-2023.1.18.xlsx"
    # new_file_path = "invoices/Buying_report.xlsx"
    # shutil.copy2(original_file_path, new_file_path)
    filepath = glob.glob("invoices/Buying_report.xlsx")[0]
    pdf = FPDF(orientation="P", unit="mm", format="A4")  # creating a pdf file
    pdf.add_page()  # adding a page
    filename = Path(filepath).stem
    buying_1 = filename.split("_")[0]
    report_1 = filename.split("_")[1]
    pdf.set_font(family="Times", size=16, style="B")  # creating a tile
    pdf.cell(w=50, h=8, txt=f"{buying_1} {report_1}", ln=1)  # ln -> indicate of one break line
    pdf.set_font(family="Times", size=16, style="B")  # creating a tile
    pdf.cell(w=50, h=8, txt=f"Date :{formatted_date}", ln=1)
    df = pd.read_excel(filepath, sheet_name="Sheet 1")  # the name of the sheet in the excel
    # add header:
    columns = df.columns
    columns = [column.replace("_", " ").title() for column in columns]
    pdf.set_font(family="Times", size=10, style="B")
    pdf.set_text_color(80, 80, 80)
    pdf.cell(w=30, h=8, txt=columns[0], border=1)
    pdf.cell(w=70, h=8, txt=columns[1], border=1)
    pdf.cell(w=30, h=8, txt=columns[2], border=1)
    pdf.cell(w=30, h=8, txt=columns[3], border=1)
    pdf.cell(w=30, h=8, txt=columns[4], border=1, ln=1)
    df = pd.read_csv(csv_file)
    print(df)
    for index, row in df.iterrows():
        pdf.set_font(family="Times", size=10, style="B")
        pdf.set_text_color(80, 80, 80)
        pdf.cell(w=30, h=8, txt=str(row["ID"]), border=1)
        pdf.cell(w=70, h=8, txt=str(row["Product Name"]), border=1)
        pdf.cell(w=30, h=8, txt=str(row["Quantity"]), border=1)
        pdf.cell(w=30, h=8, txt=str(row["Price"]), border=1)
        pdf.cell(w=30, h=8, txt=str(row["Total"]), border=1, ln=1)
    total_sum = df["Total"].tolist()
    pdf.set_font(family="Times", size=10, style="B")
    pdf.set_text_color(80, 80, 80)
    pdf.cell(w=30, h=8, txt="", border=1)
    pdf.cell(w=70, h=8, txt="", border=1)
    pdf.cell(w=30, h=8, txt="", border=1)
    pdf.cell(w=30, h=8, txt="", border=1)
    pdf.cell(w=30, h=8, txt=str(total_sum[0]), border=1, ln=1)
    pdf.set_font(family="Times", size=10, style="B")
    pdf.cell(w=30, h=8, txt=f"the total price is: {total_sum[0]}", ln=1)
    # add company name and logo
    pdf.set_font(family="Times", size=14, style="B")
    pdf.cell(w=25, h=8, txt=f"Eden_Capital")
    # pdf.image("pythonhow.png",w=10)
    pdf.output(f"PDF/{filename}.pdf")


