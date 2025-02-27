# test.player_list_test.py
import unittest
from app.player_list import PlayerList
from app.player import Player

class TestPlayerList(unittest.TestCase):
    """Testing the PlayerList class"""

    def setUp(self):
        """Set up PlayerList instance for testing"""
        self.player_list = PlayerList()

    def test_is_empty_on_creation(self):
        """Test that the PlayerList is empty on creation"""
        self.assertTrue(self.player_list.is_empty())

    def test_insert_at_head_when_not_empty(self):
        """Test inserting a player node when list is not empty"""
        player = Player("123", "Ten")
        self.player_list.insert_at_head(player)
        self.assertFalse(self.player_list.is_empty())
        self.player_list.insert_at_head(player.name)

    def test_insert_at_head_when_empty(self):
        """Test inserting a player node when list is empty"""
        self.player_list.insert_at_head(Player("123", "Ten"))

    def test_get_tail_player_when_empty(self):
        """Test getting the tail player when list is empty"""
        self.assertIsNone(self.player_list.get_tail_player())

    def test_get_tail_player_when_not_empty(self):
        """Test getting the tail player when list is not empty"""
        player = Player("123", "Ten")
        self.player_list.insert_at_head(player)
        self.assertEqual(self.player_list.get_tail_player(), player)

    def test_insert_at_tail(self):
        """Test inserting a player node at the tail of the list"""
        player = Player("123", "Ten")
        self.player_list.insert_at_tail(player)

if __name__ == '__main__':
    """main function"""
    unittest.main()