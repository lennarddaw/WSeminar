# Wetter als Kriegsfaktor: Der gescheiterte Vormarsch der Heeresgruppen 1941

## Projektübersicht

**W-Seminar Arbeit aus dem Fach Geschichte**  
**Oberstufenjahrgang 2024/2026**  
**Otto-von-Taube-Gymnasium**

### Forschungsfrage
> Inwiefern beeinflussten klimatische und geografische Bedingungen den Vormarsch der Heeresgruppen Nord, Mitte und Süd im Rahmen des deutschen Angriffs auf die Sowjetunion im Jahr 1941?

### Projektinformationen
- **Verfasser:** Lennard Gross
- **Seminarleiter:** Sebastian Weber
- **Kurztitel:** Wetter als Kriegsfaktor: Der gescheiterte Vormarsch der Heeresgruppen 1941
- **Zeitraum:** 2024-2026

---

## Zielsetzung

Diese Seminararbeit untersucht den Einfluss meteorologischer und geografischer Faktoren auf den militärischen Verlauf der Operation Barbarossa im Jahr 1941. Im Fokus stehen alle drei deutschen Heeresgruppen (Nord, Mitte, Süd) und deren Operationen von Juni bis Dezember 1941. Durch die Kombination historischer Quellen mit modernen Wetterdatenanalysen (ERA5-Reanalyse) wird eine interdisziplinäre Herangehensweise verfolgt, die operative Wendepunkte, Versorgungsengpässe und wetterbedingte Einschränkungen präzise rekonstruiert.

---

## Projektstruktur

```
C:\WSeminar/
├── analysis/           # Wetteranalysen und Visualisierungen
│   ├── video/            # Animationen der Wetterdaten
│   └── *.png             # Diagramme und Karten
├── installation/       # Software-Tools
│   ├── PanoplyWin-5.7.1/ # Wettervisualisierung
│   └── XyGrib/           # GRIB-Dateien Viewer
├── parts/             # Kapitel der Seminararbeit
├── raw/               # Rohdaten
│   ├── copernicus/      # Copernicus Climate Data Store
│   ├── other/            # Weitere Datenquellen
│   └── ourworldindata/   # Our World in Data
├── scripts/           # Python-Scripts und Exposé
└── sources/           # Historische Quellen
```

---

## Gliederung der Arbeit

### I. Einleitung
- Problemstellung und Forschungsfrage
- Methodische Herangehensweise
- Quellenlage und Forschungsstand

### II. Strategische Ausgangslage der Heeresgruppen bis Juli 1941
- **II.1** Zielsetzung bis Herbst 1941
  - Heeresgruppe Nord: Vorstoß auf Leningrad
  - Heeresgruppe Mitte: Kesselschlachten und Moskau-Operation
  - Heeresgruppe Süd: Ukraine und Donez-Becken
- **II.2** Auswirkungen der Schlammperiode („Rasputiza")
  - Herbstliche Nässe und Wegeaufweichung
  - Regionale Unterschiede im Niederschlagsregime

### III. Wetterbedingte Herausforderungen nach dem Herbst 1941
- **III.1** Auswirkungen auf die Soldaten der Wehrmacht
  - **III.1a** Fehlende Winterkleidung
    - Verzögerte Winterausrüstung
    - Pelz- und Fellspende-Kampagne
    - Kältebedingte Ausfälle
  - **III.1b** Auswirkungen auf Waffen und Munition
    - Vereisung von Mechanismen
    - Probleme mit Schmier- und Betriebsstoffen
    - Funktionsstörungen bei Handwaffen
- **III.2** Logistische und Mobilitätsschwierigkeiten
  - **III.2a** Vereiste Straßen
    - Frühfrost und Glatteisbildung
    - Regionale Unterschiede (Nord, Mitte, Süd)
    - Tragfähigkeitsprobleme
  - **III.2b** Versorgungsengpässe
    - Blockierte Transportmittel
    - Munitionsmangel
    - Infrastrukturausfälle (Brücken, Fähren)

### IV. Fazit
- Zusammenfassung der Wirkungsketten
- Bewertung des Wettereinflusses
- Methodische Reflexion

---

## Datenanalyse und Methodik

### Verwendete Datenquellen

#### Historische Quellen
- **Kriegstagebuch des Oberkommandos der Wehrmacht, Bd. I (1965)**
- **Führerweisung Nr. 21 („Fall Barbarossa") und Folgeweisungen**
- **Kriegstagebuch-Auszüge** (Primärquellen)
- **Halder, Franz: Kriegstagebuch Band Oktober–Dezember 1941**

#### Meteorologische Daten
- **Copernicus Climate Data Store (CDS) – ERA5 Reanalyse**
  - Stündliche Daten ab 1940
  - Niederschlagsdaten (Juni–Dezember 1941)
  - Temperaturdaten (Min/Max)
  - Schneefallstatistiken
  - Windgeschwindigkeiten
  - Frosttage
- **Our World in Data** – Historische Klimadaten
- **American Meteorological Society (AMS)** – Studien zum Winter 1941/42

### Analysewerkzeuge
- **Python** – Hauptwerkzeug für Datenverarbeitung
  - pandas, numpy – Datenmanipulation
  - matplotlib, seaborn – Visualisierung
  - xarray – NetCDF/GRIB-Datenverarbeitung
- **Panoply 5.7.1** – NetCDF/GRIB Datenvisualisierung
- **XyGrib 1.2.6** – Meteorologische Kartenanalyse
- **QGIS** – Kartenerstellung

### Meteorologische Kenngrößen
Die folgenden Definitionen wurden für die Wetteranalyse verwendet:

- **Starkniederschlagstag**: Tag mit ≥10–20 mm Niederschlag in 24 Stunden
- **5-Tages-Maximum**: Höchste Niederschlagssumme innerhalb gleitender 5-Tages-Fenster
- **Frosttag**: Tag mit Tagesminimum < 0°C
- **Sturmböen**: Windgeschwindigkeiten ≥17,2 m/s (Beaufort 8)

### Erstellte Visualisierungen
- `Cumulative precipitation (mm) — Jun–Dec 1941.png`
- `Frost days — Jun–Dec 1941.png`
- `Maximum 5-day precipitation (mm in month) — Jun–Dec 1941.png`
- `Mean wind speed (m_s) — Jun–Dec 1941.png`
- `Monthly Tmin_Tmax (°C) — Jun–Dec 1941.png`
- `Standardized anomaly (z) — total precipitation (Jun–Dec 1941).png`
- `Total precipitation (mm) — Jun–Dec 1941 (Trans Central Europe).png`
- `Operationsgebiet_Karte.png` – Eigene QGIS-Kartierung

---

## Zentrale Erkenntnisse

### Wetterbedingte Faktoren nach Heeresgruppen

#### Heeresgruppe Nord (Leningrad-Front)
- **Sommer-Niederschlagsregime**: Juli/August als nasseste Monate (~78-85 mm)
- **Früher Frosteinbruch**: Bereits am 7. November 1941 starke Kälte bis -20°C
- **Eisbildung Ladogasee**: Ab 17./19. November erste Tragfähigkeit, ab 22. November Kolonnenverkehr
- **Achsengebundenheit**: Pskow-Nowgorod-Ladoga besonders empfindlich

#### Heeresgruppe Mitte (Moskau-Front)
- **Rasputiza-Effekt**: Aufweichung unbefestigter Wege im Oktober
- **Tragfrost-Fenster**: Kurzzeitig befahrbare Wege ab 13. November
- **Vereisung**: Ab 20. November flächige Glätte und Bewegungseinschränkungen
- **Operation Taifun**: Wetterbedingte Verzögerungen in kritischer Phase
- **Munitionsmangel**: Am 13. November Rücknahme der 31. I.D. um 3-4 km

#### Heeresgruppe Süd (Ukraine/Don-Front)
- **Sommerniederschläge**: ~63,5 mm Juni-August, Maximum im Juli (~69,7 mm)
- **Früher Frost im Süden**: Bereits ab 15. November -13°C tags, -22°C nachts
- **Infrastrukturprobleme**: Zerstörte Dnjepr-Brücke und Fähren bei Kiew
- **Vereiste Straßen**: Ab 21. November bei 11. Armee

### Übergreifende Wetterwirkungen
- **Rasputiza (Schlammperiode)**: Erhebliche Verzögerungen durch aufgeweichte Straßen im Oktober/November
- **Frühwinter 1941**: Ungewöhnlich früher und harter Wintereinbruch
- **Niederschläge**: Überdurchschnittliche Regenmengen im Herbst 1941
- **Temperatursturz**: Drastische Temperaturabfälle ab November 1941
- **Großwetterlage**: Persistierendes Hochdruckgebiet über Ostatlantik, Trog über Westrussland

### Militärische Auswirkungen
- **Verzögerte Angriffstermine** durch Wetterbedingungen
- **Logistische Probleme** bei der Nachschubversorgung
- **Technische Ausfälle** bei Fahrzeugen und Waffen
  - Vereisung von Verschlüssen und Optiken
  - Viskositätsprobleme bei Schmierstoffen
  - Funktionsstörungen bei K 98k, MP 38/40, MG 34
- **Gesundheitliche Belastungen** für die Truppen
  - Verspätete Winterausrüstung (erst Frühjahr 1942)
  - Kältebedingte Ausfälle
  - Requisition von Zivilkleidung (Weisung 21.12.1941)
- **Infrastrukturelle Engpässe**
  - Nur 6-8% hartgedeckte Straßen im sowjetischen Netz
  - Eisenbahnprobleme im russischen Winter

---

## Methodische Besonderheiten

### Interdisziplinärer Ansatz
Die Arbeit verbindet:
- **Militärgeschichte**: Operationsanalyse anhand von Primärquellen
- **Klimatologie**: Quantitative Wetteranalyse mit ERA5-Reanalyse
- **Geographie**: Räumliche Analyse der Operationsachsen
- **Technikgeschichte**: Waffenfunktion unter Kältebedingungen

### Transparenz und Reproduzierbarkeit
- **GitHub-Veröffentlichung**: Gesamter Code und Workflow öffentlich einsehbar
- **QGIS-Kartierung**: Eigene Operationsgebietskarte mit Legende
- **Dokumentierte Berechnungen**: Alle Schritte nachvollziehbar
- **Externe Validierung**: Abgleich mit AMS-Studien zum Winter 1941/42

### Quellenarbeit
- **Primärquellen**: Tageweise Auswertung KTB OKW
- **Führungsweisungen**: Systematische Extraktion von Datum, Ort, Zielrichtung
- **Zeitlinie**: Chronologisch konsistente operative Wendepunkte
- **Plausibilisierung**: Abgleich von KTB-Einträgen mit Wetterdaten

---

## Literaturverzeichnis (Auswahl)

### Primärquellen
- Halder, Franz: Kriegstagebuch. Band Oktober–Dezember 1941
- Hitler, Adolf: Weisung Nr. 21 für die Kriegführung („Fall Barbarossa"), 18.12.1940
- Kriegstagebuch des Oberkommandos der Wehrmacht. Bd. I (1965), OCR

### Sekundärliteratur
- Blau, George E.: German Campaign in Russia: Planning and Operations, 1940–1942 (DA Pamphlet 20-261a), 1955
- Chew, William E.: Fighting the Russians in Winter. Three Case Studies, Army University Press 1981
- Haupt, Werner: Heeresgruppe Mitte 1941–1945. Podzun-Pallas, Bad Nauheim 1966
- Stahel, David: Operation Barbarossa and Germany's Defeat in the East, Cambridge 2009
- Stahel, David: Operation Typhoon: Hitler's March on Moscow, October 1941, Cambridge 2013
- Showalter, Dennis: Hitler's Panzers: The Lightning Attacks that Revolutionized Warfare, Berkley Caliber 2009

### Meteorologische Literatur
- Copernicus Climate Change Service (C3S): ERA5 hourly data on single levels from 1940 to present
- Danilovich, Irina / Beate Geyer: Estimates of current and future climate change in Belarus, Meteorology Hydrology and Water Management 9 (1–2), 2021
- Lejenäs, Harald: The Severe Winter in Europe 1941–42: The Large-scale Circulation, Cut-off Lows, and Blocking, BAMS 70(3), 1989
- Jevrejeva, S. / Leppäranta, M. / Moore, J.C.: Baltic Sea ice seasons in the twentieth century, Climate Research 25, 2004

### Technische Dokumentation
- U.S. War Department: Special Series No. 14: German Infantry Weapons, 1943
- Department of the Army: Field Manual FM 31-70: Basic Cold Weather Manual, 1968
- U.S. Army Center of Military History: Military Improvisations During the Russian Campaign, 1986

### Datenquellen
- Copernicus Climate Change Service (C3S) Climate Data Store
- Our World in Data – Historical Weather Database
- Deutscher Wetterdienst: Klimadiagramme
- CIA: Highway Transport in the USSR (1952)

---

## Technische Voraussetzungen

### Software-Installation
```bash
# Panoply (bereits im Projekt enthalten)
./installation/PanoplyWin-5.7.1/PanoplyWin/Panoply.exe

# XyGrib (Installer vorhanden)
./installation/XyGrib_Win_Offline_Installer_v1.2.6.exe

# QGIS
# Download von qgis.org
```

### Python-Umgebung
```bash
# Erforderliche Pakete
pip install pandas numpy matplotlib seaborn xarray netCDF4 cartopy

# Jupyter Notebook (optional)
pip install jupyter
```

### Datenformate
- **GRIB/NetCDF**: Meteorologische Rohdaten (ERA5)
- **CSV**: Tabellarische Auswertungen
- **PDF**: Historische Dokumente
- **PNG**: Visualisierungen und Karten
- **Shapefile**: Geografische Vektordaten (QGIS)

---

## Verwendung der Analysedaten

### Workflow Wetterdatenanalyse
1. **Datenakquise**: Download von ERA5-Daten aus Copernicus CDS
2. **Plausibilisierung**: Prüfung auf Vollständigkeit und Konsistenz
3. **Indikatorberechnung**: Frosttage, Niederschlagssummen, etc.
4. **Räumliche Aggregation**: Mittelwerte entlang Operationsachsen
5. **Zeitreihenanalyse**: Juni-Dezember 1941
6. **Visualisierung**: Karten, Zeitreihen, Hovmöller-Diagramme
7. **Korrelation**: Abgleich mit KTB-Einträgen

### Beispiel-Workflow
```python
# Vereinfachtes Beispiel für Datenverarbeitung
import xarray as xr
import pandas as pd
import matplotlib.pyplot as plt

# Lade ERA5-Daten
ds = xr.open_dataset('raw/copernicus/era5_1941_precipitation.nc')

# Definiere Untersuchungsgebiet
lat_slice = slice(60, 45)  # 45°N bis 60°N
lon_slice = slice(15, 45)  # 15°E bis 45°E

# Extrahiere Teilgebiet
data = ds.sel(latitude=lat_slice, longitude=lon_slice)

# Berechne tägliche Summen
daily_precip = data['tp'].resample(time='1D').sum()

# Zeitliche Auswertung
time_series = daily_precip.mean(dim=['latitude', 'longitude'])

# Visualisierung
plt.figure(figsize=(12, 6))
time_series.plot()
plt.title('Niederschlag während Operation Barbarossa 1941')
plt.xlabel('Datum')
plt.ylabel('Niederschlag (mm)')
plt.grid(True)
plt.savefig('analysis/precipitation_timeseries.png', dpi=300)
plt.show()
```

### Frosttage-Berechnung
```python
import xarray as xr

# Lade Temperatur-Minimaldaten
ds = xr.open_dataset('raw/copernicus/era5_1941_t2m_min.nc')

# Definiere Frosttag (Tmin < 0°C = 273.15 K)
frost_days = (ds['t2m'] < 273.15).sum(dim='time')

# Visualisierung
frost_days.plot(cmap='Blues')
plt.title('Frosttage Juni–Dezember 1941')
plt.savefig('analysis/frost_days_map.png', dpi=300)
```

---

## Forschungsbeitrag

Diese Arbeit leistet einen Beitrag zur:
- **Militärgeschichtsforschung**: Interdisziplinäre Analyse von Wetter und Kriegsführung unter Berücksichtigung aller drei Heeresgruppen
- **Klimageschichte**: Quantitative Rekonstruktion der Wetterbedingungen 1941 in Osteuropa mit modernen Reanalysedaten
- **Methodenentwicklung**: Kombination historischer Primärquellen und meteorologischer Datenanalyse
- **Technikgeschichte**: Funktionsweise von Waffen und Fahrzeugen unter Extrembedingungen

---

## Zentrale Ergebnisse

### Operative Wendepunkte
1. **Juli 1941**: Erste operative Umpriorisierungen (Weisungen 33/34)
2. **Oktober 1941**: Einsetzen der Rasputiza, massive Bewegungseinschränkungen
3. **7.-12. November 1941**: Tragfrost-Fenster, kurzzeitig verbesserte Verhältnisse
4. **Ab 20. November 1941**: Flächige Vereisung, Ende der Beweglichkeit
5. **Dezember 1941**: Sowjetische Gegenoffensive bei anhaltender Kälte

### Wirkungsketten
```
Nässe/Regen → Aufweichung unbefestigter Wege → Bewegungsstockungen → 
Versorgungsverzögerungen → Operative Einschränkungen

Frühfrost → Kurzzeitige Tragfähigkeit → Fortsetzung der Operationen → 
Flächige Vereisung → Endgültiger Stillstand

Kälte + fehlende Winterausrüstung → Kältebedingte Ausfälle → 
Verminderte Kampfkraft → Defensive Lage
```

### Regionale Differenzierung
Die Arbeit zeigt, dass die drei Heeresgruppen unterschiedlich stark und zu unterschiedlichen Zeitpunkten von Wetterfaktoren betroffen waren:

- **Nord**: Frühe Kälte, frühe Eisbildung, Achsengebundenheit
- **Mitte**: Rasputiza-Effekt in kritischer Operationsphase (Taifun)
- **Süd**: Früher Frost, Infrastrukturprobleme (Brücken/Fähren)

---

## Kontakt und Veröffentlichung

**Lennard Gross**  
W-Seminar Geschichte 2024/2026  
Otto-von-Taube-Gymnasium  

**Seminarleiter:** Sebastian Weber

### GitHub-Repository
Das vollständige Projekt mit allen Skripten, Daten und Visualisierungen ist verfügbar unter:
- GitHub: [WSeminar – Lennard Gross](https://github.com/lennardgross)

---

## Lizenz und Nutzung

Dieses Projekt dient ausschließlich wissenschaftlichen und pädagogischen Zwecken im Rahmen des W-Seminars am Otto-von-Taube-Gymnasium.

### Datenquellen-Attribution
- Meteorologische Daten: © Copernicus Climate Change Service (ERA5)
- Historische Quellen: Verschiedene Archive (siehe Literaturverzeichnis)
- Basiskarten: © OpenStreetMap contributors, Natural Earth
- QGIS: Open Source Geospatial Foundation

### Zitiervorschlag
```
Gross, Lennard (2025): Wetter als Kriegsfaktor: Der gescheiterte Vormarsch 
der Heeresgruppen 1941. W-Seminar Geschichte, Otto-von-Taube-Gymnasium. 
GitHub: https://github.com/lennardgross/WSeminar
```

---

## Projektstand

- Literaturrecherche abgeschlossen
- Datensammlung und -aufbereitung
- Visualisierungen erstellt
- Kapitelerstellung abgeschlossen
- Endfassung und Formatierung

**Abgabe:** 26.11.2025
**Letztes Update:** November 2025

---

## Anhang

### Abbildungsverzeichnis
- Abbildung A.1: Karte des Operationsgebiets mit Stoßrichtungen
- Abbildung B.1: Monatsanomalien Juni–Dezember 1941
- Abbildung B.2a/b: Frequenz feuchter Tage
- Abbildung B.3: Maximale 5-Tages-Niederschlagssumme
- Abbildung B.4: Domain-Mittel der Regenrate
- Abbildung B.5: Zeitmittel der Regenrate
- Abbildung B.6a/b: Hovmöller-Diagramme
- Abbildung B.7: Korrelation Druckgradient-Windgeschwindigkeit

### Tabellenverzeichnis
- Tabelle 1: Übersicht Führerweisungen Juni–September 1941
- Tabelle 2: KTB-Einträge zu Wetterbedingungen November 1941
- Tabelle 3: Regionale Klimakennzahlen Heeresgruppen-Operationsräume

---

**Hinweis**: Dieses Projekt behandelt ein Thema mit hoher historischer Sensibilität. Die Arbeit dient ausschließlich der wissenschaftlichen Aufarbeitung und steht in keiner Weise in Verbindung mit einer Glorifizierung oder Verharmlosung der NS-Verbrechen und des Vernichtungskriegs gegen die Sowjetunion.