**Datum:** 2026-06-03  
**Version:** 1.1  
**Status:** In Arbeit  

# Test- & Verifizierungsplan: ComplianceLabels

Dieser Testplan definiert die Abnahmeschritte zur Überprüfung der Gesetzeskonformität (EU-Richtlinie 2024/825) auf dem Testsystem von weboffice.

---

## 1. Test-Szenarien

### Szenario A: Artikel ohne Herstellergarantie
*   **Voraussetzung:** Ein Testartikel, bei dem das Attribut `manufacturer_warranty_years` leer oder auf `0` gesetzt ist.
*   **Erwartetes Verhalten:**
    *   Die gesetzliche Gewährleistungsmitteilung (Notice) **muss** angezeigt werden.
    *   Das Garantielabel (Garan-Label) **darf nicht** erscheinen.

### Szenario B: Artikel mit Herstellergarantie (z. B. 3 Jahre)
*   **Voraussetzung:** Ein Testartikel mit `manufacturer_warranty_years` = `3`, `manufacturer` = `Siemens` und der Modellbezeichnung `WM14`.
*   **Erwartetes Verhalten:**
    *   Die gesetzliche Gewährleistungsmitteilung **muss** angezeigt werden.
    *   Das Garantielabel **muss** als reduziertes Symbol erscheinen.
    *   Die dynamischen Felder müssen exakt befüllt sein: *Siemens*, *WM14* und *3 Jahre*.
    *   Die Schriftart der dynamischen Felder muss *Inter* sein.

### Szenario C: Mobil- & Touch-Bedienung
*   **Voraussetzung:** Aufrufen der Produktdetailseite auf einem Smartphone (oder im Chrome DevTools Device-Modus).
*   **Erwartetes Verhalten:**
    *   Das Garantielabel muss sich bei kurzem Antippen (Touch) sofort in voller Größe öffnen und lesbar sein.
    *   Die Skalierung des QR-Codes muss auch auf kleinen Bildschirmen eine problemlose Kamera-Erfassung ermöglichen.

---

## 2. Visueller Konformitäts-Abgleich

| Prüfpunkt | WKO-Vorgabe | Ist-Zustand (Testsystem) | Status |
| :--- | :--- | :--- | :---: |
| **Farben** | Blau (`#003399`) & Gelb (`#FFED00`) exakt getroffen? | | [ ] |
| **Notice-Sichtbarkeit** | Notice permanent sichtbar (kein Tooltip/Dropdown)? | | [ ] |
| **Schriftart** | Dynamische Label-Felder in *Inter* gerendert? | | [ ] |
| **Symbole** | Häkchen & 365-Tage-Kalender im Label enthalten? | | [ ] |
| **QR-Code Link** | QR-Code führt direkt auf das Portal *Your Europe*? | | [ ] |
| **Nach dem Kauf** | PDF/Grafik-Label im Mailanhang der Bestellbestätigung? | | [ ] |

---

## 3. Protokollierung der Testläufe

| Datum | Testlauf # | Testartikel (SKU) | Testergebnis | Gefundene Abweichungen | Freigabe |
| :---: | :---: | :--- | :--- | :--- | :---: |
| | Run 1 | | | | [ ] |
| | Run 2 (Re-QS)| | | | [ ] |

