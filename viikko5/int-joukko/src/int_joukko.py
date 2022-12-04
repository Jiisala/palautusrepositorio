#Refaktoroida olisi voinut vielä lisää, mutta pyrin säilyttämään alkuperäisen tehtävän vaatimukset.
#Paljon siistimpi kuin lähtötilanne kuitenkin. 

KAPASITEETTI = 5
OLETUSKASVATUS = 5

class IntJoukko:
    def __init__(self, kapasiteetti=KAPASITEETTI, kasvatuskoko=OLETUSKASVATUS):
                            
        if not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("Epäkelpo kapasiteetti")  
        else:
            self.kapasiteetti = kapasiteetti
       
        if not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("Epäkelpo kasvatuskoko")  
        else:
            self.kasvatuskoko = kasvatuskoko

        self.lukujono = [0] * self.kapasiteetti
        self.alkioiden_lkm = 0

    def kuuluu(self, n):
        return n in self.lukujono 

        
    def lisaa(self, n):

        if not self.kuuluu(n):
            self.lukujono[self.alkioiden_lkm] = n
            self.alkioiden_lkm += 1

            if self.alkioiden_lkm == len(self.lukujono):
                lukujono_vanha = self.lukujono
                self.lukujono = [0] * (self.alkioiden_lkm + self.kasvatuskoko)
                self.kopioi_taulukko(lukujono_vanha, self.lukujono)

            return True

        return False

    def poista(self, n):
        if self.kuuluu(n):
                
            kohta = self.lukujono.index(n)
            self.alkioiden_lkm -= 1
            for i in range(kohta, len(self.lukujono)-1):
                self.lukujono[i] = self.lukujono[i+1]
            self.lukujono[-1] = 0
            return True

        return False

    def kopioi_taulukko(self, a, b):
        for i in range(0, len(a)):
            b[i] = a[i]

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        uusi_lukujono = []

        for i in range(0, self.alkioiden_lkm):
            uusi_lukujono.append(self.lukujono[i])

        return uusi_lukujono

    @staticmethod
    def yhdiste(a, b):
        yhdiste_lukujono = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            yhdiste_lukujono.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            yhdiste_lukujono.lisaa(b_taulu[i])

        return yhdiste_lukujono

    @staticmethod
    def leikkaus(a, b):
        leikkaus_lukujono = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            for j in range(0, len(b_taulu)):
                if a_taulu[i] == b_taulu[j]:
                    leikkaus_lukujono.lisaa(b_taulu[j])

        return leikkaus_lukujono

    @staticmethod
    def erotus(a, b):
        erotus_lukujono = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            erotus_lukujono.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            erotus_lukujono.poista(b_taulu[i])

        return erotus_lukujono

    def __str__(self):
                return f"\u007b{', '.join(map(str, self.lukujono[:self.alkioiden_lkm]))}\u007d"