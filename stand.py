class StandStandard:
    def __init__(self, codice, n1, n2, n3):
        self.codice = codice
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3


    def __str__(self):
        return f"{self.codice} {self.n1} {self.n2} {self.n3}"


class StandPremium(StandStandard):
    def __init__(self, codice, n1, n2, n3, preseextra):
        self.codice = codice
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3
        self.preseextra = preseextra

    def __str__(self):
        return f"{self.codice} {self.n1} {self.n2} {self.n3} {self.preseextra}"
