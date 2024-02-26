import pandas as pd
import glob
import fpdf
import pathlib

# Get files
filepaths = glob.glob("invoices/*.xlsx")

for filepath in filepaths:

    # Create a PDF
    document = fpdf.FPDF("P", "mm", "A4")

    # Extract data from excel sheets
    df = pd.read_excel(filepath, sheet_name="Sheet 1")

    # Get the file name for naming and indexing
    filename = pathlib.Path(filepath).stem
    filenum = filename.split("-")[0]

    # Create the output PDF
    document.add_page()
    document.set_font("Times", "B", 24)
    document.cell(w=5, h=1, txt=f"Invoice {filenum}")
    document.output(f"PDFs/invoice-{filenum}.pdf")
