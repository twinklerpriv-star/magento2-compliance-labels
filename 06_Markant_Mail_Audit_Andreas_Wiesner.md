# Rechtliche & technische Bewertung der Markant/Globus-E-Mail (EU-Verordnung 2025/1960)

**An:** Andreas Wiesner (Geschäftsführung)  
**Von:** Thomas Winkler (Projektleiter Gewährleistungs- und Garantielabel 2026)  
**Datum:** 06.07.2026  
**Status:** Zur Information / Entscheidungsvorbereitung (Korrektur: Fokus SBS als Lieferant)

---

## 1. Management Summary

Die von Markant PIM weitergeleitete E-Mail beschreibt die Systemanforderungen des Großhändlers *Globus Fachmärkte* zur Umsetzung der Durchführungsverordnung (EU) 2025/1960 (Garantielabel ab 27.09.2026). 

**Wichtigste Klarstellung zur Rolle von SBS:**  
In dieser Konstellation ist **Globus Fachmärkte der Händler (Retailer)** und **SBS Austria der Lieferant/Hersteller**. Die E-Mail fordert uns (SBS) auf, unsere Garantiedaten im Markant-PIM-System zu pflegen, damit Globus seine gesetzlichen Anzeigepflichten im Globus-Shop erfüllen kann.

Die E-Mail von Markant enthält jedoch fachliche Ungenauigkeiten und verwechselt technische Anforderungen des Markant-Systems mit tatsächlichen gesetzlichen Verpflichtungen für uns als Lieferant.

---

## 2. Die drei wesentlichen Diskrepanzen im Markant-Text

### Diskrepanz 1: Die angebliche Pflicht zum Upload eines „Garantie-Labels als PDF“
* **Aussage Markant:**  
  Lieferanten (SBS) müssen ein *„Garantie-Label als PDF“* über m.PIM hochladen, damit das Globus-System die gewerbliche Haltbarkeitsgarantie erkennt.
* **Rechtlicher Fakt:**  
  **Es gibt keine gesetzliche Verpflichtung für Lieferanten oder Händler, ein visuelles Label als PDF zu erstellen oder hochzuladen.** Das grüne „GARAN“-Symbol ist ein standardisiertes Element der EU-Kommission. Es wird von den Shop-Systemen der Händler (wie Globus) dynamisch gerendert. 
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

## 3. Bewertung der Betroffenheit von SBS Austria

Für SBS Austria als Lieferant von Globus ergeben sich folgende Handlungsschritte:

1. **Prüfung des Sortiments (Betroffenheit):**  
   Bietet SBS Austria für Artikel, die an Globus geliefert werden, eine **kostenlose Herstellergarantie von mehr als 2 Jahren** an, die das **gesamte Produkt** abdeckt?
   * *Falls ja:* Wir sind verpflichtet, die Garantiedauer (in Monaten) in m.PIM einzutragen und die Garantiebedingungen als PDF hochzuladen.
   * *Falls nein:* Es ist **keine Aktion** erforderlich. Normale 2-Jahres-Garantien oder Teilgarantien (z. B. Garantie nur auf bestimmte Teile) fallen nicht unter die Label-Pflicht und werden im Markant-System wie bisher ohne PDF-Upload gepflegt.
2. **Keine grafischen Arbeiten nötig:**  
   Der Einkauf bzw. Produktmanagement von SBS muss keine Bilddateien oder Logos entwerfen. Das geforderte Dokument ist lediglich das Text-PDF der Garantievereinbarung.

---

## 4. Handlungsempfehlung für die Geschäftsführung (Andreas Wiesner)

Um die Anfrage von Globus/Markant fristgerecht bis zum **27.07.2026** zu beantworten, empfehlen wir folgendes Vorgehen:

* **Schritt 1: Sortimentsabgleich durch Produktmanagement / Vertrieb**  
  Prüfen, ob SBS-Eigenmarken oder exklusiv vertriebene Artikel mit einer kostenlosen Herstellergarantie von > 2 Jahren an Globus geliefert werden.
* **Schritt 2: Datenpflege im m.PIM (nur bei Betroffenheit)**  
  Aktivierung der „Globus Fachmärkte“-Extension im m.PIM und Befüllung des Attributs „Herstellergarantie“ (in Monaten) sowie Upload der Garantiebedingungen (PDF) für die betroffenen Artikel.
* **Schritt 3: Rückmeldung an Globus bei Nicht-Betroffenheit**  
  Ergibt die Prüfung, dass SBS für Globus-Artikel keine Garantien über 2 Jahre gewährt, ist laut E-Mail keine weitere Aktion notwendig. Zur Sicherheit sollte dem Globus-Einkauf kurz schriftlich bestätigt werden, dass unsere Artikel nicht unter die Richtlinie fallen.
