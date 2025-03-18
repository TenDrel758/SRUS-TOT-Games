"""
Player Test.
    Author: Tendrel Ongmo Tshering
    Student ID: 20149664
    Description: A test for Player class.
    Date: 2025-02-28
    File: player_test.py
"""

#test/player_test.py
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

    def test_hash_function(self):
        player1 = Player('001', 'Alice')
        player2 = Player('002', 'Bob')

        # Check that players with different UIDs have different hashes
        self.assertNotEqual(hash(player1), hash(player2))

        # Check that two players with the same UID have the same hash
        player3 = Player('001', 'Alicia')
        self.assertEqual(hash(player1), hash(player3))

    def test_equality(self):
        player1 = Player('001', 'Alice')
        player2 = Player('001', 'Alicia')
        player3 = Player('002', 'Bob')

        # Same UID should be considered equal
        self.assertEqual(player1, player2)

        # Different UIDs should not be equal
        self.assertNotEqual(player1, player3)

if __name__ == '__main__':
    """main function"""
    unittest.main()