# from extractor.loader import read_pdf_pages
# from extractor.detector import find_tables_on_page
# from extractor.extractor import get_table_data
# from extractor.exporter import save_tables_to_excel
# import sys
# import os

# def extract_tables_from_pdf(pdf_file_path):
#     pdf_pages = read_pdf_pages(pdf_file_path)
#     tables_found = []

#     for page_index, page in enumerate(pdf_pages):
#         tables_in_page = find_tables_on_page(page)
#         for table_index, table in enumerate(tables_in_page):
#             table_content = get_table_data(table)
#             sheet_name = f"page_{page_index + 1}_table_{table_index + 1}"
#             tables_found.append((sheet_name, table_content))

#     output_file = os.path.splitext(pdf_file_path)[0] + ".xlsx"
#     save_tables_to_excel(tables_found, output_file)
#     print("Tables saved in:", output_file)

# if __name__ == "__main__":
#     if len(sys.argv) != 2:
#         print("Please run the script like this: python main.py path_to_pdf_file")
#     else:
#         extract_tables_from_pdf(sys.argv[1])


# main.py
import os
import sys
import fitz  # PyMuPDF
import pandas as pd
from extractor.loader import read_pdf_pages
from extractor.detector import find_tables_on_page
from extractor.extractor import get_table_data
from extractor.exporter import save_tables_to_excel


def extract_tables_from_pdf(pdf_file_path):
    try:
        pdf_pages = read_pdf_pages(pdf_file_path)
    except Exception as e:
        print(f"❌ Failed to read PDF: {e}")
        return

    tables_found = []

    for page_index, page in enumerate(pdf_pages):
        print(f"🔍 Processing page {page_index + 1}...")
        try:
            tables_in_page = find_tables_on_page(page)
            for table_index, table in enumerate(tables_in_page):
                table_content = get_table_data(table)
                sheet_name = f"page_{page_index + 1}_table_{table_index + 1}"
                tables_found.append((sheet_name, table_content))
        except Exception as e:
            print(f"❌ Unexpected error on page {page_index + 1}: {e}")

    if tables_found:
        output_file = os.path.splitext(pdf_file_path)[0] + ".xlsx"
        save_tables_to_excel(tables_found, output_file)
        print("✅ Tables saved in:", output_file)
    else:
        print("⚠️  No tables extracted. Excel file not created.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Please run the script like this: python main.py path_to_pdf_file")
    else:
        extract_tables_from_pdf(sys.argv[1])
