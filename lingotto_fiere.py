from espositore import Espositore
from stand import Stand, StandPreseExtra, StandPremium


class LingottoFiere:
    def __init__(self, nome):
        """Inizializza gli attributi e le strutture dati"""
        # TODO
        self.__nome = nome
        self.stands = []
        self.espositori = []
        self.assegnazioni = []

    """Aggiungere setter e getter se necessari"""
    # TODO
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nuovo_nome):
        self.__nome = nuovo_nome

    def carica_file_dati(self, file_path):
        """Carica i dati (stand ed espositori) dal file"""
        # TODO
        from csv import reader
        with open(file_path) as csv_file:
            csv_reader = reader(csv_file)

            for i, line in enumerate(csv_reader):

                codice = line[0].strip()

                if str(codice[:2].upper()) == "ST":
                    superficie = line[1].strip()
                    padiglione = line[2].strip()
                    prezzo = line[3].strip()
                    if len(line) > 4:
                        extra = line[4].strip()
                        if extra.isdigit():
                            stand = StandPreseExtra(codice, superficie, padiglione, prezzo, extra)
                        else:
                            stand = StandPremium(codice, superficie, padiglione, prezzo, extra)
                    else:
                        stand = Stand(codice, superficie, padiglione, prezzo)
                    self.stands.append(stand)

                elif str(codice[:2].upper()) == "ES":
                    nome = line[1].strip()
                    cognome = line[2].strip()
                    espositore = Espositore(codice, nome, cognome)
                    self.espositori.append(espositore)



    def assegna_stand_a_espositore(self, codice_stand, codice_espositore):
        """Associa uno stand a un espositore"""
        # TODO
        #verifico che espositore e stand esistono
        stand_esiste = None
        espositore_esiste = None
        for stand in self.stands:
            if stand.codice == codice_stand:
                stand_esiste = stand
        if stand_esiste is None:
            raise Exception(f"Codice {codice_stand} non è registrato")

        for espositore in self.espositori:
            if espositore.codice == codice_espositore:
                espositore_esiste = espositore
        if espositore_esiste is None:
            raise Exception(f"Codice {codice_espositore} non è registrato")

        #controllo che non siano già stati assegnati
        if stand_esiste.espositore is not None:
            raise Exception(f"Lo stand selezionato è già stato assegnato a {stand_esiste.espositore}")

        if espositore_esiste.stand is not None:
            raise Exception(f"L'espositore selezionato è già allo stand {espositore_esiste.stand}")

        # assegno i valori dopo aver passato i controlli
        stand_esiste.espositore = espositore_esiste
        espositore_esiste.stand = stand_esiste


    def elenca_espositori(self):
        """Stampa l'elenco degli espositori mostrando, per ognuno, lo stand a cui è associato, quando applicabile """
        # TODO
        for espositore in self.espositori:
            if espositore.stand is not None:
                print(f"{espositore.codice} si trova in {espositore.stand.codice}")
            else:
                print(f"{espositore.codice} non è assegnato ad alcuno stand")


    def stand_ordinati_per_prezzo(self):
        """Restituisce la lista ordinata degli stand in base al prezzo"""
        # TODO
        return sorted(self.stands)