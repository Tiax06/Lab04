class Assegnazione:
    def __init__(self, codice_stand, codice_espositore):
        self.codice_stand = codice_stand
        self.codice_espositore = codice_espositore

    def __str__(self):
        return f"{self.codice_stand} {self.codice_espositore}"
