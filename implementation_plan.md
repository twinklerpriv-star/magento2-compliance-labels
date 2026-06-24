# Implementierungsplan: Englische Lieferanten-Garantieabfrage-Dateien

Dieses Projekt erstellt die englischsprachigen Excel-Abfragedateien für alle 104 Lieferanten.
Die Dateien werden in den bereits bestehenden, jeweiligen Lieferanten-Unterordnern abgelegt.

---

## Proposed Changes

### A. Python-Skript zur Generierung

#### [NEW] [split_articles_by_supplier_en.py](file:///C:/Users/thomas.winkler/Desktop/Projekte/Google%20Antigravity/ELEKTROPEPI/GEWAEHRLEISTUNG_GARANTIELABEL/scratch/split_articles_by_supplier_en.py)
* Das Skript liest das Datenblatt `Garantiedaten_Erfassung` aus der Quell-Datei `alle gelisteten Artikel - Stand 24.06.2026.xlsx`.
* Es filtert die Artikel nach Lieferant und erstellt pro Lieferant die englischsprachige Datei.
* **Zielpfad:** `C:\Users\thomas.winkler\Desktop\Projekte\Google Antigravity\ELEKTROPEPI\GEWAEHRLEISTUNG_GARANTIELABEL\Lieferanten\<Lieferantenname>\<Lieferantenname>_Warranty_Inquiry.xlsx`

### B. Tabellen-Spezifikationen (EN)
1. **Tabellenblatt-Name:**  
   `Warranty_Data_Collection`
2. **Spaltenbezeichnungen:**
   1. `Supplier ID` (Spalte A)
   2. `Supplier Name` (Spalte B)
   3. `SKU / Article Number` (Spalte C)
   4. `Product Description` (Spalte D)
   5. `Manufacturer Warranty (in years)` (Spalte E)
   6. `Notes / Link to Warranty Conditions` (Spalte F)
3. **Tabellen-Styling:**  
   * Formatierung als native Excel-Tabelle mit dem Design-Stil `TableStyleMedium14` (grünes Design passend zu den DE-Dateien).
   * Gitterlinien werden explizit aktiviert (`showGridLines = True`).
   * Schriftart: Segoe UI (Größe 11).
4. **Datenvalidierung (Column E):**  
   * Überprüfung auf Ganzzahlen > 2.
   * **Englische Textausgaben:**
     * Prompt Title: `Manufacturer Warranty`
     * Prompt Text: `Please enter the manufacturer warranty in years as a whole number (must be > 2).`
     * Error Title: `Invalid Value`
     * Error Text: `Please enter a whole number greater than 2 (e.g. 3, 5, 10).`
5. **Layout-Formatierung:**  
   * Spalten E (Breite 30) und F (Breite 45) erhalten vergrößerte Standardbreiten für einfache Eingabe.
   * Ausrichtung: Zentriert für Spalte E, linksbündig für Textspalten.

---

## Verification Plan

### Automated Tests
- Programmatische Verifizierung der erstellten Excel-Dateien über ein Testskript auf:
  * Existenz im gleichen Unterordner des Lieferanten.
  * Korrektheit des Tabellenblattnamens (`Warranty_Data_Collection`).
  * Vorhandensein der 6 englischen Spaltenbezeichnungen.
  * Integrierte Datenüberprüfung und korrektes Tabellendesign.

### Manual Verification
- Stichprobenartige manuelle Sichtprüfung von 2-3 englischen Excel-Dateien in Microsoft Excel auf Layout, Gitterlinien und Datenvalidierungsverhalten.
