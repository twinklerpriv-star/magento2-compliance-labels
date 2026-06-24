# Kontext & Bewertungen: Gewährleistungs- und Garantielabel 2026

**Datum:** 10.06.2026

## Strategische Einschätzungen & Entscheidungsrational

## 23.06.2026: Sitzungs-Kontext & Bewertungen
*   **Aktive Strategie:**
    Die Datenerhebung für Herstellergarantien (> 2 Jahre) wird über standardisierte, zweisprachige Excel-Erhebungsbögen gestartet, um Einkaufsmitarbeitern und Lieferanten ein klares Datenformat vorzugeben.
    Das strikte Einhalten der SBS-Corporate-Design-Richtlinien (Stahlblau/Pastellgelb) sorgt für ein professionelles Auftreten gegenüber den Lieferanten und minimiert Rückfragen.
*   **🚨 Aktives Risiko: Rücklaufquote der Lieferanten-Daten**
    Die zeitnahe Rückmeldung der Lieferanten bezüglich der konkreten Garantiejahre und der Bereitstellung der Labels ist der kritische Pfad für den CSV-Import.
    Fehlende oder unvollständige Daten können den Go-Live-Termin der Frontend-Garantielabel gefährden.

## 16.06.2026: Sitzungs-Kontext & Bewertungen
*   **Aktive Strategie:**
    Der offizielle Start des Folgeprojekts zur Implementierung der gesetzlichen Garantielabels ist für unmittelbar nach dem morgigen WKO-Webinar (17.06.2026 um 13:00 Uhr) angesetzt.  
    Die dort vermittelten regulatorischen Details bilden das Fundament für die finale weboffice-Spezifikation.  
*   **🚨 Aktives Risiko: Datenqualität im Artikelstamm**
    Die Befüllung der Attribute für Garantiejahre und Hersteller bei rund 4.000 Magento-Artikeln bis zum gesetzlichen Stichtag am 27.09.2026 ist zeitkritisch.  
    Ein automatisierter CSV-Import oder eine direkte Schnittstellenübermittlung muss frühzeitig mit Multidata abgestimmt werden, um manuelle Pflegeaufwände zu vermeiden.  

* **Inline-SVG vs. Bilddateien:**
  Die Entscheidung für Inline-SVGs statt statischer Bilddateien (`.png`/`.jpg`) ist rechtlich zwingend.
  Nur durch Inline-SVG können Platzhalter im WKO-Garantielabel (wie „Brand/Trademark“ oder „XX“ Jahre) zur Laufzeit dynamisch mit echten Magento-Produktdaten befüllt werden.
  Gleichzeitig optimiert dies die Ladezeit der Produktdetailseite (PDP), da der Browser keine zusätzlichen Bild-HTTP-Requests ausführen muss.
* **Übersetzungs-Relevanz (i18n):**
  Die Übersetzung der Label-Header `"Brand/Trademark"` ➔ `"Marke/Handelsmarke"` und `"Model identifier"` ➔ `"Modellkennung"` in den deutschen Sprachpaketen (`de_AT.csv`/`de_DE.csv`) ist rechtlich kritisch.
  Eine reine englische Beschriftung auf dem ansonsten deutschen Label im österreichischen/deutschen Webshop stellt eine Abmahngefahr dar, da die EU-Verordnung 2025/1960 die jeweilige Amtssprache verlangt.

## Aktive Risiken & Blinde Flecken
* **Garantie-Attribute in Magento:**
  Das Modul setzt voraus, dass die Attribute `manufacturer_warranty_years`, `manufacturer` und `model` im Backend existieren und gepflegt sind.
  Sollte das Einpflegen dieser Attribute bei ~4.000 Artikeln vor dem Stichtag (27.09.2026) scheitern, wird das GARAN-Label nicht korrekt oder unvollständig ausgespielt.
  Dieses Risiko muss durch eine frühzeitige Datenpflege-Initiative (z. B. Import via CSV) minimiert werden.
