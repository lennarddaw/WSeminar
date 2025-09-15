# Wetter als Kriegsfaktor: Der gescheiterte Vormarsch der Heeresgruppe Mitte 1941

## Projektübersicht

**W-Seminar Arbeit aus dem Fach Geschichte**  
**Oberstufenjahrgang 2024/2026**  
**Otto-von-Taube-Gymnasium**

### Forschungsfrage
> Inwiefern beeinflussten klimatische und geografische Bedingungen den Vormarsch der Heeresgruppe Mitte im Rahmen des deutschen Angriffs auf die Sowjetunion im Jahr 1941?

### Projektinformationen
- **Verfasser:** Lennard Gross
- **Seminarleiter:** Sebastian Weber
- **Kurztitel:** Wetter als Kriegsfaktor: Der gescheiterte Vormarsch der Heeresgruppe Mitte 1941
- **Zeitraum:** 2024-2026

---

## Zielsetzung

Diese Seminararbeit untersucht den Einfluss meteorologischer und geografischer Faktoren auf den militärischen Verlauf der Operation Barbarossa, speziell den Vormarsch der Heeresgruppe Mitte 1941. Durch die Kombination historischer Quellen mit modernen Wetterdatenanalysen wird eine interdisziplinäre Herangehensweise verfolgt.

---

## Projektstruktur

```
C:\WSeminar/
├── analysis/           # Wetteranalysen und Visualisierungen
│   ├── video/            # Animationen der Wetterdaten
│   └── *.png             # Diagramme und Karten
├──  installation/       # Software-Tools
│   ├── PanoplyWin-5.7.1/ # Wettervisualisierung
│   └── XyGrib/           # GRIB-Dateien Viewer
├── parts/             # Kapitel der Seminararbeit
├── raw/               # Rohdaten
│   ├── coperinicus/      # Copernicus Climate Data Store
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

### II. Strategische Ausgangslage der Heeresgruppe Mitte bis Juni 1941
- **II.1** Zielsetzung bis Herbst 1941
- **II.2** Auswirkungen der Schlammperiode („Rasputiza")

### III. Wetterbedingte Herausforderungen nach dem Herbst 1941
- **III.1** Auswirkungen auf die Soldaten der Wehrmacht
  - **III.1a** Fehlende Winterkleidung
  - **III.1b** Auswirkungen auf Waffen und Munition
- **III.2** Logistische und Mobilitätsschwierigkeiten
  - **III.2a** Vereiste Straßen
  - **III.2b** Versorgungsengpässe

### IV. Verlauf der Winteroffensive 1941
- **IV.1** Sowjetische Gegenoffensive und Reserven
- **IV.2** Sowjetische Verluste durch das Wetter

### V. Folgen der Winteroffensive für die Heeresgruppe Mitte

---

##  Datenanalyse und Methodik

### Verwendete Datenquellen

#### Historische Quellen
- **Kriegstagebuch des Oberkommandos der Wehrmacht, Bd. I (1965)**
- **Kriegstagebuch-Auszüge 644-1109** (Primärquellen)
- **Halder, Franz: Kriegstagebuch Band Oktober–Dezember 1941**

#### Meteorologische Daten
- **Copernicus Climate Data Store (CDS)**
  - Niederschlagsdaten (1941)
  - Temperaturdaten (Min/Max)
  - Schneefallstatistiken
  - Windgeschwindigkeiten
- **Our World in Data** - Historische Klimadaten

### Analysewerkzeuge
- **Panoply 5.7.1** - NetCDF/GRIB Datenvisualisierung
- **XyGrib 1.2.6** - Meteorologische Kartenanalyse
- **Python Scripts** - Datenverarbeitung und -analyse

### Erstellte Visualisierungen
- `Cumulative precipitation (mm) — Jun–Dec 1941.png`
- `Frost days — Jun–Dec 1941.png`
- `Maximum 5‑day precipitation (mm in month) — Jun–Dec 1941.png`
- `Mean wind speed (m_s) — Jun–Dec 1941.png`
- `Monthly Tmin_Tmax (°C) — Jun–Dec 1941.png`
- `Standardized anomaly (z) — total precipitation (Jun–Dec 1941).png`
- `Total precipitation (mm) — Jun–Dec 1941 (Trans Central Europe).png`

---

## Zentrale Erkenntnisse

### Wetterbedingte Faktoren
- **Rasputiza (Schlammperiode)**: Erhebliche Verzögerungen durch aufgeweichte Straßen
- **Frühwinter 1941**: Ungewöhnlich früher und harter Wintereinbruch
- **Niederschläge**: Überdurchschnittliche Regenmengen im Herbst 1941
- **Temperatursturz**: Drastische Temperaturabfälle ab November 1941

### Militärische Auswirkungen
- Verzögerte Angriffstermine durch Wetterbedingungen
- Logistische Probleme bei der Nachschubversorgung
- Technische Ausfälle bei Fahrzeugen und Waffen
- Gesundheitliche Belastungen für die Truppen

---

## Literaturverzeichnis (Auswahl)

### Primärquellen
- Halder, Franz: Kriegstagebuch. Band Oktober–Dezember 1941
- Kriegstagebuch des Oberkommandos der Wehrmacht. Bd. I (1965), OCR

### Sekundärliteratur
- Haupt, Werner: Heeresgruppe Mitte 1941–1945. Podzun-Pallas, Bad Nauheim 1966
- Stahel, David: Operation Typhoon: Hitler's March on Moscow, October 1941, New York, NY: Cambridge University Press, 2013
- Showalter, Dennis: Hitler's Panzers: The Lightning Attacks that Revolutionized Warfare, New York: Berkley Caliber, 2009

### Datenquellen
- Copernicus Climate Change Service (C3S) Climate Data Store
- Our World in Data - Historical Weather Database

---

## Technische Voraussetzungen

### Software-Installation
```bash
# Panoply (bereits im Projekt enthalten)
./installation/PanoplyWin-5.7.1/PanoplyWin/Panoply.exe

# XyGrib (Installer vorhanden)
./installation/XyGrib_Win_Offline_Installer_v1.2.6.exe
```

### Datenformate
- **GRIB**: Meteorologische Rohdaten
- **NetCDF**: Klimadatenanalyse
- **CSV**: Tabellarische Auswertungen
- **PDF**: Historische Dokumente

---

## Verwendung der Analysedaten

### Auswertung der Wetterdaten
1. **Laden der GRIB-Dateien** in Panoply
2. **Zeitreihenanalyse** für Juni-Dezember 1941
3. **Geografische Visualisierung** der Wetteranomalien
4. **Korrelation** mit historischen Ereignissen

### Beispiel-Workflow
```python
# Vereinfachtes Beispiel für Datenverarbeitung
import pandas as pd
import matplotlib.pyplot as plt

# Lade Wetterdaten
weather_data = pd.read_csv('raw/coperinicus/csv/Total_precipitation_surface_1_Hour_Accumulation.csv')

# Analysiere kritische Perioden
critical_periods = weather_data[
    (weather_data['date'] >= '1941-06-01') & 
    (weather_data['date'] <= '1941-12-31')
]

# Erstelle Visualisierung
plt.plot(critical_periods['date'], critical_periods['precipitation'])
plt.title('Niederschlag während Operation Barbarossa 1941')
plt.xlabel('Datum')
plt.ylabel('Niederschlag (mm)')
plt.show()
```

---

## Forschungsbeitrag

Diese Arbeit leistet einen Beitrag zur:
- **Militärgeschichtsforschung**: Interdisziplinäre Analyse von Wetter und Kriegsführung
- **Klimageschichte**: Rekonstruktion der Wetterbedingungen 1941 in Osteuropa
- **Methodenentwicklung**: Kombination historischer und meteorologischer Datenanalyse

---

## Kontakt

**Lennard Gross**  
W-Seminar Geschichte 2024/2026  
Otto-von-Taube-Gymnasium  

**Betreuer:** Sebastian Weber

---

## Lizenz und Nutzung

Dieses Projekt dient ausschließlich wissenschaftlichen und pädagogischen Zwecken im Rahmen des W-Seminars am Otto-von-Taube-Gymnasium.

### Datenquellen-Attribution
- Meteorologische Daten: © Copernicus Climate Change Service
- Historische Quellen: Verschiedene Archive (siehe Literaturverzeichnis)

---

## Projektstand

-  Literaturrecherche abgeschlossen
-  Datensammlung und -aufbereitung
-  Visualisierungen erstellt
-  Kapitelerstellung (laufend)
-  Endfassung und Formatierung

**Letztes Update:** September 2025
