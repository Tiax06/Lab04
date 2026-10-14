from espositore import Espositore
from stand import StandStandard, StandPremium
from assegnazione import Assegnazione

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

    def carica_file_dati(self, file_path):
        """Carica i dati (stand ed espositori) dal file"""
        # TODO
        from csv import reader
        with open(file_path) as csv_file:
            csv_reader = reader(csv_file)

            for i, line in enumerate(csv_reader):
                if i == 0:
                    continue

                codice = line[0]

                if str(codice[:2].upper()) == "ST":
                    n1 = line[1]
                    n2 = line[2]
                    n3 = line[3]
                    if len(line) > 4:
                        prese = line[4]
                        stand = StandPremium(codice, n1, n2, n3, prese)
                    else:
                        stand = StandStandard(codice, n1, n2, n3)
                    self.stands.append(stand)

                elif str(codice[:2].upper()) == "ES":
                    nome = line[1]
                    cognome = line[2]
                    espositore = Espositore(codice, nome, cognome)
                    self.espositori.append(espositore)



    def assegna_stand_a_espositore(self, codice_stand, codice_espositore):
        """Associa uno stand a un espositore"""
        # TODO
        # Quando viene effettuata una richiesta, il sistema deve verificare che lo stand e
        # l'espositore esistano, che lo stand sia effettivamente disponibile e che l'espositore
        # non sia già associato a un altro stand. Ogni stand deve mantenere un riferimento all'espositore
        # a cui è stato assegnato. Se tutte le condizioni sono soddisfatte, lo stand viene contrassegnato
        # come non disponibile e viene registrata l'associazione tra espositore e stand.
        controllo1 = False
        controllo2 = False
        for stand in self.stands:
            if stand == codice_stand:
                controllo1 = True
        for espositore in self.espositori:
            if espositore == codice_espositore:
                controllo2 = True


        # da qui in poi potrebbe essere giusta la soluzione ma è sbagliata rispetto al testo dell'esercizio
        condizione = True
        if controllo1 and controllo2:
            for codici in self.assegnazioni:
                if codici == codice_stand or codici == codice_espositore:
                    condizione = False

            if condizione:
                assegno = Assegnazione(codice_stand, codice_espositore)
                self.assegnazioni.append(assegno)
            else:
                return f"stand non disponibile"






    def elenca_espositori(self):
        """Stampa l'elenco degli espositori mostrando, per ognuno, lo stand a cui è associato, quando applicabile """
        # TODO

    def stand_ordinati_per_prezzo(self):
        """Restituisce la lista ordinata degli stand in base al prezzo"""
        # TODO
