import openpyxl
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

def check_table_style(file_path, sheet_name):
    if not os.path.exists(file_path):
        print(f"Error: '{file_path}' does not exist.")
        return
        
    wb = openpyxl.load_workbook(file_path)
    ws = wb[sheet_name]
    
    print("Tables in sheet:")
    for name, table in ws.tables.items():
        print(f"  Table Name: {name}")
        print(f"  Range: {table.ref}")
        if table.tableStyleInfo:
            print(f"  Style Name: {table.tableStyleInfo.name}")
            print(f"  Show Row Stripes: {table.tableStyleInfo.showRowStripes}")
            print(f"  Show Column Stripes: {table.tableStyleInfo.showColumnStripes}")

def main():
    file_path = r"C:\Users\thomas.winkler\Desktop\Projekte\Google Antigravity\ELEKTROPEPI\GEWAEHRLEISTUNG_GARANTIELABEL\alle gelisteten Artikel - Stand 24.06.2026.xlsx"
    sheet_name = "alle gelisteten Artikel"
    check_table_style(file_path, sheet_name)

if __name__ == "__main__":
    main()
