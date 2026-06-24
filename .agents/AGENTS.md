# Custom Rules

## Workspace-Synchronisation Scope-Optimierung
*   **Synchronisations-Scope:**
    *   Der Dateivergleich und Abgleich (Initialisierungs- und Abschluss-Sync) beschränkt sich **ausschließlich** auf die globalen Dateien im Haupt-Root-Verzeichnis (wie `00_*.md`, `task.md`, `walkthrough.md`) sowie auf die Dateien direkt in dem für dieses Teilprojekt zuständigen Ordner (z. B. `GEWAEHRLEISTUNG_GARANTIELABEL/` und dessen Unterordner).
    *   Alle anderen Teilprojekt-Verzeichnisse (z. B. `BESTELLRYTHMUS/`, `SCHULUNGEN/`, `SPEDITIONEN/` etc. im übergeordneten Verzeichnisstruktur-Scope) werden beim Synchronisations-Abgleich komplett ignoriert.
