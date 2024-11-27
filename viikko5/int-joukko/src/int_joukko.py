KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    def _luo_lista(self, koko):
        """Luo uuden listan, jonka koko on määritetty."""
        return [0] * koko

    def __init__(self, kapasiteetti=KAPASITEETTI, kasvatuskoko=OLETUSKASVATUS):
        if not isinstance(kapasiteetti, int) or kapasiteetti < 1:
            raise ValueError(
                "Kapasiteetin tulee olla positiivinen kokonaisluku.")
        if not isinstance(kasvatuskoko, int) or kasvatuskoko < 1:
            raise ValueError(
                "Kasvatuskoon tulee olla positiivinen kokonaisluku.")

        self.kapasiteetti = kapasiteetti
        self.kasvatuskoko = kasvatuskoko
        self.alkiot = self._luo_lista(self.kapasiteetti)
        self.alkioiden_maara = 0

    def kuuluu(self, luku):
        """Tarkistaa, kuuluuko luku joukkoon."""
        return luku in self.alkiot[:self.alkioiden_maara]

    def lisaa(self, luku):
        """Lisää luvun joukkoon, jos se ei jo kuulu joukkoon."""
        if not self.kuuluu(luku):
            if self.alkioiden_maara >= len(self.alkiot):
                self._kasvata_taulukkoa()
            self.alkiot[self.alkioiden_maara] = luku
            self.alkioiden_maara += 1
            return True
        return False

    def poista(self, luku):
        """Poistaa luvun joukosta, jos se löytyy."""
        try:
            indeksi = self.alkiot.index(luku, 0, self.alkioiden_maara)
            for i in range(indeksi, self.alkioiden_maara - 1):
                self.alkiot[i] = self.alkiot[i + 1]
            self.alkioiden_maara -= 1
            self.alkiot[self.alkioiden_maara] = 0  # Nollaa viimeinen arvo
            return True
        except ValueError:
            return False

    def mahtavuus(self):
        """Palauttaa joukossa olevien alkioiden määrän."""
        return self.alkioiden_maara

    def to_int_list(self):
        """Palauttaa listan joukon alkioista."""
        return self.alkiot[:self.alkioiden_maara]

    @staticmethod
    def yhdiste(joukko1, joukko2):
        """Luo joukon, joka sisältää kahden joukon yhdistelmän."""
        tulos = IntJoukko()
        for luku in joukko1.to_int_list() + joukko2.to_int_list():
            tulos.lisaa(luku)
        return tulos

    @staticmethod
    def leikkaus(joukko1, joukko2):
        """Luo joukon, joka sisältää vain kummassakin joukossa esiintyvät alkiot."""
        tulos = IntJoukko()
        for luku in joukko1.to_int_list():
            if joukko2.kuuluu(luku):
                tulos.lisaa(luku)
        return tulos

    @staticmethod
    def erotus(joukko1, joukko2):
        """Luo joukon, joka sisältää ensimmäisen joukon alkiot ilman toisen joukon alkioita."""
        tulos = IntJoukko()
        for luku in joukko1.to_int_list():
            if not joukko2.kuuluu(luku):
                tulos.lisaa(luku)
        return tulos

    def _kasvata_taulukkoa(self):
        """Kasvattaa sisäisen listan kokoa uudelleenkopioinnilla."""
        uusi_koko = len(self.alkiot) + self.kasvatuskoko
        uusi_lista = self._luo_lista(uusi_koko)
        for i in range(self.alkioiden_maara):
            uusi_lista[i] = self.alkiot[i]
        self.alkiot = uusi_lista

    def __str__(self):
        """Palauttaa joukon merkkijonoesityksen."""
        return "{" + ", ".join(map(str, self.to_int_list())) + "}"
