# EDSF Hütten-Hotzenwald – MSFS 2024

Quellprojekt für eine Szenerie des Sonderlandeplatzes EDSF. **In Entwicklung, noch nicht installierbar.**

## Ziel
Originalgetreue Graspiste, Hangars, Vereinsheim, Abstellflächen und Umgebung. Quellen werden hier versioniert; nur ein späterer getesteter Release wird nach Google Drive ausgeliefert.

## Projektstruktur
- `PackageSources/`: Szenerie- und Modelldaten
- `PackageDefinitions/`: SDK-Paketdefinitionen (nach SDK-Validierung)
- `docs/`: Referenzen und Bauplan
- `tools/`: reproduzierbare Modellierungswerkzeuge

## Status
Die geometrischen Konzeptmodelle sind über `tools/generate_models.py` reproduzierbar. Exakte Positionen und Maße müssen anhand verlässlicher Quellen bestätigt werden. Keine Google-Maps-Bilder als Texturen verwenden.

## Build
MSFS-2024-Developer-Mode/SDK auf Windows benötigt. Eine gültige Airport-XML und ModelLib werden nach Prüfung gegen die SDK-Beispiele ergänzt; dieses Repository ist noch **kein fertiges Community-Paket**.
