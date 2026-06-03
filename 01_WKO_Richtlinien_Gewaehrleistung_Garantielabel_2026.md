

**Datum:** 2026-06-03  
**Version:** 1.1  
**Status:** Freigegeben  

# WKO-Richtlinien & Webshop-Vorgaben: Gewährleistung & Garantielabel 2026

**Stichtag für das Inkrafttreten:** 27. September 2026  
**Rechtsgrundlage:** Österreichisches Verbraucherrechts-Änderungsgesetz (VerbRÄG 2026) zur Umsetzung der EU-Richtlinien 2023/2673 und 2024/825.

---

## 1. Gesetzliche Gewährleistung („Harmonised Notice“)

Die gesetzliche Gewährleistung (Mindestdauer 2 Jahre) muss künftig durch eine europaweit einheitliche Mitteilung („Harmonised Notice“) im Webshop dargestellt werden, um eine klare Abgrenzung zu freiwilligen Herstellergarantien zu schaffen.

### UI- & Platzierungsvorgaben (Das „Poster-an-der-Wand“-Prinzip)
* **Keine Verschachtelung:** Die Gewährleistungsmitteilung darf **nicht** hinter Links, Tooltips (Mouse-over) oder ausklappbaren Accordions (Toggles) versteckt werden. Sie muss für den Kunden direkt und barrierefrei sichtbar sein.
* **Empfohlene Umsetzung:** Ein fester Inhaltsblock auf der Produktdetailseite (PDP) oder ein permanenter, gut sichtbarer Banner (Sticky Footer) während der Artikelauswahl.
* **Farbpflicht:** Im Online-Shop muss zwingend die farbige EU-Vorlage verwendet werden (Blau/Gelb/Schwarz/Weiß). Schwarz-Weiß-Darstellungen sind nur für gedruckte Angebote oder Offline-Medien zulässig.
* **Inhaltsintegrität:** Der Text und das Layout sind durch die Durchführungsverordnung (EU) 2025/1960 rechtlich starr vorgegeben und dürfen gestalterisch nicht verändert werden.
* **QR-Code:** Der im Label integrierte QR-Code muss auf das offizielle EU-Portal *„Your Europe“* verlinken.

---

## 2. Freiwillige Herstellergarantien („Harmonised Label“)

Dieses Label ist nur dann verpflichtend einzubinden, wenn ein Hersteller eine freiwillige Haltbarkeitsgarantie von **mehr als 2 Jahren** auf das **gesamte Produkt** gewährt, ohne dass dafür Zusatzkosten anfallen.

### Technische & Dynamische Vorgaben
* **Datenbank-Kopplung (Dynamische Felder):** Das Label enthält variable Platzhalter, die vom Webshop dynamisch je Artikel befüllt werden müssen:
  1. **Garantiedauer:** Angabe der Jahre (z. B. „3“ oder „5“ – eine Angabe in Monaten ist im Design nicht vorgesehen).
  2. **Herstellername:** Offizieller Marken- oder Herstellername.
  3. **Modellbezeichnung:** Die eindeutige Modellkennung des Artikels.
* **Schriftart-Vorgabe:** Die variablen Texte in diesen Feldern müssen zwingend in der Schriftart **„Inter“** gerendert werden.
* **Verschachtelung zulässig (Hover/Click):** Im Gegensatz zur Gewährleistungsmitteilung darf das Garantielabel platzsparend integriert werden (z. B. als kleineres Icon). Es muss sich jedoch sofort vergrößern und vollständig anzeigen bei:
  * Erstem Mausklick / Fingertipp (Click/Touch)
  * Berührung mit der Maus (Mouse-over / Hover)
  * Touchscreen-Gesten (z. B. Auseinanderziehen)
* **Grafische Pflichtelemente:** Das Label muss zwingend den Titel **„GARAN“** sowie das Kalendersymbol (mit 365-Tage-Referenz) und das grüne Häkchen-Symbol enthalten.

---

## 3. Nachhaltigkeits- & Update-Pflichtangaben

Zusätzlich zu den Labels müssen Produktseiten ab September 2026 detaillierte Nachhaltigkeits- und Software-Informationen ausweisen:

* **Software-Updates:** Für Produkte mit digitalen Elementen (z. B. Smart-TVs, Smart-Home-Komponenten, Steuerungen) muss ein **konkretes Datum** oder ein exakter Zeitraum angegeben werden, bis zu dem der Hersteller kostenlose Sicherheits- und Funktionsupdates bereitstellt. Allgemeine Formulierungen wie „Updates so lange wie möglich“ sind unzulässig.
* **Reparierbarkeits-Wert (Repair-Score):** Falls für die Produktgruppe ein EU-weiter Reparierbarkeitswert existiert, muss dieser dargestellt werden. Andernfalls müssen Fallback-Informationen zur Verfügbarkeit von Ersatzteilen, deren geschätzten Kosten, der Bestellmöglichkeit sowie Reparaturanleitungen ausgewiesen werden.

---

## 4. Technisches Design & Style Sheet

Für die Einbindung der HTML-/CSS-Komponenten im Webshop gelten folgende exakte Vorgaben:

### Farbpalette
```text
BLAU:   HEX: #003399 | RGB: 0, 51, 153  | CMYK: 100, 80, 0, 0
GELB:   HEX: #FFED00 | RGB: 255, 237, 0 | CMYK: 0, 0, 100, 0
SCHWARZ: HEX: #000000 | RGB: 0, 0, 0     | CMYK: 0, 0, 0, 100
WEISS:  HEX: #FFFFFF | RGB: 255, 255, 255 | CMYK: 0, 0, 0, 0
```

### Typografie
* Alle editierbaren Felder im Garantielabel müssen in **„Inter“** (Regular, SemiBold oder ExtraBold) dargestellt werden.

### QR-Code
* Muss scannbar sein (mind. 95x100mm im Offline-Verhältnis als Orientierungsgröße) und auf das offizielle EU-Portal *„Your Europe“* verlinken.

---

## 5. Umsetzungs-Checkliste für den Webshop

- [ ] **Gewährleistungshinweis (Notice):** Permanent sichtbarer farbiger Inhaltsblock auf jeder PDP (ohne Tooltip/Zusatzklick).
- [ ] **Garantielabel (Garan-Label):** Dynamisches Rendering von *Modellbezeichnung, Herstellername* und *Jahren* in der Schriftart *Inter*.
- [ ] **Hover/Touch-Event:** Einblendung des vollständigen Garantielabels bei Hover oder Klick auf der Produktseite.
- [ ] **Update-Angaben:** Spezifisches Enddatum für Software-Updates gepflegt (bei digitalen Produkten).
- [ ] **Reparierbarkeit:** Repair-Score oder fallback-basierte Ersatzteil-Informationen auf der PDP dargestellt.
- [ ] **Bestellbestätigung (Nach dem Kauf):** Automatisierter Versand des farbigen Labels als dauerhafter Datenträger (z. B. PDF-Anhang in der E-Mail).
