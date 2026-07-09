# Offene Punkte und To-Dos: Gewährleistungs- und Garantielabel 2026

**Datum:** 24.06.2026 | **Version:** 1.6 | **Status:** Aktiv

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
    Für die Erhebung der Herstellergarantien bei Lieferanten wurden zwei zweisprachige Excel-Vorlagen erstellt.
    Die deutsche Vorlage ist unter [garantieabfrage_lieferanten_de.xlsx](file:///C:/Users/thomas.winkler/Desktop/Projekte/Google%20Antigravity/ELEKTROPEPI/GEWAEHRLEISTUNG_GARANTIELABEL/garantieabfrage_lieferanten_de.xlsx) abgelegt.
    Die englische Vorlage ist unter [warranty_inquiry_suppliers_en.xlsx](file:///C:/Users/thomas.winkler/Desktop/Projekte/Google%20Antigravity/ELEKTROPEPI/GEWAEHRLEISTUNG_GARANTIELABEL/warranty_inquiry_suppliers_en.xlsx) abgelegt.
*   **Lieferantenspezifische Verteilung (Splittung):**
    Die Gesamtartikelliste wurde nach Lieferanten gefiltert und in 104 separate Ordner zerlegt (aktualisiert am 24.06.2026).
    Der Zielpfad ist [Lieferanten](file:///C:/Users/thomas.winkler/Desktop/Projekte/Google%20Antigravity/ELEKTROPEPI/GEWAEHRLEISTUNG_GARANTIELABEL/Lieferanten).
    Jeder Lieferant besitzt einen eigenen Unterordner, in dem die beiden länderspezifischen Abfragedateien abgelegt sind:
    1. Deutsche Version: `<Lieferantenname>_Garantieabfrage.xlsx` (Arbeitsblatt: `Garantiedaten_Erfassung`)
    2. Englische Version: `<Lieferantenname>_Warranty_Inquiry.xlsx` (Arbeitsblatt: `Warranty_Data_Collection`)
    Beide Versionen sind als native Excel-Tabellen im grünen Stil `TableStyleMedium7` formatiert, besitzen eine Datenvalidierung für Ganzzahlen > 2 in Spalte G, eine Dropdown-Auswahl (Ja/Nein bzw. Yes/No) in Spalte I, hilfreiche Tooltips für alle Eingabespalten (E bis I) sowie vordefinierte Spaltenbreiten über alle 9 Spalten.
*   **Rechtliche Argumentation für den Einkauf:**
    Die Leitlinien für das rechtliche Auftreten des Einkaufs gegenüber Lieferanten wurden erarbeitet und in der Datei [Auftreten_gegenueber_Lieferanten_rechtlich.md](file:///C:/Users/thomas.winkler/Desktop/Projekte/Google%20Antigravity/ELEKTROPEPI/GEWAEHRLEISTUNG_GARANTIELABEL/Auftreten_gegenueber_Lieferanten_rechtlich.md) dokumentiert (24.06.2026). Sie klären, dass Lieferanten zur Bereitstellung der Daten verpflichtet sind (nicht aber zur Zusendung fertiger Bilddateien), und definieren die rechtliche Position des Einkaufs bei Verweigerung.
*   **Excel-Spezifikationsdokument:**
    Das Spezifikationsdokument für die Excel-Dateien, Spalten, Tooltips und Validierungen wurde unter [04_Excel_Datenstruktur_und_Validierung.md](file:///C:/Users/thomas.winkler/Desktop/Projekte/Google%20Antigravity/ELEKTROPEPI/GEWAEHRLEISTUNG_GARANTIELABEL/04_Excel_Datenstruktur_und_Validierung.md) erstellt.

---

## 2. Offene To-Dos (Agiles Backlog)

### ▶ Aktueller Fokus: Abstimmung mit Einkauf & Lieferanten
*   [x] **Besprechung der Markant/Globus-E-Mail im Jour Fixe (07.07.2026):**
    Ergebnisse: Vertagt / Fokus liegt zunächst auf der Strukturierung der Lieferanten-Garantieabfrage.
*   [ ] **Finale Spaltenabstimmung mit Helmut Nobis:**
    Besprechung der [Spaltenanalyse_Lieferantenabfrage.xlsx](file:///C:/Users/thomas.winkler/Desktop/Projekte/Google%20Antigravity/ELEKTROPEPI/GEWAEHRLEISTUNG_GARANTIELABEL/Spaltenanalyse_Lieferantenabfrage.xlsx) zur Festlegung der abzufragenden Spalten. **Termin: Montag, 13.07.2026 um 10:00 Uhr** (im Büro von Thomas Winkler).

*   [ ] **Lieferantenauswahl durch Einkauf:**
    Helmut Nobis um Erstellung einer Auswahl jener Lieferanten bitten, die tatsächlich angeschrieben werden sollen.
*   [ ] **Umstrukturierung der Excel-Vorlagen (nach Freigabe):**
    Überarbeitung der 104 Lieferantenordner: Umstellung auf leere Listen und Hinzufügen des Tabellenblatts „Beispiel“ (Spalten als Zeilen in Spalte A, Werte in Spalte B).
*   *Warten auf Rücklauf der Lieferanten-Excel-Dateien (Zusendung durch Thomas Winkler vorgeschlagen).*

### ⏳ Zukünftige Etappen (Zur Orientierung - Aktuell on hold)
*   [ ] **Spezifikation der Magento-Datenstruktur:**
    Definition der notwendigen Produkt-Attribute (Garantiejahre, Hersteller, Modellkennung) im Magento-Backend.
*   [ ] **Datenpflege & Import-Vorbereitung:**
    Strukturierte Erfassung der von Lieferanten übermittelten Garantiedaten zur Vorbereitung des CSV-Imports.
*   [ ] **Übergabe des Moduls an weboffice:**
    Bereitstellung des ZIP-Archivs für das Testsystem und Freigabe zur Qualitätssicherung (UAT).

---

## 3. Erledigt / Warten auf externe Partner (Archiv)
*   [x] **Schreiben an den Einkauf entwerfen:**
    Der E-Mail-Entwurf an Helmut Nobis wurde erstellt und unter [01_Email_Entwurf_Heli_Nobis_Garantieabfrage.md](file:///C:/Users/thomas.winkler/Desktop/Projekte/Google%20Antigravity/ELEKTROPEPI/GEWAEHRLEISTUNG_GARANTIELABEL/Korrespondenz/01_Email_Entwurf_Heli_Nobis_Garantieabfrage.md) abgelegt (23.06.2026).
*   [ ] **Lieferanten-Abklärung durch den Einkauf initiieren:**
    Der Einkauf soll die Lieferanten kontaktieren, um abzuklären, welche Artikel konkret von der Garantiekennzeichnungspflicht betroffen sind (Warten auf Rücklauf von Einkauf/Lieferanten, E-Mail gesendet am 23.06.2026).
*   [ ] **Klärung der Blisterverpackungs-Logik:**
    Im Zuge der Lieferanten-Abklärung ist zu klären, ob SBS das Label bei Blisterverpackungen selbst aufbringen muss (Warten auf Rücklauf von Einkauf/Lieferanten, E-Mail gesendet am 23.06.2026).
