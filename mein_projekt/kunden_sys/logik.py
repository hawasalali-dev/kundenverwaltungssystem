from .daten import Kunde


class KundenManager:
    def __init__(self):
        self.kunden = []

    def add_kunde(self, kunde):
        if isinstance(kunde, Kunde):
            self.kunden.append(kunde)
        else:
            raise TypeError("Es können nur Kunde-Objekte hinzugefügt werden.")