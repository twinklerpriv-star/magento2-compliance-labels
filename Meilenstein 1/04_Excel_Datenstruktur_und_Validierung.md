# Excel-Datenstruktur und Eingabehilfen: Lieferantenabfrage 2026

**Datum:** 14.07.2026 | **Version:** 1.2 | **Status:** Aktiv

---

## 1. Spaltenstruktur und Validierungen (Übersicht)

Die Tabelle umfasst für das Lieferanten-Template exakt 7 Spalten (A bis G), die identisch mit den 7 Spalten der Spaltenanalyse sind. Für alle Eingabespalten (C bis G) sind hilfreiche Eingabehinweise (Prompts) hinterlegt. Die Spalten E und G besitzen zudem eine restriktive Validierung mit Fehlermeldungen bei Falscheingaben.

| Spalte | Spaltenüberschrift (DE) | Spaltenüberschrift (EN) | Typ | Validierung / Restriktion |
| :---: | :--- | :--- | :---: | :--- |
| **A** | `EAN / GTIN (Barcode)` | `EAN / GTIN (Barcode)` | Eingabe | Eindeutige Artikelzuordnung |
| **B** | `Lieferanten-Artikelnummer (Herstellernummer)` | `Supplier SKU / Article Number` | Eingabe | Eindeutige Identifikation Lieferant |
| **C** | `Marke / Brand (Kurzform für Label - z. B. Miele)` | `Brand (short form for label - e.g. Miele)` | Eingabe | Text-Eingabe (Hilfe-Tooltip aktiv) |
| **D** | `Modellbezeichnung (für Label)` | `Model Identifier (for Label)` | Eingabe | Text-Eingabe (Hilfe-Tooltip aktiv) |
| **E** | `Herstellergarantie (in Jahren)` | `Manufacturer Warranty (in years)` | Eingabe | Ganzzahl > 2 (Restriktive Fehlermeldung) |
| **F** | `Link zu Garantiebedingungen (URL mit https://)` | `Link to Warranty Conditions (URL starting with https://)` | Eingabe | Text-Eingabe (Hilfe-Tooltip aktiv) |
| **G** | `Kostenlos & für gesamte Ware? (Ja/Nein)` | `Warranty is free of charge & covers entire product? (Yes/No)` | Eingabe | Dropdown-Liste: `Ja,Nein` / `Yes,No` (Restriktiv) |

---

## 2. Detaillierte Konfiguration der Eingabehilfen (Tooltips & Fehler)

### Spalte C: Marke / Brand
* **Zweck:** Erfassung des reinen Markennamens zur Platzierung auf dem Label (z. B. "Miele" statt "Miele GmbH").
* **Deutsch (DE):**
  * **Tooltip-Titel:** `Marke / Brand`
  * **Tooltip-Text:** `Tragen Sie bitte den kurzen Markennamen ein, der auf dem Label stehen soll (z. B. „Miele“ statt „Miele GmbH“).`
* **Englisch (EN):**
  * **Tooltip-Titel:** `Brand Name`
  * **Tooltip-Text:** `Please enter the short brand name to be shown on the label (e.g. "Miele" instead of "Miele GmbH").`

### Spalte D: Modellbezeichnung
* **Zweck:** Zuweisung der eindeutigen Modellbezeichnung des Herstellers.
* **Deutsch (DE):**
  * **Tooltip-Titel:** `Modellbezeichnung`
  * **Tooltip-Text:** `Tragen Sie bitte die exakte Modellkennung des Herstellers ein (z. B. „WXD160“).`
* **Englisch (EN):**
  * **Tooltip-Titel:** `Model Identifier`
  * **Tooltip-Text:** `Please enter the exact manufacturer model code (e.g. "WXD160").`

### Spalte E: Herstellergarantie (in Jahren)
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

### Spalte F: Link zu Garantiebedingungen
* **Zweck:** Erfassung der URL zu den rechtsverbindlichen Garantiebedingungen (Pflichtbestandteil des Labels).
* **Deutsch (DE):**
  * **Tooltip-Titel:** `Link zu Garantiebedingungen`
  * **Tooltip-Text:** `Bitte tragen Sie hier den direkten Link (URL) zu den Garantiebedingungen auf Ihrer Website ein (z. B. https://www.hersteller.at/garantie). Schreiben Sie keinen Freitext wie „liegt bei“.`
* **Englisch (EN):**
  * **Tooltip-Titel:** `Link to Warranty Conditions`
  * **Tooltip-Text:** `Please enter the direct URL link to the warranty conditions on your website (e.g., https://www.manufacturer.com/warranty). Do not write free text like "in the box".`

### Spalte G: Kostenlose Garantiebestätigung
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

# Bereich zuweisen (z. B. Spalte C)
dv_info.add("C2:C1000")
```
Dies stellt sicher, dass Excel den Hinweiskasten einblendet, dem Lieferanten aber freien Text zur Eingabe überlässt (nötig für Marken, Modellbezeichnungen und URLs).
