# Rechtliche & technische Bewertung der Markant/Globus-E-Mail (EU-Verordnung 2025/1960)

**An:** Andreas Wiesner (Geschäftsführung)  
**Von:** Thomas Winkler (Projektleiter Gewährleistungs- und Garantielabel 2026)  
**Datum:** 06.07.2026  
**Status:** Zur Information / Entscheidungsvorbereitung  

---

## 1. Management Summary

Die von Markant PIM weitergeleitete E-Mail beschreibt die Systemanforderungen des Großhändlers *Globus Fachmärkte* zur Umsetzung der Durchführungsverordnung (EU) 2025/1960 (Garantielabel ab 27.09.2026). 

**Wichtigste Erkenntnis für Elektro Pepi:**  
Der E-Mail-Text von Markant enthält gravierende rechtliche Diskrepanzen und stellt rein technische Krücken ihres PIM-Systems als gesetzliche Pflichten dar. 
Für Elektro Pepi besteht **kein technischer oder operativer Handlungsbedarf**. Unser eingeschlagener Weg (direkte Excel-Erfassung der strukturierten Daten und dynamisches Rendering im Magento-Frontend) ist rechtssicher, schützt uns vor Abmahnungen und ist technisch deutlich robuster als das von Globus gewählte Verfahren.

---

## 2. Die drei wesentlichen Diskrepanzen im Markant-Text

### Diskrepanz 1: Die angebliche Pflicht zum Upload eines „Garantie-Labels als PDF“
* **Aussage Markant:**  
  Lieferanten müssen ein *„Garantie-Label als PDF“* über m.PIM hochladen, damit das System die gewerbliche Haltbarkeitsgarantie erkennt.
* **Rechtlicher Fakt:**  
  **Es gibt keine gesetzliche Verpflichtung für Hersteller oder Händler, ein visuelles Label als PDF zu erstellen oder zu übermitteln.** Die EU-Verordnung schreibt lediglich das Aussehen des grünen „GARAN“-Symbols (Jahre + Schriftzug) zwingend vor. Die Darstellung dieses Symbols erfolgt **dynamisch durch die jeweilige Shop-Software** des Händlers anhand der Rohdaten.
* **Hintergrund:**  
  Das m.PIM-System von Markant kann die Garantiearten offenbar nicht intelligent filtern. Als Umgehungslösung prüft Globus einfach: *„Liegt eine PDF-Datei vor? Wenn ja, blende das EU-Label ein.“* Das ist eine rein hausinterne IT-Spezialität von Globus/Markant und keine gesetzliche Pflicht.

### Diskrepanz 2: Die unvollständige Händlerpflicht (Verschweigen der Haftungsbefreiung)
* **Aussage Markant:**  
  *„Für die gewerbliche Haltbarkeitsgarantie ist der Händler darüber hinaus verpflichtet, diese Informationen [...] unter Verwendung des harmonisierten EU-Garantielabels darzustellen.“*
* **Rechtlicher Fakt:**  
  Die Pflicht des Händlers (Elektropepi oder Globus) ist laut EU-Richtlinie 2024/825 (EmpCo) und § 4 FAGG **konditional** (bedingt): Sie gilt nur dann, **wenn der Hersteller dem Händler diese Informationen zur Verfügung stellt**.
* **Hintergrund:**  
  Liefert der Hersteller trotz Anfrage keine Daten, ist der Händler von der Anzeigepflicht des Labels befreit und kann für das Fehlen nicht abgemahnt werden. (Globus verschweigt diese gesetzliche Haftungsbefreiung im Anschreiben, um den Druck auf die Lieferanten zur Datenlieferung zu maximieren).

### Diskrepanz 3: Das Abmahnrisiko durch die automatisierte Globus-Systemlogik
* **Aussage Markant:**  
  *„Die Unterscheidung der Garantiearten erfolgt dabei systemseitig bei Globus anhand des Vorhandenseins des Garantie-Labels [PDF].“*
* **Rechtlicher Fakt:**  
  Diese Logik birgt ein hohes rechtliches Risiko. Lädt ein Lieferant ein PDF für eine *Teilgarantie* hoch (z. B. eine 5-Jahres-Garantie, die nur den Kompressor eines Kühlschranks abdeckt), würde das System von Globus fälschlicherweise das EU-Garantielabel einblenden.
* **Hintergrund:**  
  Das offizielle EU-Garantielabel darf **ausschließlich** für Garantien verwendet werden, die kostenlos sind und das **gesamte Gerät** abdecken. Eine irrtümliche Einblendung des Labels bei Teilgarantien ist ein Wettbewerbsverstoß und führt zu einer direkten **Abmahnbarkeit des Händlers**.

---

## 3. Vergleich der Vorgehensweisen: Globus/Markant vs. Elektro Pepi

| Kriterium | Ansatz Globus Fachmärkte (Markant) | Ansatz Elektro Pepi (Magento 2) |
| :--- | :--- | :--- |
| **Datenquelle** | m.PIM / GDSN-Netzwerk (Standardisierte PIM-Felder) | Direkte, strukturierte Lieferanten-Excelabfrage (DE/EN) |
| **Garantie-Nachweis** | Manueller PDF-Upload durch Lieferanten | Strukturierte Angaben (Marke, Modell, Jahre, URL, Vollgarantie-Ja/Nein) |
| **Label-Erstellung** | Abhängig von hochgeladener PDF-Datei | Vollautomatische, dynamische HTML/CSS-Generierung im Frontend |
| **Fehlerrisiko** | **Hoch** (Upload falscher PDFs führt zu unzulässiger Label-Anzeige) | **Minimiert** (Filterung über dedizierte Spalte I verhindert Fehlbelegungen) |
| **Abmahnschutz** | Schwach, da Systemlogik fehleranfällig ist | **Stark**, da bei Verweigerung kein Label angezeigt wird (Werbung wird blockiert) |

---

## 4. Handlungsempfehlung für die Geschäftsführung (Andreas Wiesner)

Da unser technisches und organisatorisches Konzept vollkommen konform mit der Rechtslage und dem WKO-Seminar ist, sind **keine Änderungen** an den Excel-Dateien oder am Magento-Modul nötig. 

Für den Einkauf empfehlen wir folgende Vorgehensweise:
1. **Konsequente Nutzung unserer Excel-Abfragen:**  
   Lieferanten müssen unsere Tabellen ausfüllen. Verweisen Lieferanten darauf, die Daten bei Markant eingepflegt zu haben, sollte der Einkauf klarstellen, dass Elektro Pepi keinen automatisierten Import aus dem GDSN-Pool nutzt und die Daten zwingend strukturiert über unsere Dateien benötigt.
2. **Nutzung des Hebel-Arguments:**  
   Verweigert ein Lieferant die Zieldaten, darf das Produkt im Online-Shop ab dem 27.09.2026 nicht mehr mit einer verlängerten Garantie (z. B. „5 Jahre Garantie“ im Text) beworben werden. Dies führt zu direkten Umsatzeinbußen für den Lieferanten und sollte vom Einkauf als Argument genutzt werden.
