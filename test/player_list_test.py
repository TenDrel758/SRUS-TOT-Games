"""
Player List Test.
    Author: Tendrel Ongmo Tshering
    Student ID: 20149664
    Description: A test for PlayerList class.
    Date: 2025-02-28
    File: player_list_test.py
    Refrences: https://www.geeksforgeeks.org/doubly-linked-list-set-2-insert-in-between/
               https://www.youtube.com/watch?v=0BTZB5DU2OE&t=0s
               https://www.youtube.com/watch?v=w-fnG4LIU_0&t=0s
               https://www.youtube.com/watch?v=galDq38nlWg&t=0s
               https://www.youtube.com/watch?v=LrCAokPC12g&t=0s
"""

# test/player_list_test.py
import io
import unittest

from contextlib import redirect_stdout
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
        print("New player inserted at head", self.player_list)

    def test_insert_at_head_when_empty(self):
        """Test inserting a player node when list is empty"""
        self.player_list.insert_at_head(Player("123", "Ten"))
        print("New player inserted", self.player_list)

    def test_get_tail_player_when_empty(self):
        """Test getting the tail player when list is empty"""
        self.assertIsNone(self.player_list.get_tail_player())
        print("The tail is: ", self.player_list.get_tail_player())

    def test_get_tail_player_when_not_empty(self):
        """Test getting the tail player when list is not empty"""
        player = Player("123", "Ten")
        self.player_list.insert_at_head(player)
        self.assertEqual(self.player_list.get_tail_player(), player)
        print("The tail is: ", self.player_list.get_tail_player())

    def test_insert_at_tail_when_empty(self):
        """Test inserting a player node when list is empty"""
        self.player_list.insert_at_tail(Player("123", "Ten"))
        print("New player inserted ", self.player_list)

    def test_insert_at_tail_when_not_empty(self):
        """Test inserting a player node when list is not empty"""
        self.player_list.insert_at_head(Player("123", "Ten"))
        self.player_list.insert_at_tail(Player("456", "Jane"))
        print("New player inserted at tail ", self.player_list)

    def test_delete_from_head(self):
        players = [Player("123", "Ten"), Player("456", "Jane")]
        self.player_list.insert_at_head(players[0])
        self.player_list.insert_at_head(players[1])

        deleted_player = self.player_list.delete_from_head()
        print("No player at current node pointing to head ", deleted_player)
        print("The head is: ", players[1])

    def test_delete_from_tail(self):
        players = [Player("123", "Ten"), Player("456", "Jane")]
        self.player_list.insert_at_tail(players[0])
        self.player_list.insert_at_tail(players[1])

        self.player_list.delete_from_tail()
        print("The deleted player from tail is: ", players[0])


    def test_delete_by_key(self):
        players = [Player("123", "Ten"), Player("456", "Jane")]
        self.player_list.insert_at_head(players[0])
        self.player_list.insert_at_head(players[1])

        deleted_player = self.player_list.delete_by_key("123")
        print("The deleted player for uid given is ",deleted_player)
        print("The current player is: ", players[1])

        not_found = self.player_list.delete_by_key("789")
        print("The player for given uid: ", not_found, "is not found")

    def test_display_empty_list(self):
        """Test displaying the list when it is empty"""
        f = io.StringIO()
        with redirect_stdout(f):            #Capture printed output
            self.player_list.display()
        print("The list is empty\n")

    def test_display_when_list_forward(self):
        """Test displaying the list when it is forward"""
        players = [Player("123", "Ten"), Player("456", "Jane")]
        self.player_list.insert_at_head(players[0])
        self.player_list.insert_at_head(players[1])

        with redirect_stdout(io.StringIO()) as f:
            self.player_list.display(forward=True)
            print(f.getvalue().strip())

        expected_output = "The list is showing player from head to tail:\n"
        expected_output += "123 - Ten\n"
        expected_output += "456 - Jane\n"

    def test_display_when_list_backward(self):
        """Test displaying the list when it is backward"""
        players = [Player("123", "Ten"), Player("456", "Jane")]
        self.player_list.insert_at_tail(players[0])
        self.player_list.insert_at_tail(players[1])

        with redirect_stdout(io.StringIO()) as f:
            self.player_list.display(forward=False)
            print(f.getvalue().strip())

        expected_output = "The list is showing player from tail to head:\n"
        expected_output += "456 - Jane\n"
        expected_output += "123 - Ten\n"

if __name__ == '__main__':
    """main function"""
    unittest.main()
