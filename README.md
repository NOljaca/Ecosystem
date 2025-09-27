# Ökosystem-Simulation

**Autor**: Nikola Oljaca  
**Projektname**: Ecosystem Simulation Program  
**Sprache**: Python 3.x

---

## 1. Einleitung

Dieses Projekt implementiert eine Simulation eines Ökosystems mit Pflanzen- und Tierpopulationen unter Verwendung objektorientierter Programmierung in Python.  
Die Simulation umfasst:

- Verschiedene Pflanzenarten  
- Pflanzenfresser  
- Allesfresser  
- Fleischfresser  

Die Arten interagieren miteinander über Mechanismen wie Wachstum, Ernährung, Fortpflanzung und Sterblichkeit.

---

## 2. GitHub-Repository

Das vollständige Projekt befindet sich unter:  
[https://github.com/NOljaca/Ecosystem](https://github.com/NOljaca/Ecosystem)

---

## 3. Hauptdatei

Die zentrale Datei für die Simulation ist:


---

## 4. Klassenübersicht

- **Ecosystem**  
  Verwaltet die Anzahl der Simulationsrunden und den Ablauf der gesamten Simulation.

- **Habitat**  
  Repräsentiert einen Lebensraum mit Eigenschaften wie Größe und Reproduktionsfaktor.

- **Pflanzenarten (Pflanzenart1, Pflanzenart2, Pflanzenart3)**  
  Repräsentieren unterschiedliche Pflanzen mit Methoden wie `grow()`, `age()` und `die()`.

- **Pflanzen**  
  Sammlung von Pflanzenobjekten, mit Methoden zum Hinzufügen und Iterieren.

- **Tierklassen:**
  - Pflanzenfresser  
  - Allesfresser  
  - Fleischfresser  
  Diese Klassen enthalten das Verhalten für Ernährung, Fortpflanzung, Altern und Sterben.

- **Tierlisten:**
  - Pflanzenfresserliste  
  - Allesfresserliste  
  - Fleischfresserliste  
  Diese Klassen verwalten Sammlungen von Tierobjekten.

---

## 5. Installation und Ausführung

### Voraussetzungen

- Python 3.x
- Keine externen Abhängigkeiten (nur Standardbibliotheken)

### Ausführung

1. Speichere den Code als:


2. Starte die Simulation im Terminal:

```bash
python Ecosystem_Simulation_Program.py
