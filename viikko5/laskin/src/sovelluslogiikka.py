#Sovelluksen kumoa logiikka on toteutettu hieman eri lailla kuin tehtävässä ohjeistettiin.
#Sen sijaan että olisin toteuttanut jokaiselle Luokalle oman kumoa metodinsa, tallensin edellisen tuloksen
#suoraan sovelluslogiikkaan ja toteutin kumoa metodin sinne (vaihda tulokset metodi). 
#henkilökohtaisesti olen sitä mieltä että se oli loogisempi toteutus, 
#mutta olen valmis keskustelemaan asiasta ja haastamaan näkemykseni.

class Sovelluslogiikka:
    def __init__(self, tulos=0):
        self.tulos = tulos
        self.edellinen_tulos = 0
    
    def muista_edelinen_tulos(self):
        self.edellinen_tulos = self.tulos
    
    def vaihda_tulokset(self):
        self.tulos, self.edellinen_tulos = self.edellinen_tulos, self.tulos

class Summa:
    
    def __init__(self, sovellus, io):
        
        self.sovellus = sovellus 
        self.io = io

    def suorita(self):
        if self.io():
            self.sovellus.muista_edelinen_tulos()        
            self.sovellus.tulos += int(self.io())

class Erotus:
    
    def __init__(self, sovellus, io):
        self.sovellus = sovellus 
        self.io = io

    def suorita(self):
        if self.io():
            self.sovellus.muista_edelinen_tulos()
            self.sovellus.tulos -= int(self.io())

class Nollaus:
    
    def __init__(self, sovellus):
        self.sovellus = sovellus 
        
    def suorita(self):
        self.sovellus.muista_edelinen_tulos()    
        self.sovellus.tulos = 0

class Kumoa:
    
    def __init__(self, sovellus):
        self.sovellus = sovellus 

    def suorita(self):        
        self.sovellus.vaihda_tulokset()
