import urllib.request
import urllib.parse
import json
import os
import csv

api_key = "a0eb1419466cef8904285c21a094a99e63708fd59d3f101d8fa1205d275b2396"
endpoint = "https://api.garan-label.com/api.php"

def generate_label(brand, model, duration, output_path):
    payload = {
        "brand": brand,
        "model": model,
        "duration": str(duration),
        "sandbox": "1"  # Test-Modus mit Wasserzeichen (0 für Echtbetrieb)
    }
    
    data = urllib.parse.urlencode(payload).encode("utf-8")
    req = urllib.request.Request(endpoint, data=data, headers={"X-API-Key": api_key})
    
    try:
        with urllib.request.urlopen(req) as response:
            res_data = json.loads(response.read().decode("utf-8"))
            if res_data.get("success"):
                url = res_data.get("url")
                print(f"-> Erfolg für {brand} {model} ({duration} Jahre): {url}")
                # Herunterladen und Speichern des Bildes
                urllib.request.urlretrieve(url, output_path)
                print(f"   Bild gespeichert unter: {output_path}")
                return True
            else:
                print(f"-> Fehler für {brand} {model}: {res_data.get('error')}")
                return False
    except Exception as e:
        print(f"-> HTTP-Fehler für {brand} {model}: {e}")
        return False

def process_csv(csv_path):
    print(f"Lese CSV-Datei ein: {csv_path}")
    if not os.path.exists(csv_path):
        print(f"Fehler: Datei {csv_path} existiert nicht.")
        return
        
    with open(csv_path, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        row_count = 0
        for row in reader:
            row_count += 1
            brand = row.get("brand", "").strip()
            model = row.get("model", "").strip()
            duration = row.get("duration", "").strip()
            
            if not brand or not model or not duration:
                print(f"Zeile {row_count}: Unvollständige Daten. Überspringe...")
                continue
                
            # Dateiname entspricht dem Modellnamen (Bereinigung von unzulässigen Dateizeichen)
            clean_model = "".join([c if (c.isalnum() or c in ("-", "_", ".")) else "_" for c in model])
            filename = f"{clean_model}.png"
            output_path = os.path.join(os.path.dirname(csv_path), filename)
            
            generate_label(brand, model, duration, output_path)

if __name__ == "__main__":
    csv_file = "Meilenstein 4/api_test/test_products.csv"
    process_csv(csv_file)
