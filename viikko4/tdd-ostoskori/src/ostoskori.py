from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote

        self.sisalto = {}

    def tavaroita_korissa(self):
        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2 
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2 

        maara = 0
        for value in self.sisalto.values():
            maara += value.lukumaara()
        return maara
        
    def hinta(self):
        hinta = 0
        print (self.sisalto.values())
        for ostos in self.sisalto.values():
            print ("pok")
            hinta += ostos.hinta()
        return hinta
    
        # kertoo korissa olevien ostosten yhteenlasketun hinnan

    def lisaa_tuote(self, lisattava: Tuote):
        
        if lisattava.nimi not in self.sisalto.keys():
            self.sisalto[lisattava.nimi] = Ostos(lisattava)
        else:
            self.sisalto[lisattava.nimi].muuta_lukumaaraa(1)
            
    def poista_tuote(self, poistettava: Tuote):
        # poistaa tuotteen
        self.sisalto[poistettava.nimi].muuta_lukumaaraa(-1)
        if self.sisalto[poistettava.nimi].lukumaara() == 0:
            self.sisalto.pop(poistettava.nimi)
        

    def tyhjenna(self):
        pass
        # tyhjentää ostoskorin

    def ostokset(self):
        
        return list(self.sisalto.values())
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
