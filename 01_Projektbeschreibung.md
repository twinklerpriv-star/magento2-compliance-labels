# Projektbeschreibung: Gewährleistungs- und Garantielabel 2026 (EU-Richtlinie & VerbRÄG)

**Datum:** 10.07.2026 | **Version:** 1.1 | **Status:** In Bearbeitung

---

## 1. Projekt-Hintergrund

Mit Inkrafttreten des Verbraucherrechte-Änderungsgesetzes (VerbRÄG 2026) in Österreich und der EU-Durchführungsverordnung 2025/1960 zum **27. September 2026** gelten neue, strenge Informationspflichten für den Handel. Wenn für ein Produkt eine kostenlose Hersteller-Haltbarkeitsgarantie von mehr als 2 Jahren für die gesamte Ware gewährt wird, muss der Händler dieses Produkt mit dem grünen EU-Garantielabel („GARAN“) auszeichnen.

Als Großhändler und Webshop-Betreiber (SBS Austria) müssen wir diese Anforderungen auf zwei unterschiedlichen Kanälen umsetzen:
1. Für unseren eigenen B2C-Webshop **Elektropepi** (wo wir die Pflichten des Händlers erfüllen müssen).
2. Für unsere **B2B-Handelspartner** (wie Globus Fachmärkte, Hornbach AT, etc.), die diese Daten und fertige Labels von uns als Lieferant verlangen, um sie in ihren Online-Shops und physischen Baumärkten/Filialen zu integrieren.

---

## 2. Projektziele

* **Rechtskonforme Ausweisung (B2C & B2B):**
  Gesetzeskonforme Bereitstellung des statischen Gewährleistungshinweises und der dynamischen Haltbarkeitsgarantie-Labels ab dem Stichtag 27.09.2026.
* **Lieferanten-Erhebung:**
  Systematische Einholung aller relevanten Garantielaufzeiten, Garantiebedingungen (Links/PDFs) und Kriterienbestätigungen von unseren Herstellern.
* **Technische Magento-Integration (Elektropepi):**
  Automatisierte Verarbeitung der erhobenen Lieferantendaten im Backend und dynamische Generierung/Darstellung des Labels im Frontend.
* **B2B-Daten- und Dokumentenbereitstellung:**
  Befüllung der Garantie-Attribute in Partnersystemen (z. B. m.PIM für Globus) und Bereitstellung von Bild-/PDF-Labels für den Omnichannel-Verkauf (Online-Shops und Filialdruck).

---

## 3. Bereitstellungs- und Integrationskanäle (Begriffsdefinitionen)

Für die Verteilung und Anzeige des Garantielabels wurden zwei wesentliche Kanäle definiert:

*   **Kanal A -- B2C-Online-Frontend (Magento Elektropepi):**
    Dynamische Darstellung des Labels direkt beim Produkt im Webshop.
    *   *Collapsed State:* Geschachteltes Format (XX GARAN) neben dem Produktbild.
    *   *Expanded State:* Vollständiges Label öffnet sich per Mouse-over, Klick oder Touchgeste.
    *   *Bedingungs-Verlinkung:* Direkte Verlinkung der detaillierten Hersteller-Garantiebedingungen am Produkt.
*   **Kanal B -- B2B-Datenpool-Bereitstellung (m.PIM / GDSN / Markant):**
    Übertragung der Daten und Dokumente an unsere B2B-Kunden.
    *   *Stammdaten:* Eintrag der Garantiedauer in Monaten in den entsprechenden m.PIM-Feldern.
    *   *Dokumentenupload:* Upload der schriftlichen Garantiebedingungen als PDF (Klassifizierung `WARRANTY_INFORMATION`).
    *   *Grafik-Upload (Globus-Sonderspezifikation):* Bereitstellung von ausgefüllten PNG/PDF-Labels (z. B. generiert über *garan-label.com*), da Globus diese für den Filialdruck und die starre Shop-Anzeige benötigt.

---

## 4. Projekt-Scope & Randbedingungen

* **In-Scope:**
  * Alle Artikel unseres Sortiments, bei denen der Hersteller eine **kostenlose gewerbliche Haltbarkeitsgarantie** für das **gesamte Produkt** gewährt, die **länger als 2 Jahre** ist.
  * Alle Kunden (stationäre Einzelhändler, Onlineshops und Großhändler), die diese Artikel von uns beziehen und die Daten für ihren Verkauf (online/offline) benötigen.
* **Out-of-Scope:**
  * Artikel mit gesetzlicher Standardgewährleistung (bis 2 Jahre).
  * Kostenpflichtige Zusatzgarantien oder reine Teil-/Komponentengarantien (z. B. Garantie nur auf den Kompressor). Für diese darf das grüne EU-Label nicht verwendet werden.
* **Geografischer Raum:**
  Österreich, Deutschland und der gesamte EU-Raum.

---

## 5. Projektdaten & Quellen

* **Datenbasis Lieferantenabfrage:**
  Die Excel-Vorlagen [Supplier_Warranty_Inquiry_Template_DE.xlsx](file:///C:/Users/thomas.winkler/Desktop/Projekte/Google%20Antigravity/ELEKTROPEPI/GEWAEHRLEISTUNG_GARANTIELABEL/Meilenstein%201/Lieferantenabfrage/Supplier_Warranty_Inquiry_Template_DE.xlsx) (deutsch) und [Supplier_Warranty_Inquiry_Template_EN.xlsx](file:///C:/Users/thomas.winkler/Desktop/Projekte/Google%20Antigravity/ELEKTROPEPI/GEWAEHRLEISTUNG_GARANTIELABEL/Meilenstein%201/Lieferantenabfrage/Supplier_Warranty_Inquiry_Template_EN.xlsx) (englisch) dienen als Muster für die Abfrage. Sie enthalten ein ausgefülltes Beispielblatt und die leere Erfassungsliste im blauen Händler-Design.
* **Gesamtartikelliste (Datenbasis für Lieferantensplittung):**
  Die Excel-Datei `alle gelisteten Artikel - Stand 24.06.2026.xlsx` (abgelegt in [Meilenstein 1/](file:///C:/Users/thomas.winkler/Desktop/Projekte/Google%20Antigravity/ELEKTROPEPI/GEWAEHRLEISTUNG_GARANTIELABEL/Meilenstein%201)) diente als Rohdatenbasis zur Generierung der lieferantenspezifischen Teillisten.
* **Rechts- und Verordnungsgrundlagen:**
  * Das WKO-Referenzdokument [07_WKO_Richtlinien_Garantie_Details.md](file:///C:/Users/thomas.winkler/Desktop/Projekte/Google%20Antigravity/ELEKTROPEPI/GEWAEHRLEISTUNG_GARANTIELABEL/Meilenstein%201/07_WKO_Richtlinien_Garantie_Details.md).
  * Offizielle WKO-Informationsseite: [WKO - E-Commerce: Widerrufsbutton, Gewährleistung & Garantielabel](https://www.wko.at/handeldigital/e-commerce-widerrufsbutton-gewaehrleistung-garantielabel#heading_aufzeichnung_webinar__last_call_Widerrufsbutton__)
  * WKO-Detailseiten zu [Gewährleistung](https://www.wko.at/handel/elektro-einrichtungsfachhandel/informationspflichten-garantien-gewaehrleistung-haendle#heading_gewaehrleistung___was_muss_mitgeteilt_werden_) und [Haltbarkeitsgarantie](https://www.wko.at/handel/elektro-einrichtungsfachhandel/informationspflichten-garantien-gewaehrleistung-haendle#heading_haltbarkeitsgarantie___was_muss_mitgeteilt_werden_).
  * Englischer Leitfaden der WKO: [Practical guidelines Harmonised Label.pdf](file:///C:/Users/thomas.winkler/Desktop/Projekte/Google%20Antigravity/ELEKTROPEPI/GEWAEHRLEISTUNG_GARANTIELABEL/Meilenstein%201/Practical%20guidelines%20Harmonised%20Label.pdf) (abgelegt in Meilenstein 1).
  * Durchführungsverordnung (EU) 2025/1960 der Kommission (Anhang I & II).
* **Externe Tool-Unterstützung:**
  * Der Online-Dienstleister **[garan-label.com](https://garan-label.com/)** zur automatisierten Einzel- und Massengenerierung von EU-konformen Label-Grafiken für den m.PIM- und Magento-Import.

---

## 6. Projekt-Meilensteine

*   **Meilenstein 1: Projektvorbereitung & Lieferanten-Abfragekonzept (Q3/2026)**
    *   *Ziel:* Definition der rechtlichen Grundlagen (WKO), Erstellung der Abfragevorlage (Excel-Template) und Abstimmung der Spaltenstruktur mit dem Einkauf.
    *   *Ergebnis:* Freigegebene Templates ([de](file:///C:/Users/thomas.winkler/Desktop/Projekte/Google%20Antigravity/ELEKTROPEPI/GEWAEHRLEISTUNG_GARANTIELABEL/Meilenstein%201/Lieferantenabfrage/Supplier_Warranty_Inquiry_Template_DE.xlsx) / [en](file:///C:/Users/thomas.winkler/Desktop/Projekte/Google%20Antigravity/ELEKTROPEPI/GEWAEHRLEISTUNG_GARANTIELABEL/Meilenstein%201/Lieferantenabfrage/Supplier_Warranty_Inquiry_Template_EN.xlsx)) und [Spaltenanalyse_Lieferantenabfrage.xlsx](file:///C:/Users/thomas.winkler/Desktop/Projekte/Google%20Antigravity/ELEKTROPEPI/GEWAEHRLEISTUNG_GARANTIELABEL/Meilenstein%201/Lieferantenabfrage/Spaltenanalyse_Lieferantenabfrage.xlsx).
    *   *Status (10.07.2026):* In Bearbeitung. Spaltenanalyse und Vorlage sind erstellt. Der Abstimmungstermin mit Helmut Nobis zur finalen Spaltenfreigabe ist für **Montag, 13.07.2026 um 10:00 Uhr** vereinbart.
*   **Meilenstein 2: Datenerhebung & Lieferantenauswahl (Q3/2026)**
    *   *Ziel:* Erstellung einer Lieferantenauswahl durch Helmut Nobis (Einkauf) und anschließende Aussendung der leeren Excel-Tabellen zur Garantieabfrage (Versand erfolgt durch Thomas Winkler).
    *   *Ergebnis:* Rücklauf der ausgefüllten Erfassungsdateien (Garantiejahre, Links zu Bedingungen, Kriterien-Bestätigung) von allen ausgewählten Lieferanten (abgelegt in [Meilenstein 2/Lieferanten](file:///C:/Users/thomas.winkler/Desktop/Projekte/Google%20Antigravity/ELEKTROPEPI/GEWAEHRLEISTUNG_GARANTIELABEL/Meilenstein%202/Lieferanten)).
*   **Meilenstein 3: Technische Integration & Magento B2C-Rollout (Q3-Q4/2026)**
    *   *Ziel:* Datenimport der erhobenen Lieferantendaten in das Magento-System und Entwicklung der Frontend-Anzeige für den Elektropepi-Webshop (dynamische & geschachtelte Darstellung des Labels).
    *   *Ergebnis:* Ein voll funktionsfähiges, getestetes Magento-Modul zur gesetzeskonformen B2C-Etikettenausgabe (Ressourcen in [Meilenstein 3/](file:///C:/Users/thomas.winkler/Desktop/Projekte/Google%20Antigravity/ELEKTROPEPI/GEWAEHRLEISTUNG_GARANTIELABEL/Meilenstein%203)).
*   **Meilenstein 4: B2B-Datenpflege & m.PIM-Abgleich (Q4/2026)**
    *   *Ziel:* Abgleich der betroffenen B2B-Artikel, Generierung der Label-Grafiken (z. B. via garan-label.com) und Befüllung des m.PIM-Systems (Stammdaten + PDF-Garantiebedingungen) für Globus, Hornbach und weitere Handelspartner.
    *   *Ergebnis:* Vollständige Absicherung unseres B2B-Vertriebs durch Bereitstellung aller geforderten Datenfeeds und Printvorlagen in den zentralen Händlersystemen (Ablage in [Meilenstein 4/](file:///C:/Users/thomas.winkler/Desktop/Projekte/Google%20Antigravity/ELEKTROPEPI/GEWAEHRLEISTUNG_GARANTIELABEL/Meilenstein%204)).
