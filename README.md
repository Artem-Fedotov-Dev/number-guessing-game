Zahlenratespiel (Guess the Number)

Ein interaktives Konsolenspiel, das in Python geschrieben wurde. Dieses Projekt wurde zur
Festigung der Programmiergrundlagen entwickelt, fuer den deutschen Sprachraum
lokalisiert und mit einem dynamischen Scoring-System erweitert.

Funktionen
- Robuste Validierung: Das Programm faengt ungueltige Benutzereingaben (Buchstaben,
- Sonderzeichen oder Zahlen ausserhalb des Bereichs) komplett ab, ohne
- abzustuerzen.

- Flexibler Zahlenbereich: Der Spieler kann waehlen, ob er im Standardbereich (1-100)
- oder in einem selbst definierten Bereich spielen möchte.

- Mathematisches Scoring-System: Das Spiel berechnet dynamisch das
- informationstheoretische Optimum an Versuchen (mittels dualem Logarithmus
- math.log2).

- Geometrischer Bonus: Schlaegt der Spieler die mathematisch perfekte Strategie des
- Computers, erhaelt er einen progressiven Punktebonus basierend auf einer
- geometrischen Folge.

- Intelligente Eingabeverarbeitung: Gross-/Kleinschreibung sowie versehentliche
- Leerzeichen bei der "Ja/Nein"-Abfrage werden automatisch normalisiert
- (.strip().lower()).

Technologien

- Python 3.x
- random Modul (fuer die Generierung der Geheimzahl)
- math Modul (fuer die Berechnung des Algorithmus-Optimums)

Installation und Start

1. Repository klonen:
  git clone github.com
2. Das Spiel im Terminal ausführen:
   python main.py
