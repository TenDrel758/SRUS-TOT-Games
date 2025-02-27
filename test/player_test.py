import unittest
from app.player import Player

class TestPlayer(unittest.TestCase):

    def setUp(self):
        """initialising a Player object"""
        self.player = Player("123", "Ten")

    def test_uid_property(self):
        """testing the uid property"""
        self.assertEqual(self.player.uid, "123")

    def test_name_property(self):
        """testing the name property"""
        self.assertEqual(self.player.name, "Ten")

if __name__ == '__main__':
    """main function"""
    unittest.main()