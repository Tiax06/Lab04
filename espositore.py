class Espositore:
    def __init__(self, codice, nome, cognome):
        self.codice = codice
        self.nome = nome
        self.cognome = cognome
        self.stand = None

    def __str__(self):
        return f"{self.codice} {self.nome}, {self.cognome}"

    def __eq__(self, other):
        if isinstance(other, Espositore):
            return self.codice == other.codice
        if isinstance(other, str):
            return self.codice == other
        return False