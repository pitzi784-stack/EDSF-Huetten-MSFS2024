# EDSF: SDK-Validierung und Release-Gate

## Aktueller Quellstand
- `PackageSources/EDSF/airport_EDSF_DRAFT.xml`: MSFS-2024-Airport-XML mit Grasbahn 11/29 und zwei Startpositionen.
- **Noch nicht als SDK-kompatibel bestätigt:** Der XML-Entwurf wurde nicht mit dem SDK kompiliert.
- Platzmarker 47.6344533 / 7.9407154 ist **nicht** als vermessener Bahnpunkt bestätigt.
- 880 m Höhe, 110° Bahnachse, 670 x 30 m und daraus abgeleitete Schwellen sind vorläufig.
- Die bisherigen 3D-Gebäude sind Konzeptgeometrie, nicht originalgetreue EDSF-Modelle.

## Validierungsfolge (MSFS 2024)
1. Offizielles SDK-Beispiel **SimpleAirport** im Developer Mode öffnen und mit **Build and Mount** erfolgreich bauen.
2. EDSF-Airport-XML im SDK Scenery Editor laden/erzeugen und eventuelle Parser- oder Schemafehler beheben.
3. Existierenden EDSF-Airport im Simulator untersuchen; bestehende Pisten-/Parkplatzdaten nicht versehentlich duplizieren.
4. Reale Bahnschwellen und Gebäude anhand zugelassener Luftbilder/Pläne präzise verorten.
5. Modellbibliothek und MSFS-2024-konforme 3D-Modelle exportieren; Gebäude und Vegetation im Editor platzieren.
6. PackageDefinitions und Projekt-XML vom SDK erzeugen bzw. anhand des offiziellen Musters validieren.
7. Build, Mount, Kaltstart, FPS, Kollisionen und Abstände im Simulator prüfen.
8. **Erst dann** Community-Paket für Google Drive freigeben.

## Lieferung
**Quellen auf GitHub. Nur ein getesteter Community-Build nach Google Drive.**
In dieser Chat-Sitzung steht derzeit keine verbundene Google-Drive-Schreibaktion zur Verfügung; ein Drive-Upload wurde nicht durchgeführt.

## SDK-Quellen
- https://docs.flightsimulator.com/msfs2024/retail/samples-tutorials/samples/sceneries/simpleairport/
- https://docs.flightsimulator.com/msfs2024/retail/content-configuration/environment/airports-and-facilities/runway-xml-properties/
- https://docs.flightsimulator.com/msfs2024/retail/content-configuration/environment/airports-and-facilities/airport-xml-properties/
