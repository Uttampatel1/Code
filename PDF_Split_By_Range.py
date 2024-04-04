import PyPDF2
import os
from zipfile import ZipFile

def split_pdf(input_pdf, output_directory, page_ranges):
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    with open(input_pdf, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for i, page_range in enumerate(page_ranges, start=1):
            start, end = page_range
            writer = PyPDF2.PdfWriter()
            for page_num in range(start - 1, end):
                writer.add_page(reader.pages[page_num])

            output_pdf = os.path.join(output_directory, f'output_{i}.pdf')
            with open(output_pdf, 'wb') as out_file:
                writer.write(out_file)

def create_zip(output_directory, zip_filename):
    with ZipFile(zip_filename, 'w') as zipf:
        for root, dirs, files in os.walk(output_directory):
            for file in files:
                zipf.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), output_directory))

if __name__ == "__main__":
    input_pdf = r'I:\Common\Uttam\paper 03_04_2024\US 9.221,808.pdf'
    output_directory = 'output_pdfs'
    page_ranges = [(34,36), (37, 39), (40, 43), (44,46), (47, 49), (50, 52) , (63,63), (66, 66)]  # Example: [(start_page1, end_page1), (start_page2, end_page2), ...]
    zip_filename = 'output.zip'

    split_pdf(input_pdf, output_directory, page_ranges)
    create_zip(output_directory, zip_filename)
