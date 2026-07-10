# Sbs_ComplianceLabels (Magento 2 Extension)

Dieses Magento 2-Modul implementiert die ab dem **27. September 2026** in Kraft tretenden EU-Verbraucherschutzrichtlinien (VerbRÄG 2026 / EU 2024/825) zur harmonisierten Kennzeichnung von gesetzlichen Gewährleistungen und freiwilligen Herstellergarantien (durability labels) im Webshop von **Elektropepi**.

---

## 🛠️ Features

1. **Gesetzliches Gewährleistungs-Poster (Statutory Notice Poster):**
   * Permanenter, nicht einklappbarer Info-Block auf der Produktdetailseite.
   * Entspricht exakt den WKO-Farbvorgaben (Blau: `#003399`, Gelb: `#FFED00`).
   * Enthält den offiziellen, scannbaren QR-Code, der direkt auf das EU-Portal *Your Europe* verlinkt.
2. **Freiwilliges Hersteller-Garantielabel (GARAN Durability Label):**
   * Erscheint dynamisch nur bei Artikeln mit einer Herstellergarantie von **mehr als 2 Jahren**.
   * Einklappbar per JavaScript-Toggle (benutzerfreundlich für Mobilgeräte).
   * Zeigt dynamisch Marke, Modell und Garantiedauer an.
3. **Mehrsprachigkeit (i18n):**
   * Alle Texte laufen über Magentos Übersetzungshelfer (`__('...')`).
   * Lokalisierungen für Deutschland (`de_DE.csv`), Österreich (`de_AT.csv`) und Englisch (`en_US.csv`) sind im Modul enthalten.

---

## 📋 Voraussetzungen (Magento-Attribute)

Damit das dynamische **GARAN-Garantielabel** ausgespielt wird, müssen im Magento-Backend folgende Attribute angelegt und beim Produkt gepflegt sein:

1. **`manufacturer_warranty_years`** (Eigenschaft: Text oder Dropdown)
   * *Zweck:* Gibt die Dauer der Herstellergarantie in Jahren an (z. B. `3` oder `5`). 
   * *Hinweis:* Bei Werten `<=` 2 wird das Garantielabel ausgeblendet (da dies durch die gesetzliche Gewährleistung abgedeckt ist).
2. **`manufacturer`** (Hersteller-Attribut)
   * *Zweck:* Wird für das Feld „Brand/Trademark“ auf dem Label ausgelesen.
3. **`model`** (Modell-Attribut)
   * *Zweck:* Wird für das Feld „Model identifier“ auf dem Label ausgelesen. Falls nicht vorhanden/gepflegt, erfolgt ein automatischer Fallback auf die Artikelnummer (SKU).

---

## ⚙️ Installation (Manuell)

Das fertige Deployment-Paket liegt als **`Sbs_ComplianceLabels.zip`** im Root-Verzeichnis dieses Repositories.

1. Entpacke das Zip-Archiv.
2. Kopiere die entpackten Dateien auf dem Webserver in das Verzeichnis:
   `app/code/Sbs/ComplianceLabels/`
3. Führe per SSH im Magento-Wurzelverzeichnis folgende Standard-Befehle aus:
   ```bash
   php bin/magento setup:upgrade
   php bin/magento setup:di:compile
   php bin/magento setup:static-content:deploy
   php bin/magento cache:clean
   ```

---

## 📁 Projektstruktur

```text
Meilenstein 3/
├── README.md                     # Diese Anleitung zur Installation
├── Sbs_ComplianceLabels.zip      # Das fertige Installationspaket für die Agentur
├── implementation_plan_magento.md # Technischer Konzeptplan für Magento
├── task_magento.md               # Lokale Aufgabenliste für das Magento-Modul
├── tests.md                      # Test- & QS-Protokoll zur Abnahme
└── MODUL_QUELLCODE/              # Die Magento-Moduldateien
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

## 📞 Kontakt & Dokumentation
Entwickelt von **SBS** (Thomas Winkler).  
Dokumentationen und QS-Pläne liegen im Root-Verzeichnis dieses Repositories vor.
