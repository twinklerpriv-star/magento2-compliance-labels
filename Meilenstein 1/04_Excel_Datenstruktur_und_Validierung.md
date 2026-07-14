# Excel-Datenstruktur und Eingabehilfen: Lieferantenabfrage 2026

**Datum:** 14.07.2026 | **Version:** 1.1 | **Status:** Aktiv

---

## 1. Spaltenstruktur und Validierungen (Übersicht)

Die Tabelle umfasst nach der Reduktion der Artikelbezeichnung exakt 8 Spalten (A bis H). Für alle Eingabespalten (D bis H) sind hilfreiche Eingabehinweise (Prompts) hinterlegt. Die Spalten F und H besitzen zudem eine restriktive Validierung mit Fehlermeldungen bei Falscheingaben.

| Spalte | Spaltenüberschrift (DE) | Spaltenüberschrift (EN) | Typ | Validierung / Restriktion |
| :---: | :--- | :--- | :---: | :--- |
| **A** | `Lie ID` | `Supplier ID` | Vorausgefüllt | Keine (Gesperrt für Eingabe) |
| **B** | `Lieferant Zuname` | `Supplier Name` | Vorausgefüllt | Keine (Gesperrt für Eingabe) |
| **C** | `ArtikelNr` | `SKU / Article Number` | Vorausgefüllt | Keine (Gesperrt für Eingabe) |
| **D** | `Marke / Brand (Kurzform für Label - z. B. Miele)` | `Brand (short form for label - e.g. Miele)` | Eingabe | Text-Eingabe (Hilfe-Tooltip aktiv) |
| **E** | `Modellbezeichnung (für Label)` | `Model Identifier (for Label)` | Eingabe | Text-Eingabe (Hilfe-Tooltip aktiv) |
| **F** | `Herstellergarantie (in Jahren)` | `Manufacturer Warranty (in years)` | Eingabe | Ganzzahl > 2 (Restriktive Fehlermeldung) |
| **G** | `Link zu Garantiebedingungen (URL beginnend mit https://)` | `Link to Warranty Conditions (URL starting with https://)` | Eingabe | Text-Eingabe (Hilfe-Tooltip aktiv) |
| **H** | `Kostenlos & für gesamte Ware? (Ja/Nein)` | `Warranty is free of charge & covers entire product? (Yes/No)` | Eingabe | Dropdown-Liste: `Ja,Nein` / `Yes,No` (Restriktiv) |

---

## 2. Detaillierte Konfiguration der Eingabehilfen (Tooltips & Fehler)

### Spalte D: Marke / Brand
* **Zweck:** Erfassung des reinen Markennamens zur Platzierung auf dem Label (z. B. "Miele" statt "Miele GmbH").
* **Deutsch (DE):**
  * **Tooltip-Titel:** `Marke / Brand`
  * **Tooltip-Text:** `Tragen Sie bitte den kurzen Markennamen ein, der auf dem Label stehen soll (z. B. „Miele“ statt „Miele GmbH“).`
* **Englisch (EN):**
  * **Tooltip-Titel:** `Brand Name`
  * **Tooltip-Text:** `Please enter the short brand name to be shown on the label (e.g. "Miele" instead of "Miele GmbH").`

### Spalte E: Modellbezeichnung
* **Zweck:** Zuweisung der eindeutigen Modellbezeichnung des Herstellers.
* **Deutsch (DE):**
  * **Tooltip-Titel:** `Modellbezeichnung`
  * **Tooltip-Text:** `Tragen Sie bitte die exakte Modellkennung des Herstellers ein (z. B. „WXD160“).`
* **Englisch (EN):**
  * **Tooltip-Titel:** `Model Identifier`
  * **Tooltip-Text:** `Please enter the exact manufacturer model code (e.g. "WXD160").`

### Spalte F: Herstellergarantie (in Jahren)
* **Zweck:** Angabe der Garantielaufzeit. Nur Ganzzahlen über 2 sind zulässig.
* **Deutsch (DE):**
  * **Tooltip-Titel:** `Herstellergarantie`
  * **Tooltip-Text:** `Tragen Sie hier bitte ausschließlich die nackte Zahl ein (z. B. 3, 5, 10). Schreiben Sie keine Einheiten wie „Jahre“ oder „J“ dazu.`
  * **Fehler-Titel:** `Ungültiger Wert`
  * **Fehler-Text:** `Geben Sie bitte eine ganze Zahl größer als 2 ein (z.B. 3, 5, 10).`
* **Englisch (EN):**
  * **Tooltip-Titel:** `Manufacturer Warranty`
  * **Tooltip-Text:** `Please enter the warranty period in years as a whole number only (e.g., 3, 5, 10). Do not write "years" or "y".`
  * **Fehler-Titel:** `Invalid Value`
  * **Fehler-Text:** `Please enter a whole number greater than 2 (e.g. 3, 5, 10).`

### Spalte G: Link zu Garantiebedingungen
* **Zweck:** Erfassung der URL zu den rechtsverbindlichen Garantiebedingungen (Pflichtbestandteil des Labels).
* **Deutsch (DE):**
  * **Tooltip-Titel:** `Link zu Garantiebedingungen`
  * **Tooltip-Text:** `Bitte tragen Sie hier den direkten Link (URL) zu den Garantiebedingungen auf Ihrer Website ein (z. B. https://www.hersteller.at/garantie). Schreiben Sie keinen Freitext wie „liegt bei“.`
* **Englisch (EN):**
  * **Tooltip-Titel:** `Link to Warranty Conditions`
  * **Tooltip-Text:** `Please enter the direct URL link to the warranty conditions on your website (e.g., https://www.manufacturer.com/warranty). Do not write free text like "in the box".`

### Spalte H: Kostenlose Garantiebestätigung
* **Zweck:** Absicherung, ob die Garantie alle gesetzlichen Label-Kriterien erfüllt (kostenlos & Vollgarantie).
* **Deutsch (DE):**
  * **Dropdown-Optionen:** `Ja,Nein`
  * **Tooltip-Titel:** `Garantie-Bestätigung`
  * **Tooltip-Text:** `Bitte wählen Sie ausschließlich „Ja“ oder „Nein“ aus dem Dropdown-Menü aus.`
  * **Fehler-Titel:** `Ungültige Auswahl`
  * **Fehler-Text:** `Ungültige Auswahl. Bitte wählen Sie Ja oder Nein aus dem Dropdown-Menü.`
* **Englisch (EN):**
  * **Dropdown-Optionen:** `Yes,No`
  * **Tooltip-Titel:** `Warranty Confirmation`
  * **Tooltip-Text:** `Please select "Yes" or "No" from the dropdown menu.`
  * **Fehler-Titel:** `Invalid Selection`
  * **Fehler-Text:** `Invalid selection. Please select Yes or No from the dropdown menu.`

---

## 3. Technische Umsetzung in openpyxl

In Python werden die reinen Informationstext-Tooltips ohne Eingabesperre über ein leeres `DataValidation`-Objekt realisiert:

```python
from openpyxl.worksheet.datavalidation import DataValidation

# Tooltip erstellen (ohne Validierungstyp)
dv_info = DataValidation(allow_blank=True)
dv_info.prompt = "Tooltip-Inhalt"
dv_info.promptTitle = "Tooltip-Titel"
ws.add_data_validation(dv_info)

# Bereich zuweisen (z. B. Spalte D)
dv_info.add("D2:D100")
```
Dies stellt sicher, dass Excel den Hinweiskasten einblendet, dem Lieferanten aber freien Text zur Eingabe überlässt (nötig für Marken, Modellbezeichnungen und URLs).
