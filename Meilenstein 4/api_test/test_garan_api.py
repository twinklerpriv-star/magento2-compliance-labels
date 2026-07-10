import urllib.request
import urllib.parse
import json
import os

api_key = "a0eb1419466cef8904285c21a094a99e63708fd59d3f101d8fa1205d275b2396"
endpoint = "https://api.garan-label.com/api.php"

def test_api(duration, filename):
    payload = {
        "brand": "Adidas",
        "model": "abc-123456",
        "duration": str(duration),
        "sandbox": "1"  # Test-Modus mit Wasserzeichen
    }
    
    print(f"\n--- Teste API mit Garantiedauer: {duration} Jahre ---")
    data = urllib.parse.urlencode(payload).encode("utf-8")
    req = urllib.request.Request(endpoint, data=data, headers={"X-API-Key": api_key})
    
    try:
        with urllib.request.urlopen(req) as response:
            res_data = json.loads(response.read().decode("utf-8"))
            if res_data.get("success"):
                url = res_data.get("url")
                print(f"API-Aufruf erfolgreich!")
                print(f"Image-URL: {url}")
                # Herunterladen und Speichern des Bildes
                urllib.request.urlretrieve(url, filename)
                print(f"Bild erfolgreich gespeichert unter: {filename}")
                return True
            else:
                print(f"API-Fehlermeldung: {res_data.get('error')}")
                return False
    except Exception as e:
        print(f"Verbindungsfehler zur API: {e}")
        return False

if __name__ == "__main__":
    # Test 1: Gültige Garantiedauer von 3 Jahren (sollte funktionieren)
    test_api(3, "Meilenstein 4/api_test/label_3_jahre.png")
    
    # Test 2: Garantiedauer von 2 Jahren (gesetzliches Minimum - Grenzfallprüfung)
    test_api(2, "Meilenstein 4/api_test/label_2_jahre.png")
