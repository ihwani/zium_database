from urllib import request
import openpyxl
import requests
from tqdm import tqdm

# Pc path
file_path = 'C:/github/zium_database'
# Mac path
# file_path = '/Users/ihwani/Documents/GitHub/zium_database'

excel_file = file_path + '/zium_database.xlsx'
json_file = file_path + '/zium_database_check.json'

wb = openpyxl.load_workbook(excel_file, read_only=True, data_only=True)

sheet = wb.worksheets[0]

url_list = []
for address_row_num in range(2, sheet.max_row + 1):
    url_list.append(sheet.cell(
        row=address_row_num, column=12).value)


print(len(url_list))

wb.close()

for i in range(len(url_list)):
    if requests.get(url_list[i]).status_code == 200:
        print(str(i)+'pass')
    else:
        print(str(i)+'error')
