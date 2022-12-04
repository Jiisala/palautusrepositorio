#Refaktoroida olisi voinut vielä lisää, mutta pyrin säilyttämään alkuperäisen tehtävän annon vaatimukset.
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
        taulu = [0] * self.alkioiden_lkm

        for i in range(0, len(taulu)):
            taulu[i] = self.lukujono[i]

        return taulu

    @staticmethod
    def yhdiste(a, b):
        x = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            x.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            x.lisaa(b_taulu[i])

        return x

    @staticmethod
    def leikkaus(a, b):
        y = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            for j in range(0, len(b_taulu)):
                if a_taulu[i] == b_taulu[j]:
                    y.lisaa(b_taulu[j])

        return y

    @staticmethod
    def erotus(a, b):
        int_joukko = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            int_joukko.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            int_joukko.poista(b_taulu[i])

        return int_joukko

    def __str__(self):
        return f"\u007b{', '.join(map(str, self.lukujono))}\u007d"
