import re

file_path = r"C:\Users\thomas.winkler\.gemini\antigravity\brain\c0963404-99f0-498e-9958-b86a3114c369\.system_generated\steps\544\content.md"

with open(file_path, "r", encoding="utf-8") as f:
    html = f.read()

# Decode unicode escape sequences like \u00fcr
def decode_escapes(s):
    return re.sub(r'\\u([0-9a-fA-F]{4})', lambda m: chr(int(m.group(1), 16)), s)

html_decoded = decode_escapes(html)
text = re.sub(r'<[^>]+>', ' ', html_decoded)
text = re.sub(r'\s+', ' ', text)

keywords = ["verpflicht", "Hersteller", "Lieferant", "Garantie", "Label"]

print("=== KEYWORD SEARCH IN WKO CONTENT (DECODED) ===")
for kw in keywords:
    print(f"\nMatches for keyword '{kw}':")
    matches = [m.start() for m in re.finditer(kw, text, re.IGNORECASE)]
    print(f"Found {len(matches)} matches.")
    # Print the first 5 matches with 200 chars context
    for i, idx in enumerate(matches[:5]):
        start = max(0, idx - 100)
        end = min(len(text), idx + 100)
        print(f"  Match {i+1}: ... {text[start:end].strip()} ...")
