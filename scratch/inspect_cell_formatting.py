import openpyxl
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

def inspect_cell_formatting(file_path, sheet_name):
    if not os.path.exists(file_path):
        print(f"Error: '{file_path}' does not exist.")
        return
        
    wb = openpyxl.load_workbook(file_path, data_only=True)
    ws = wb[sheet_name]
    
    # Let's inspect row 1 (header) and row 2 (first data row)
    for row_idx in [1, 2, 3]:
        print(f"\nRow {row_idx}:")
        for col_idx in range(1, 7):
            cell = ws.cell(row=row_idx, column=col_idx)
            val = cell.value
            fill = cell.fill
            font = cell.font
            
            fill_type = fill.fill_type if fill else 'None'
            fg_color = fill.fgColor.value if fill and fill.fgColor else 'None'
            bg_color = fill.bgColor.value if fill and fill.bgColor else 'None'
            
            font_name = font.name if font else 'None'
            font_size = font.size if font else 'None'
            font_bold = font.bold if font else 'None'
            font_color = font.color.value if font and font.color else 'None'
            
            print(f"  Col {col_idx} '{val}':")
            print(f"    Fill: type={fill_type}, fgColor={fg_color}, bgColor={bg_color}")
            print(f"    Font: name={font_name}, size={font_size}, bold={font_bold}, color={font_color}")

def main():
    source_file = r"C:\Users\thomas.winkler\Desktop\Projekte\Google Antigravity\ELEKTROPEPI\GEWAEHRLEISTUNG_GARANTIELABEL\alle gelisteten Artikel - Stand 24.06.2026.xlsx"
    generated_file = r"C:\Users\thomas.winkler\Desktop\Projekte\Google Antigravity\ELEKTROPEPI\GEWAEHRLEISTUNG_GARANTIELABEL\Lieferanten\A.S.SAT-ANTENNENZUBEHÖR\A.S.SAT-ANTENNENZUBEHÖR_Garantieabfrage.xlsx"
    
    print("=== SOURCE FILE ===")
    inspect_cell_formatting(source_file, "Garantiedaten_Erfassung")
    
    print("\n=== GENERATED FILE ===")
    inspect_cell_formatting(generated_file, "Garantiedaten_Erfassung")

if __name__ == "__main__":
    main()
