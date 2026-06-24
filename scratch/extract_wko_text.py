import re
from bs4 import BeautifulSoup

file_path = r"C:\Users\thomas.winkler\.gemini\antigravity\brain\c0963404-99f0-498e-9958-b86a3114c369\.system_generated\steps\544\content.md"

with open(file_path, "r", encoding="utf-8") as f:
    html = f.read()

# Parse the HTML with BeautifulSoup
soup = BeautifulSoup(html, "html.parser")
text = soup.get_text()

# Clean up whitespace
text = re.sub(r'\s+', ' ', text)

# Write to a clean file for inspection
clean_file = r"C:\Users\thomas.winkler\Desktop\Projekte\Google Antigravity\ELEKTROPEPI\GEWAEHRLEISTUNG_GARANTIELABEL\scratch\clean_wko_text.txt"
with open(clean_file, "w", encoding="utf-8") as f:
    f.write(text)

print(f"Extracted {len(text)} characters. Saved to clean_wko_text.txt.")

# Search for mentions of manufacturer/supplier/cooperation
search_terms = ["Hersteller", "Lieferant", "Pflicht", "muss", "Garantie"]
for term in search_terms:
    matches = [m.start() for m in re.finditer(term, text, re.IGNORECASE)]
    print(f"Keyword '{term}': {len(matches)} matches.")
    for i, idx in enumerate(matches[:5]):
        start = max(0, idx - 150)
        end = min(len(text), idx + 150)
        print(f"  Match {i+1}: ... {text[start:end].strip()} ...")
