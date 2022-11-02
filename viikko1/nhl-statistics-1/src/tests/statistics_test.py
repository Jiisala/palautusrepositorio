import unittest
from statistics import Statistics, SortBy
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

class TestStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(
            PlayerReaderStub()
        )
    
    def test_init_works_as_expected(self):
        self.assertEqual(self.statistics._players[0].name, "Semenko")
        self.assertEqual(len(self.statistics._players), 5)

    def test_search_works_with_valid_input(self):

        self.assertEqual(self.statistics.search("Kurri"), self.statistics._players[2])

    
    def test_search_returns_none_with_invalid_input(self):

        self.assertIsNone(self.statistics.search("Pallopaa Penttinen"))    
    
    def test_search_by_team_works(self):
        self.assertEqual(len(self.statistics.team("EDM")), 3)
        self.assertEqual(self.statistics.team("PIT")[0].name, "Lemieux")
    
    def test_top_works_as_expected(self):
        self.assertEqual(len(self.statistics.top(3)), 3)
        self.assertEqual(self.statistics.top(3)[0].name, "Gretzky" )

    def test_top_works_as_expected_when_sorted_by_goals(self):

        self.assertEqual(self.statistics.top(3, SortBy.GOALS)[0].name, "Lemieux")

    
    def test_top_works_as_expected_when_sorted_by_assists(self):

        self.assertEqual(self.statistics.top(3, SortBy.ASSISTS)[0].name, "Gretzky")    