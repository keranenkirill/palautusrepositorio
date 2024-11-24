import unittest
from unittest.mock import Mock, ANY
from kauppa import Kauppa
from viitegeneraattori import Viitegeneraattori
from varasto import Varasto
from tuote import Tuote


class TestKauppa(unittest.TestCase):
    def setUp(self):
        self.pankki_mock = Mock()
        self.viitegeneraattori_mock = Mock()
        self.viitegeneraattori_mock.uusi.return_value = 42
        self.varasto_mock = Mock()
        self.kauppa = Kauppa(
            self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)

    def test_ostoksen_jalkeen_pankin_metodia_tilisiirto_kutsutaan(self):
        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10

        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)

        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with(
            "pekka", 42, "12345", "33333-44455", 5)

    def test_ostoksen_jalkeen_pankin_metodia_tilisiirto_kutsutaan_oikeilla_parametreilla(self):
        # Määritellään varaston metodien käyttäytyminen
        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10

        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)

        # Side effectit käyttöön mockille
        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        # Suoritetaan testin toiminnot
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        # Varmistetaan oikeat parametrit
        self.pankki_mock.tilisiirto.assert_called_with(
            "pekka", 42, "12345", "33333-44455", 5
        )

    def test_kahden_eri_tuotteen_ostoksen_jalkeen_tilisiirto_kutsutaan_oikeilla_parametreilla(self):
        def varasto_saldo(tuote_id):
            return 10 if tuote_id in [1, 2] else 0

        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)
            if tuote_id == 2:
                return Tuote(2, "leipä", 3)

        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with(
            "pekka", 42, "12345", "33333-44455", 8)

    def test_kahden_saman_tuotteen_ostoksen_jalkeen_tilisiirto_kutsutaan_oikeilla_parametreilla(self):
        def varasto_saldo(tuote_id):
            return 10

        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)

        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with(
            "pekka", 42, "12345", "33333-44455", 10)

    def test_tuotteen_joka_on_varastossa_ja_loppuneen_tuotteen_ostoksen_jalkeen_tilisiirto_kutsutaan_oikeilla_parametreilla(self):
        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10  # Tuote 1 on varastossa
            if tuote_id == 2:
                return 0   # Tuote 2 on loppu

        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)
            if tuote_id == 2:
                return Tuote(2, "leipä", 3)

        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with(
            "pekka", 42, "12345", "33333-44455", 5)

    def test_aloita_asiointi_nollaa_edellisen_ostoksen_tiedot(self):
        # Määritellään varaston metodien käyttäytyminen
        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10
            if tuote_id == 2:
                return 5

        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)
            if tuote_id == 2:
                return Tuote(2, "leipä", 3)

        # Side effectit käyttöön mockille
        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        # Ensimmäinen ostos
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)  # Maitoa hintaan 5
        self.kauppa.tilimaksu("pekka", "12345")

        # Varmistetaan ensimmäisen tilisiirron oikeat tiedot
        self.pankki_mock.tilisiirto.assert_called_with(
            "pekka", 42, "12345", "33333-44455", 5
        )

        # Aloitetaan uusi asiointi
        self.kauppa.aloita_asiointi()

        # Lisätään uusi tuote koriin
        self.kauppa.lisaa_koriin(2)  # Leipää hintaan 3
        self.kauppa.tilimaksu("arto", "67890")

        # Varmistetaan, että toinen tilisiirto ei sisällä edellisen ostoksen hintaa
        self.pankki_mock.tilisiirto.assert_called_with(
            "arto", 42, "67890", "33333-44455", 3
        )

    def test_poista_korista_palauttaa_tuotteen_varastoon(self):
        def varasto_saldo(tuote_id):
            return 10

        def varasto_hae_tuote(tuote_id):
            return Tuote(tuote_id, "tuote", 1)

        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.poista_korista(1)

        self.assertEqual(self.varasto_mock.palauta_varastoon.call_count, 1)
        self.varasto_mock.palauta_varastoon.assert_called_with(
            Tuote(1, "tuote", 1))

    def test_uusi_viitenumero_jokaiselle_maksutapahtumalle(self):
        def varasto_saldo(tuote_id):
            return 10

        def varasto_hae_tuote(tuote_id):
            return Tuote(tuote_id, "tuote", 1)

        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        self.viitegeneraattori_mock.uusi.assert_called_once()

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("arto", "54321")

        self.viitegeneraattori_mock.uusi.assert_called_with()
