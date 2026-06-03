**Datum:** 2026-06-03  
**Version:** 1.1  
**Status:** In Arbeit (User-Review erforderlich)  

# Implementierungsplan: Magento 2-Modul „Sbs_ComplianceLabels“

Dieses Projekt implementiert die ab dem **27. September 2026** in Kraft tretenden EU-Verbraucherschutzrichtlinien (VerbRÄG 2026 / EU 2024/825) zur harmonisierten Kennzeichnung von gesetzlichen Gewährleistungen und freiwilligen Herstellergarantien im Magento 2 Webshop von **Elektropepi**.

---

## 1. Voraussetzungen & Klärungspunkte

### Magento-Attribute
Das Modul prüft dynamisch, ob für ein Produkt eine Herstellergarantie von über 2 Jahren vorliegt. Dafür müssen in Magento folgende Attribute existieren und gepflegt sein:
1. Ein Attribut für die Garantie-Dauer in Jahren (z. B. `manufacturer_warranty_years` vom Typ Text oder Auswahlliste).
2. Ein Attribut für die Marke/Hersteller (z. B. `manufacturer` oder `brand`).

**Aufgabe:** Thomas Winkler prüft, ob diese Attribute bereits in Magento vorhanden und gepflegt sind oder neu angelegt werden müssen.

### Software-Updates & Reparierbarkeit
Es ist zu klären, ob die Angaben zu Software-Updates und Reparierbarkeits-Scores (siehe WKO-Richtlinien) ebenfalls über dieses Modul dynamisch ausgespielt werden sollen, oder ob dies vorerst manuell über die Produktbeschreibungen erfolgt.

---

## 2. Detaillierte UI-Vorgaben aus den Originalquellen

Basierend auf den vom User bereitgestellten Quellgrafiken (WKO-Poster & EU-Label-Entwürfe) werden folgende UI-Elemente exakt umgesetzt:

### A. Gesetzliche Gewährleistung (Harmonised Notice Poster)
Das Poster wird als eigenständiger, fest integrierter Inhaltsblock auf der Produktdetailseite gerenert und darf nicht versteckt oder einklappbar sein.
* **Header:** Blauer Hintergrund (`#003399`), weiße, fette Aufschrift „GESETZLICHE GEWÄHRLEISTUNG“.
* **EU-Wappen:** Ein blaues Schild mit weißer Outline, darin ein weißes stilisiertes „G“ und 12 gelbe Sterne im Kreis.
* **Layout:**
  * **Linke Spalte:** 
    * Eine Box mit blauem Rahmen und blauem Text: „Mindestens zwei Jahre gesetzliche Gewährleistung der Vertragsmäßigkeit für Waren, die in der Europäischen Union verkauft werden.“
    * Darunter die Aufklärungstexte für Verbraucher bezüglich Mängel und Fristen (siehe Screenshot 1).
    * Darunter die Verkäuferpflichten (kostenlose Nachbesserung/Ersatzlieferung, Preisminderung/Erstattung).
  * **Rechte Spalte:** 
    * Informationen über länderspezifische Gewährleistungsfristen und gebrauchte Waren.
    * Ein funktionstüchtiger, scannbarer QR-Code, der auf `https://europa.eu/youreurope/garantien` verlinkt.
    * Die Textunterschrift `europa.eu/youreurope/garantien`.
  * **Bottom-Bereich:**
    * „Was ist zu tun, wenn Sie vertragswidrige Waren erhalten?“ mit den Schritten 1 (Melden) und 2 (Kaufnachweis vorlegen).
    * Der Hinweis auf freiwillige gewerbliche Garantien („GARAN-Kennzeichnung“).

### B. Freiwillige Herstellergarantie (Harmonised Durability Label „GARAN“)
Dieses Label wird dynamisch geladen (wenn Garantie > 2 Jahre) und ist einklappbar.
* **Außenhülle:** Schwarzer Rahmen mit abgerundeten Ecken.
* **Kopfbereich:**
  * Schriftzug **GARAN** (schwarz, fett) mit dem Häkchen-Icon (Häkchen im abgerundeten Quadrat).
  * Rechtsbündig das EU-Wappenschild (Blau/Weiß/Gelb).
* **Datenzeilen (mit durchgehender schwarzer Unterlinie):**
  * Spalte links: „Brand/Trademark“ -> Dynamischer Markenname (z. B. Siemens) in Schriftart **Inter**.
  * Spalte rechts: „Model identifier“ -> Dynamische Modellnummer/SKU (z. B. WM14) in Schriftart **Inter**.
* **Mittelbereich:**
  * Links: Die Anzahl der Garantie-Jahre (z. B. „3“ oder „5“) in sehr großen Ziffern, daneben das Kalender-Icon mit der Aufschrift „365“.
  * Rechts: Ein scannbarer QR-Code, der auf die EU-Informationsseite für gewerbliche Garantien verlinkt: `https://europa.eu/youreurope/commercial-guarantee-durability/index.htm`.
* **Fußzeilen (Fußnoten-Block):**
  * Eine Trennlinie.
  * Der standardisierte mehrsprachige Fußnoten-String in Schriftgröße ca. 7.5px (BG, CS, DA, DE, EL, EN, ES, ET, FI, FR, GA, HR, HU, IT, LT, LV, MT, NL, PL, PT, RO, SK, SL, SV).

---

## 3. Vorgeschlagene Projektstruktur

Die Entwicklung erfolgt als eigenständiges Magento 2-Modul `Sbs_ComplianceLabels` im Ordner `MODUL_QUELLCODE`.

```text
GEWAEHRLEISTUNG_GARANTIELABEL/
├── 01_WKO_Richtlinien_Gewaehrleistung_Garantielabel_2026.md
├── implementation_plan.md
├── task.md
├── tests.md
└── MODUL_QUELLCODE/
    ├── registration.php
    ├── etc/
    │   └── module.xml
    ├── Block/
    │   └── Product/
    │       └── View/
    │           └── Labels.php
    └── view/
        └── frontend/
            ├── layout/
            │   └── catalog_product_view.xml
            ├── templates/
            │   └── product/
            │       └── view/
            │           └── compliance_labels.phtml
            └── web/
                ├── css/
                │   └── compliance-labels.css
                └── js/
                    └── compliance-labels.js
```

---

## 4. Modul-Dateien im Detail

### a) [registration.php](file:///C:/Users/thomas.winkler/Desktop/Projekte/Google%20Antigravity/ELEKTROPEPI/GEWAEHRLEISTUNG_GARANTIELABEL/MODUL_QUELLCODE/registration.php)
Registriert das Modul `Sbs_ComplianceLabels` in Magento.

### b) [module.xml](file:///C:/Users/thomas.winkler/Desktop/Projekte/Google%20Antigravity/ELEKTROPEPI/GEWAEHRLEISTUNG_GARANTIELABEL/MODUL_QUELLCODE/etc/module.xml)
Definiert das Modul und seine Abhängigkeiten (z. B. `Magento_Catalog`).

### c) [Labels.php](file:///C:/Users/thomas.winkler/Desktop/Projekte/Google%20Antigravity/ELEKTROPEPI/GEWAEHRLEISTUNG_GARANTIELABEL/MODUL_QUELLCODE/Block/Product/View/Labels.php)
Block-Klasse, die das aktuelle Produkt lädt und Hilfsmethoden zur Abfrage der Garantie-Attribute für das Template bereitstellt.

### d) [catalog_product_view.xml](file:///C:/Users/thomas.winkler/Desktop/Projekte/Google%20Antigravity/ELEKTROPEPI/GEWAEHRLEISTUNG_GARANTIELABEL/MODUL_QUELLCODE/view/frontend/layout/catalog_product_view.xml)
Layout-XML, das unser Template `compliance_labels.phtml` in den Inhaltsbereich der Produktdetailseite (unterhalb der Kurzbeschreibung / Preisbox) injiziert.

### e) [compliance_labels.phtml](file:///C:/Users/thomas.winkler/Desktop/Projekte/Google%20Antigravity/ELEKTROPEPI/GEWAEHRLEISTUNG_GARANTIELABEL/MODUL_QUELLCODE/view/frontend/templates/product/view/compliance_labels.phtml)
HTML/PHP-Template, das:
* Die Gewährleistungsmitteilung (Notice) rendert (statisch, farbig, mit scannbaren QR-Codes als inline-SVGs und EU-Wappen).
* Prüft, ob Herstellergarantie-Bedingungen vorliegen, und das „Garan“-Label mit den dynamischen Werten (Marke, Modell, Jahre) rendert.
* Enthält inline-SVGs für das EU-Schild, das Kalendersymbol, das Häkchen und die QR-Codes.

### f) [compliance-labels.css](file:///C:/Users/thomas.winkler/Desktop/Projekte/Google%20Antigravity/ELEKTROPEPI/GEWAEHRLEISTUNG_GARANTIELABEL/MODUL_QUELLCODE/view/frontend/web/css/compliance-labels.css)
CSS-Datei zur Formatierung der Labels nach den exakten EU-Farbvorgaben (Blau: `#003399`, Gelb: `#FFED00`) und Einbindung der Schriftart „Inter“ für alle dynamischen Felder. Sorgt für Responsive Grid Layout.

### g) [compliance-labels.js](file:///C:/Users/thomas.winkler/Desktop/Projekte/Google%20Antigravity/ELEKTROPEPI/GEWAEHRLEISTUNG_GARANTIELABEL/MODUL_QUELLCODE/view/frontend/web/js/compliance-labels.js)
JS-Datei für das Ein- und Ausblenden des Garantielabels bei Klick oder Mouse-over (Verschachtelungs-Logik).

---

## 5. Verifizierungsplan

### Testumgebung
Die Verifizierung erfolgt nach dem Deployment der Dateien auf dem Testsystem von weboffice.

### Manuelle Tests (QS)
1. **Prüfung Gewährleistungs-Notice:** Erscheint die farbige Grafik permanent auf allen Produktdetailseiten? Ist sie ohne Klick lesbar?
2. **Prüfung Garantielabel-Dynamik:**
   * Testartikel A (Garantie = 0): Label darf nicht erscheinen.
   * Testartikel B (Garantie = 3 Jahre, Marke = Siemens, Modell = WM14): Label muss gerendert werden und die korrekten dynamischen Texte enthalten.
3. **Interaktions-Test:** Klappt das Garantielabel bei Klick oder Touch auf mobilen Geräten auf und wird in Originalgröße angezeigt?
4. **Validierung der Farbwerte & Schrift:** Visueller Abgleich mit den HEX-Werten und Verifizierung, dass editierte Felder in „Inter“ gerendert werden.
5. **Scannbarkeit:** Überprüfung der beiden QR-Codes mit einem Smartphone auf korrekte Verlinkung.

