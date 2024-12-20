# "Muistava tekoäly"
class TekoalyParannettu:
    def __init__(self, muistin_koko):
        self._muisti = [None] * muistin_koko
        self._vapaa_muisti_indeksi = 0

    def aseta_siirto(self, siirto):
        # jos muisti täyttyy, unohdetaan viimeinen alkio
        if self._vapaa_muisti_indeksi == len(self._muisti):
            for i in range(1, len(self._muisti)):
                self._muisti[i - 1] = self._muisti[i]

            self._vapaa_muisti_indeksi = self._vapaa_muisti_indeksi - 1

        self._muisti[self._vapaa_muisti_indeksi] = siirto
        self._vapaa_muisti_indeksi = self._vapaa_muisti_indeksi + 1

    def anna_siirto(self):
        if self._vapaa_muisti_indeksi == 0 or self._vapaa_muisti_indeksi == 1:
            return "k"

        viimeisin_siirto = self._muisti[self._vapaa_muisti_indeksi - 1]
        laskuri = {"k": 0, "p": 0, "s": 0}

        for i in range(self._vapaa_muisti_indeksi - 1):
            if self._muisti[i] == viimeisin_siirto:
                seuraava = self._muisti[i + 1]
                laskuri[seuraava] += 1

        return "p" if laskuri["k"] >= max(laskuri.values()) else \
               "s" if laskuri["p"] >= max(laskuri.values()) else "k"

        # Tehokkaampiakin tapoja löytyy, mutta niistä lisää
        # Johdatus Tekoälyyn kurssilla!
