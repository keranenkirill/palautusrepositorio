from pankki import Pankki
from viitegeneraattori import Viitegeneraattori
from kauppa import Kauppa


def main():
    my_net_bank = Pankki()
    viitteet = Viitegeneraattori()
    kauppa = Kauppa(my_net_bank, viitteet)

    kauppa.aloita_ostokset()
    kauppa.lisaa_ostos(5)
    kauppa.lisaa_ostos(7)
    kauppa.maksa("1111")


if __name__ == "__main__":
    main()
