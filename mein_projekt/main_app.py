from kunden_sys import KundenManager
from kunden_sys.daten import Kunde


# Manager erstellen
manager = KundenManager()

# Kunden erstellen
kunde1 = Kunde(101, "Max Mustermann", "max@example.com")
kunde2 = Kunde(102, "Erika Musterfrau", "erika@example.com")

# Kunden hinzufügen
manager.add_kunde(kunde1)
manager.add_kunde(kunde2)

# Kunden ausgeben
for kunde in manager.kunden:
    print(kunde.zeige_info())