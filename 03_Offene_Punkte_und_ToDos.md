# Offene Punkte und To-Dos: Gewährleistungs- und Garantielabel 2026

**Datum:** 10.07.2026 | **Version:** 1.7 | **Status:** Aktiv

---

## 1. Geklärte fachliche Anforderungen (Zur Dokumentation)
*   **Informationsbasis für Lieferanten und Einkauf:**
    Als Grundlage für die Information von Lieferanten und den Einkauf wird die Webinar-Präsentation inklusive des Links zur WKO-Informationsseite mitgeliefert.
    Der offizielle WKO-Info-Link lautet: [WKO - E-Commerce: Widerrufsbutton, Gewährleistung & Garantielabel](https://www.wko.at/handeldigital/e-commerce-widerrufsbutton-gewaehrleistung-garantielabel#heading_aufzeichnung_webinar__last_call_Widerrufsbutton__)
    Dies wurde im Jour Fixe am 23.06.2026 zwischen Thomas Winkler und Elisabeth Platzl vereinbart.
*   **WKO-Richtlinien-Referenzen (Notiz):**
    *   Details zur gesetzlichen Gewährleistung: [WKO - Gewährleistung Details](https://www.wko.at/handel/elektro-einrichtungsfachhandel/informationspflichten-garantien-gewaehrleistung-haendle#heading_gewaehrleistung___was_muss_mitgeteilt_werden_)
    *   Details zur Haltbarkeitsgarantie: [WKO - Haltbarkeitsgarantie Details](https://www.wko.at/handel/elektro-einrichtungsfachhandel/informationspflichten-garantien-gewaehrleistung-haendle#heading_haltbarkeitsgarantie___was_muss_mitgeteilt_werden_)
*   **Garantieabfrage-Dateivorlagen:**
    Für die Erhebung der Herstellergarantien bei Lieferanten wurden zwei benutzerfreundliche Excel-Vorlagen mit Beispielblatt erstellt (deutsch/englisch).
    Die deutsche Vorlage ist unter [Supplier_Warranty_Inquiry_Template_DE.xlsx](file:///C:/Users/thomas.winkler/Desktop/Projekte/Google%20Antigravity/ELEKTROPEPI/GEWAEHRLEISTUNG_GARANTIELABEL/Meilenstein%201/Lieferantenabfrage/Supplier_Warranty_Inquiry_Template_DE.xlsx) abgelegt.
    Die englische Vorlage ist unter [Supplier_Warranty_Inquiry_Template_EN.xlsx](file:///C:/Users/thomas.winkler/Desktop/Projekte/Google%20Antigravity/ELEKTROPEPI/GEWAEHRLEISTUNG_GARANTIELABEL/Meilenstein%201/Lieferantenabfrage/Supplier_Warranty_Inquiry_Template_EN.xlsx) abgelegt.
*   **Lieferantenspezifische Verteilung (Splittung):**
    Die Gesamtartikelliste wurde nach Lieferanten gefiltert und in 104 separate Ordner zerlegt (aktualisiert am 24.06.2026).
    Der Zielpfad ist [Lieferanten](file:///C:/Users/thomas.winkler/Desktop/Projekte/Google%20Antigravity/ELEKTROPEPI/GEWAEHRLEISTUNG_GARANTIELABEL/Meilenstein%202/Lieferanten).
    Jeder Lieferant besitzt einen eigenen Unterordner, in dem die beiden länderspezifischen Abfragedateien abgelegt sind:
    1. Deutsche Version: `<Lieferantenname>_Garantieabfrage.xlsx` (Arbeitsblatt: `Garantiedaten_Erfassung`)
    2. Englische Version: `<Lieferantenname>_Warranty_Inquiry.xlsx` (Arbeitsblatt: `Warranty_Data_Collection`)
    Beide Versionen sind als native Excel-Tabellen im grünen Stil `TableStyleMedium7` formatiert, besitzen eine Datenvalidierung für Ganzzahlen > 2 in Spalte G, eine Dropdown-Auswahl (Ja/Nein bzw. Yes/No) in Spalte I, hilfreiche Tooltips für alle Eingabespalten (E bis I) sowie vordefinierte Spaltenbreiten über alle 9 Spalten.
*   **Rechtliche Argumentation für den Einkauf:**
    Die Leitlinien für das rechtliche Auftreten des Einkaufs gegenüber Lieferanten wurden erarbeitet und in der Datei [Auftreten_gegenueber_Lieferanten_rechtlich.md](file:///C:/Users/thomas.winkler/Desktop/Projekte/Google%20Antigravity/ELEKTROPEPI/GEWAEHRLEISTUNG_GARANTIELABEL/Meilenstein%201/Auftreten_gegenueber_Lieferanten_rechtlich.md) dokumentiert (24.06.2026). Sie klären, dass Lieferanten zur Bereitstellung der Daten verpflichtet sind (nicht aber zur Zusendung fertiger Bilddateien), und definieren die rechtliche Position des Einkaufs bei Verweigerung.
*   **Excel-Spezifikationsdokument:**
    Das Spezifikationsdokument für die Excel-Dateien, Spalten, Tooltips und Validierungen wurde unter [04_Excel_Datenstruktur_und_Validierung.md](file:///C:/Users/thomas.winkler/Desktop/Projekte/Google%20Antigravity/ELEKTROPEPI/GEWAEHRLEISTUNG_GARANTIELABEL/Meilenstein%201/04_Excel_Datenstruktur_und_Validierung.md) erstellt.

---

## 2. Offene To-Dos (Agiles Backlog)

### ▶ Aktueller Fokus: Warten auf Lieferanten-Rücklauf (Gestartet 06.08.2026)
*   [x] **Finale Spaltenabstimmung mit Helmut Nobis:**
    Besprechung der [Spaltenanalyse_Lieferantenabfrage.xlsx](file:///C:/Users/thomas.winkler/Desktop/Projekte/Google%20Antigravity/ELEKTROPEPI/GEWAEHRLEISTUNG_GARANTIELABEL/Meilenstein%201/Lieferantenabfrage/Spaltenanalyse_Lieferantenabfrage.xlsx) zur Festlegung der abzufragenden Spalten. (Erfolgreich auf 7 Spalten reduziert).
*   [x] **Lieferantenauswahl durch Einkauf:**
    Helmut Nobis hat eine gezielte Auswahl von 6 Lieferanten getroffen (Thermotec, Shelly, EcoFlow, Ezviz, Avidsen, Bodo Ehmann).
*   [x] **Umstrukturierung der Excel-Vorlagen & Re-Generierung:**
    Überarbeitung und Generierung des neuen 7-spaltigen Layouts inklusive echtem EcoFlow-Beispielblatt und Reparatur der Hyperlinks für alle Lieferanten.
*   [x] **Start der Aussendung (06.08.2026):**
    Aussendung der Anschreiben und Excel-Tabellen an die 6 ausgewählten Lieferanten durch Thomas Winkler.
*   [ ] **Überwachung des Rücklaufs:**
    Erfassung und Prüfung der eingehenden Lieferantendaten (Excel-Dateien & PDF/PNG-Garantielabels). Deadline für Lieferanten: **[ca. Anfang September 2026]**.

### ⏳ Zukünftige Etappen (Zur Orientierung - Aktuell on hold)
*   [ ] **Evaluation des Dienstleisters garan-label.com:**
    Vergleich der Integrations- und Generierungsoptionen (Massen-Generierung via CSV-Upload für den Magento-Import und m.PIM-Upload vs. API-Schnittstelle) als kosteneffiziente Alternative zur rein internen Entwicklung eines eigenen Magento-Generators.
*   [ ] **Spezifikation der Magento-Datenstruktur:**
    Definition der notwendigen Produkt-Attribute (Garantiejahre, Hersteller, Modellkennung, PDF-Link) im Magento-Backend.
*   [ ] **Datenpflege & Import-Vorbereitung:**
    Strukturierte Erfassung der von Lieferanten übermittelten Garantiedaten zur Vorbereitung des CSV-Imports.
*   [ ] **Übergabe des Moduls an weboffice:**
    Bereitstellung des ZIP-Archivs für das Testsystem und Freigabe zur Qualitätssicherung (UAT).

---

## 3. Erledigt / Archiv
*   [x] **Schreiben an den Einkauf entwerfen:**
    Der E-Mail-Entwurf an Helmut Nobis wurde unter [01_Email_Entwurf_Heli_Nobis_Garantieabfrage.md](file:///C:/Users/thomas.winkler/Desktop/Projekte/Google%20Antigravity/ELEKTROPEPI/GEWAEHRLEISTUNG_GARANTIELABEL/Meilenstein%201/Korrespondenz/01_Email_Entwurf_Heli_Nobis_Garantieabfrage.md) abgelegt (23.06.2026).
*   [x] **Lieferanten-Abklärung durch den Einkauf initiieren (06.08.2026):**
    Die erste Welle der Lieferantenabfrage wurde gestartet (6 Lieferanten kontaktiert).
*   [ ] **Klärung der Blisterverpackungs-Logik:**
    Im Zuge der Lieferanten-Abfrage ist zu klären, ob SBS das Label bei Blisterverpackungen selbst aufbringen muss (Warten auf Rückmeldungen der Lieferanten).

