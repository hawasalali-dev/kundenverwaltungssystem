# kundenverwaltungssystem
<img width="4032" height="1490" alt="grafik" src="https://github.com/user-attachments/assets/3875b44a-e7d4-41bd-a3eb-edadc42d1cd5" />

mein_projekt/ ├── main_app.py └── kunden_sys/ ├── init.py ├── daten.py └── logik.py


## Module ### daten.py Enthält die Klasse `Kunde`. Attribute: - kunden_id - name - email Methode: - `zeige_info()` → Gibt die Kundendaten als lesbaren String zurück. ### logik.py Enthält die Klasse `KundenManager`. Methoden: - `add_kunde(kunde)` → Fügt einen Kunden zur Kundenliste hinzu. ### __init__.py Ermöglicht den direkten Import von `KundenManager` über das Package: ```python from kunden_sys import KundenManager
