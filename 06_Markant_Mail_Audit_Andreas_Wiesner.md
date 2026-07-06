# Rechtliche & technische Bewertung der Markant/Globus-E-Mail (EU-Verordnung 2025/1960)

**An:** Andreas Wiesner (Geschäftsführung)  
**Von:** Thomas Winkler (Projektleiter Gewährleistungs- und Garantielabel 2026)  
**Datum:** 06.07.2026  
**Status:** Zur Information / Entscheidungsvorbereitung (Korrektur: Fokus SBS als Lieferant)

---

## 1. Management Summary

Die von Markant PIM weitergeleitete E-Mail beschreibt die Systemanforderungen des Großhändlers *Globus Fachmärkte* zur Umsetzung der Durchführungsverordnung (EU) 2025/1960 (Garantielabel ab 27.09.2026). 

**Richtigstellung der Rollen:**  
In diesem Kontext ist **Globus Fachmärkte der Händler (Retailer)** und **SBS Austria der Lieferant/Hersteller**. Globus verlangt von uns (SBS) Garantiedaten, um seine gesetzlichen Verbraucherinformationspflichten erfüllen zu können.

Die E-Mail von Markant enthält jedoch fachliche Ungenauigkeiten und stellt rein technische Krücken ihres PIM-Systems als gesetzliche Pflichten dar. 

---

## 2. Die drei wesentlichen Diskrepanzen im Markant-Text

### Diskrepanz 1: Die angebliche Pflicht zum Upload eines „Garantie-Labels als PDF“
* **Aussage Markant:**  
  Lieferanten (SBS) müssen ein *„Garantie-Label als PDF“* über m.PIM hochladen, damit das Globus-System die gewerbliche Haltbarkeitsgarantie erkennt.
* **Rechtlicher Fakt:**  
  **Es gibt keine gesetzliche Verpflichtung für uns als Lieferant, ein visuelles Label als PDF zu erstellen oder hochzuladen.** Das grüne „GARAN“-Symbol ist ein standardisiertes Element der EU-Kommission. Es wird von den Shop-Systemen der Händler (wie Globus) dynamisch gerendert. 
* **Bedeutung für SBS:**  
  Markant nutzt hier eine technische Krücke: Das Hochladen eines PDF-Dokuments (tatsächlich gemeint sind die *Garantiebedingungen*) dient im PIM-System lediglich als Auslöser (Trigger), um die Garantieart systemseitig zu filtern. SBS muss daher kein grafisches Label entwerfen, sondern lediglich die Garantiebedingungen (Text/PDF) hochladen.

### Diskrepanz 2: Die unvollständige Händlerpflicht (Verschweigen der Haftungsbefreiung)
* **Aussage Markant:**  
  *„Für die gewerbliche Haltbarkeitsgarantie ist der Händler [Globus] darüber hinaus verpflichtet, diese Informationen [...] unter Verwendung des harmonisierten EU-Garantielabels darzustellen.“*
* **Rechtlicher Fakt:**  
  Die Anzeigepflicht des Händlers ist laut EU-Richtlinie 2024/825 (EmpCo) und FAGG **konditional** (bedingt). Sie gilt nur dann, **wenn der Hersteller dem Händler diese Informationen zur Verfügung stellt**.
* **Bedeutung für SBS:**  
  Globus/Markant stellen die Pflicht des Händlers als absolut dar, um Druck auf uns als Lieferanten auszuüben. Weigert sich ein Lieferant, Daten bereitzustellen, ist der Händler zwar von der Label-Anzeige befreit, darf aber auch nicht mehr mit der Garantie werben (Werbeverbot).

### Diskrepanz 3: Das Abmahnrisiko durch die automatisierte Globus-Systemlogik
* **Aussage Markant:**  
  *„Die Unterscheidung der Garantiearten erfolgt dabei systemseitig bei Globus anhand des Vorhandenseins des Garantie-Labels [PDF].“*
* **Rechtlicher Fakt:**  
  Das offizielle EU-Garantielabel darf **ausschließlich** für kostenlose Garantien verwendet werden, die das **gesamte Gerät** abdecken (gewerbliche Haltbarkeitsgarantie). Eine irrtümliche Einblendung des Labels bei Teilgarantien (z. B. nur auf den Motor) ist ein Wettbewerbsverstoß.
* **Bedeutung für SBS:**  
  Wenn SBS eine Teilgarantie anbietet und dafür fälschlicherweise ein PDF im m.PIM hochlädt, würde Globus dies automatisch als Vollgarantie labeln. Dies führt zu einer direkten **Abmahnbarkeit des Händlers (Globus)**. Eine rein dateibasierte Erkennung durch das PIM-System ist fachlich und rechtlich riskant.

---

## 3. Klarstellung der Pflichten für SBS Austria

Um für die Geschäftsführung absolute Klarheit zu schaffen, werden unsere Pflichten im Folgenden in „tatsächliche Pflichten“ und „keine Verpflichtungen“ unterteilt:

### A. Wozu SBS tatsächlich verpflichtet ist (Tatsächliche Pflichten)
1. **Bereitstellung von Garantiedaten bei aktiver Werbung (Kommerzieller Zwang):** Wenn SBS möchte, dass Globus unsere Artikel mit einer Herstellergarantie von über 2 Jahren bewirbt, **müssen** wir die Daten (Dauer und Link zu den Bedingungen) liefern. Ohne diese Daten darf Globus die Garantie im Shop nicht mehr erwähnen.
2. **Datenpflege im PIM-System (Schnittstellen-Vertrag):** Um im m.PIM/GDSN-System von Globus gelistet zu bleiben, müssen wir die entsprechenden Datenfelder (Garantiedauer in Monaten) befüllen.
3. **Haftung für die Richtigkeit der Angaben:** SBS haftet gegenüber Globus für die Richtigkeit der übermittelten Daten. Bestätigen wir fälschlicherweise eine Garantie als „kostenlose Vollgarantie“ (obwohl es sich um eine Teilgarantie handelt) und wird Globus deswegen abgemahnt, drohen SBS Regressforderungen.

### B. Wozu SBS NICHT verpflichtet ist (Keine Verpflichtungen)
1. **Kein Erstellen oder Liefern von Grafik-Labels (Bilddateien):** SBS muss **keine** Bilddateien, PNGs oder fertig gestalteten grünen Symbole („3 GARAN“ etc.) an Globus liefern. Das Rendern des Labels ist die alleinige technische Aufgabe des Online-Shops von Globus.
2. **Keine Label-Pflicht für Standardgarantien (≤ 2 Jahre):** Garantien von bis zu 2 Jahren sind vom Gesetz nicht betroffen und erfordern keine Sonderbehandlung.
3. **Keine Label-Pflicht für Teilgarantien:** Bietet SBS Garantien an, die nicht das gesamte Produkt abdecken (z. B. 5 Jahre Garantie, aber nur auf den Kompressor eines Kühlschranks), fallen diese nicht unter die EU-Verordnung. Sie werden wie bisher als normale Produktattribute gepflegt.
4. **Keine direkte gesetzliche Strafe bei Nicht-Lieferung:** Verbraucherschutzgesetze (VerbRÄG 2026/FAGG) regeln das Verhältnis zum Endverbraucher. Liefert SBS die Daten nicht an Globus, begeht SBS keinen direkten Gesetzesverstoß. Die Konsequenz ist rein vertrieblicher Natur (Globus darf die Garantie nicht mehr bewerben).

---

## 4. Bewertung der Betroffenheit von SBS Austria

Für das Produktmanagement und den Vertrieb von SBS ergeben sich folgende Handlungsschritte:

1. **Sortimentsabgleich (Betroffenheits-Prüfung):**  
   Bietet SBS Austria für Artikel, die an Globus geliefert werden, eine **kostenlose Herstellergarantie von mehr als 2 Jahren** an, die das **gesamte Produkt** abdeckt (Vollgarantie)?
   * *Falls ja:* Wir müssen die Garantiedauer (in Monaten) im m.PIM eintragen und das PDF der Garantiebedingungen (Garantiekarte/AGB) hochladen.
   * *Falls nein:* Es ist **keine Aktion** erforderlich. Die Artikel werden im System normal weitergeführt.
2. **Dokumenten-Bereitstellung:**  
   Das in m.PIM geforderte Dokument ist lediglich das Text-PDF unserer Garantiebestimmungen, **kein** grafisches Label.

---

## 5. Handlungsempfehlung für die Geschäftsführung (Andreas Wiesner)

Um die Anfrage von Globus/Markant fristgerecht bis zum **27.07.2026** zu beantworten, empfehlen wir folgendes Vorgehen:

* **Schritt 1: Sortimentsabgleich initiieren**  
  Das Produktmanagement prüft das an Globus gelieferte Sortiment auf betroffene Vollgarantien (> 2 Jahre).
* **Schritt 2: Gezielte m.PIM-Datenpflege**  
  Nur für tatsächlich betroffene Artikel die m.PIM-Erweiterung aktivieren, Monate eintragen und Garantiebedingungen-PDF hochladen.
* **Schritt 3: Rückmeldung an Globus bei Nicht-Betroffenheit**  
  Sollte SBS für Globus-Artikel keine betroffenen Garantien gewähren, ist laut E-Mail keine weitere Aktion notwendig. Zur Sicherheit sollte dem Globus-Einkauf kurz schriftlich bestätigt werden, dass unsere Artikel nicht unter die Richtlinie fallen.
