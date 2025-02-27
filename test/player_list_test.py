import unittest
from app.player_list import PlayerList
from app.player import Player

class TestPlayerList(unittest.TestCase):
    """testing the PlayerList class"""

    def setUp(self):
        """Set up PlayerList instance for testing"""
        self.player_list = PlayerList()

    def test_is_empty_on_creation(self):
        """Test that the PlayerList is empty on creation"""
        self.assertTrue(self.player_list.is_empty())

    def test_insert_at_head_when_not_empty(self):

        player1 = Player("123", "Ten")
        self.player_list.insert_at_head(player1)

        player2 = Player("456", "Drel")
        self.player_list.insert_at_head(player2)

        self.assertEqual(self.player_list.__head.player.name, "Drel")
        self.assertEqual(self.player_list.__head.next.player.name, "Ten")

    if __name__ == '__main__':
        unittest.main()