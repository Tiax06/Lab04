class Stand:
    def __init__(self, codice, superficie, padiglione, prezzo):
        self.codice = codice
        self.superficie = float(superficie)
        self.padiglione = padiglione
        self.prezzo = float(prezzo)
        self.espositore = None

    def prezzo_finale(self):
        return self.prezzo

    def __str__(self):
        if self.espositore is None:
            condizione = "Disponibile"
        else:
            condizione = "Occupato"
        return f"{self.codice}: Standard | {self.superficie} mq - Padiglione {self.padiglione} - Prezzo {self.prezzo_finale()}€ - {condizione}"

    def __lt__(self, other):
        return self.prezzo_finale() < other.prezzo_finale()

    def __eq__(self, other):
        if isinstance(other, Stand):
            return self.codice == other.codice
        if isinstance(other, str):
            return self.codice == other
        return False



class StandPreseExtra(Stand):
    def __init__(self, codice, superficie, padiglione, prezzo, prese):
        super().__init__(codice, superficie, padiglione, prezzo)
        self.prese = int(prese)

    def prezzo_finale(self):
        return self.prezzo * (1 + 0.07 * self.prese)

    def __str__(self):
        if self.espositore is None:
            condizione = "Disponibile"
        else:
            condizione = "Occupato"
        return f"{self.codice}: Prese Extra | {self.superficie} mq - Padiglione {self.padiglione} - Prezzo {self.prezzo_finale()}€ - Prese aggiuntive: {self.prese} - {condizione}"



class StandPremium(Stand):
    def __init__(self, codice, superficie, padiglione, prezzo, posizione):
        super().__init__(codice, superficie, padiglione, prezzo)
        self.posizione = posizione

    def prezzo_finale(self):
        return self.prezzo * 1.30

    def __str__(self):
        if self.espositore is None:
            condizione = "Disponibile"
        else:
            condizione = "Occupato"
        return f"{self.codice}: Premium | {self.superficie} mq - Padiglione {self.padiglione} - Prezzo {self.prezzo_finale()}€ - Posizione: {self.posizione} - {condizione}"