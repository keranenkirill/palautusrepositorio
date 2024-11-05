import unittest
from statistics_service import StatisticsService
from player import Player


class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]


class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(PlayerReaderStub())

    def test_search(self):
        player = self.stats.search("Kurri")
        self.assertEqual(str(player), "Kurri EDM 37 + 53 = 90")

    def test_search_no_player(self):
        player = self.stats.search("Koivu")
        self.assertIsNone(player)

    def test_team(self):
        players = self.stats.team("EDM")
        self.assertEqual(len(players), 3)

    def test_top(self):
        players = self.stats.top(2)  # index
        print(players)
        self.assertEqual(str(players[0]), "Gretzky EDM 35 + 89 = 124")
        self.assertEqual(str(players[1]), "Lemieux PIT 45 + 54 = 99")
        self.assertEqual(str(players[2]), "Yzerman DET 42 + 56 = 98")
