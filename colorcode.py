from bs4 import BeautifulSoup
from tkinter.filedialog import askopenfilename
import re
import xlrd
import xlsxwriter

hex_code = []
result = []
status = []


def check_values(result):
    workbook = xlsxwriter.Workbook('Audit_file.xlsx')
    worksheet = workbook.add_worksheet()

    header_format = workbook.add_format({'bold': 1})
    headers = ("Color Code", "Status")

    # Write some data headers.
    worksheet.write_row(0, 0, headers, header_format)

    # Start from the first cell below the headers.
    row_no = 1
    col_no = 0
    for res in result:
        for row in res:

            for x in row:
                worksheet.write(row_no,col_no, x)
                row_no += 1
            row_no = 1
            col_no += 1

    workbook.close()


if __name__ == '__main__':
    html_sheet_input = askopenfilename(filetypes=[('HTML', '*.html')])
    excel_sheet_input = askopenfilename(filetypes=[('Excel', ('*.xls', '*.xlsx'))])
    wb = xlrd.open_workbook(excel_sheet_input)
    sheet = wb.sheet_by_index(0)
    sheet.cell_value(0, 0)

    for i in range(sheet.nrows):
        hex_code.append(sheet.cell_value(i, 0))

    with open(html_sheet_input, "r") as f:
        soup = BeautifulSoup(f, 'lxml')
        style = str(soup)
        codes = re.findall(r'#([a-fA-F0-9]{6}){1,2}\b', style)
        color_codes = []
        for code in codes:
            code = code.upper()
            code = ('#' + code)
            color_codes.append(code)
            
        # hex_codes = []
        # for code in codes:
        #     code = code.upper()
        #     code = ('#' + code)
        #     hex_codes.append(code)
        #
        # hex_codes = set(hex_codes)

        for code in color_codes:
            if code in hex_code:
                op = "Hex color is valid"
                status.append(op)
            else:
                op = "Hex color is not valid"
                status.append(op)
        result.append([color_codes, status])
    check_values(result)

