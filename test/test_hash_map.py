import unittest
import io
from app.player_hash_map import PlayerHashMap


class TestPlayerHashMap(unittest.TestCase):

    def setUp(self):
        """Create a PlayerHashMap instance for testing."""
        self.hash_map = PlayerHashMap()

    def test_add_player(self):
        """Test adding players to the hash map."""
        self.hash_map['001'] = 'Alice'
        self.hash_map['002'] = 'Bob'

        # Verify that the players were added correctly
        self.assertEqual(self.hash_map['001'], 'Alice')
        self.assertEqual(self.hash_map['002'], 'Bob')
        self.assertNotIn(self.hash_map['003'], 'Charlie')

    def test_update_player(self):
        """Test updating an existing player's name."""
        self.hash_map['001'] = 'Alice'
        self.hash_map['001'] = 'Alicia'  # Update Alice's name

        self.assertEqual(self.hash_map['001'], 'Alicia')

    def test_get_nonexistent_player(self):
        """Test retrieving a player that does not exist."""
        with self.assertRaises(KeyError):
            _ = self.hash_map['999']  # Player with UID '999' doesn't exist

    def test_remove_player(self):
        """Test removing a player from the hash map."""
        self.hash_map['001'] = 'Alice'
        self.hash_map['002'] = 'Bob'

        self.hash_map.__delitem__('001')  # Remove Alice
        with self.assertRaises(KeyError):
            _ = self.hash_map['001']  # Should raise KeyError

        self.assertEqual(len(self.hash_map), 1)  # There should be one player left

    def test_remove_nonexistent_player(self):
        """Test removing a player that does not exist."""
        self.hash_map['001'] = 'Alice'

        # Remove a player that doesn't exist should raise an error
        with self.assertRaises(KeyError):
            self.hash_map.__delitem__('999')  # Remove player that is not in the map

    def test_count_players(self):
        """Test to check the count of players in the hash map."""
        self.hash_map['001'] = 'Alice'
        self.hash_map['002'] = 'Bob'
        self.hash_map['003'] = 'Charlie'

        self.assertEqual(len(self.hash_map), 3)

        self.hash_map.__delitem__('002')
        self.assertEqual(len(self.hash_map), 2)  # Check after deletion

    def test_display_with_players(self):
        """Test display method to see if it shows the correct players."""
        self.hash_map['001'] = 'Alice'
        self.hash_map['002'] = 'Bob'

        # Capture the print output
        with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            self.hash_map.display()
            output = mock_stdout.getvalue()

        expected_output = (
                "Index 0:\nNo players in this list.\n" +
                "Index 1:\nNo players in this list.\n" +
                "Index 2:\n  Player UID: 001, Name: Alice\n" +
                "Index 3:\n  Player UID: 002, Name: Bob\n" +
                "Index 4:\nNo players in this list.\n" +
                "Index 5:\nNo players in this list.\n" +
                "Index 6:\nNo players in this list.\n" +
                "Index 7:\nNo players in this list.\n" +
                "Index 8:\nNo players in this list.\n" +
                "Index 9:\nNo players in this list.\n"
        )

        self.assertEqual(output, expected_output)

    def test_add_none_key(self):
        """Test adding a player with a None key."""
        with self.assertRaises(TypeError):
            self.hash_map[None] = 'NoName'  # UID cannot be None

    def test_add_empty_key(self):
        """Test adding a player with an empty string as key."""
        with self.assertRaises(ValueError):
            self.hash_map[''] = 'NoName'  # UID cannot be an empty string


if __name__ == "__main__":
    unittest.main()