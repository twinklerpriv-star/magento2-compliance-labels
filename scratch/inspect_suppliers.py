import openpyxl
import os
import sys
from collections import Counter

sys.stdout.reconfigure(encoding='utf-8')

def analyze_suppliers(file_path, sheet_name):
    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' does not exist.")
        return
        
    wb = openpyxl.load_workbook(file_path, read_only=True)
    ws = wb[sheet_name]
    
    suppliers = []
    row_count = 0
    blank_suppliers = 0
    
    for row in ws.iter_rows(values_only=True):
        row_count += 1
        if row_count == 1:
            continue
        
        supplier_name = row[1] # Column 2: Lieferant Zuname
        if supplier_name:
            suppliers.append(str(supplier_name).strip())
        else:
            blank_suppliers += 1
            
    supplier_counts = Counter(suppliers)
    
    print(f"Total Rows (excluding header): {row_count - 1}")
    print(f"Unique Suppliers: {len(supplier_counts)}")
    print(f"Rows with blank supplier names: {blank_suppliers}")
    
    # Sort suppliers by count descending
    print("\nTop 15 Suppliers by product count:")
    for sup, count in supplier_counts.most_common(15):
        print(f"  - '{sup}': {count} products")
        
    # Check for small suppliers (e.g. only 1-2 products)
    small_suppliers = sum(1 for sup, count in supplier_counts.items() if count <= 2)
    print(f"\nSuppliers with 2 or fewer products: {small_suppliers}")

def main():
    file_path = r"C:\Users\thomas.winkler\Desktop\Projekte\Google Antigravity\ELEKTROPEPI\GEWAEHRLEISTUNG_GARANTIELABEL\alle gelisteten Artikel - Stand 24.06.2026.xlsx"
    sheet_name = "alle gelisteten Artikel"
    analyze_suppliers(file_path, sheet_name)

if __name__ == "__main__":
    main()
