import unittest
from app.player_hash_map import PlayerHashMap


class TestPlayerHashMap(unittest.TestCase):

    def setUp(self):
        """Create a PlayerHashMap instance for testing."""
        self.hash_map = PlayerHashMap()

    def test_add_player(self):
        """Test adding players to the hash map."""
        self.hash_map['123'] = 'Ten'
        
        self.assertEqual(len(self.hash_map), 1)
        self.assertEqual(self.hash_map['123'], 'Ten')

    def test_update_player(self):
        """Test updating an existing player's name."""
        self.hash_map['123'] = 'Te'
        self.hash_map['123'] = 'Ten'  # Update Ten's name
    
        self.assertEqual(len(self.hash_map), 1)
        self.assertEqual(self.hash_map['123'], 'Ten')

    def test_get_index(self):
        """Test retrieving an existing player."""
        self.hash_map['123'] = 'Ten'
        retrieved_player = self.hash_map['123']

        self.assertEqual(retrieved_player.uid, '123')
        self.assertEqual(retrieved_player.name, 'Ten')

    def test_delete_player(self):
        """Test deleting a player from the hash map."""
        self.hash_map['123'] = 'Ten'
        self.assertEqual(len(self.hash_map), 1)
        del self.hash_map['123']
        self.assertEqual(len(self.hash_map), 0)

    def test_size_method(self):
        self.assertEqual((len(self.hash_map)), 0)
        self.hash_map['123'] = 'Ten'
        self.assertEqual((len(self.hash_map)), 1)
        self.hash_map['456'] = 'Jane'
        self.assertEqual((len(self.hash_map)), 2)
        del self.hash_map['123']
        self.assertEqual((len(self.hash_map)), 1)

    def test_display_method(self):
        self.hash_map['123'] = 'Ten'
        self.hash_map['456'] = 'Drel'

        try:
            self.hash_map.display()
        except Exception as e:
            self.fail(f"Error occurred during display: {e}")

if __name__ == "__main__":
    unittest.main()