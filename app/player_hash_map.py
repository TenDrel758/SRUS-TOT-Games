# app/player_hash_map.py
from app.player_list import PlayerList
from app.player import Player


class PlayerHashMap:
    SIZE = 10  # Define the size of the hash map

    def __init__(self):
        """Initialize the hash map with separate PlayerList instances."""
        self.hashmap = [PlayerList() for _ in range(self.SIZE)]  # Create distinct PlayerList objects

    def get_index(self, key: str | Player) -> int:
        """Calculate the index of the hash map for the given key."""
        if isinstance(key, Player):
            return hash(key) % self.SIZE
        else:
            return hash(key) % self.SIZE

    def __setitem__(self, key: str, name: str) -> None:
        """Add or update a player in the hash map."""
        player = Player(key, name)
        index = self.get_index(key)
        self.player_list = self.hashmap[index]

        #check if player in list
        existing_player = self.player_list.get_tail_player()
        if existing_player is not None and existing_player.uid == key:
            existing_player.name = name
        else:
            self.player_list.insert_at_tail(player)

    def __getitem__(self, key: str) -> Player:
        """Retrieve a player's name from the hash map."""
        index = self.get_index(key)
        self.player_list = self.hashmap[index]
        current_player = self.player_list.get_tail_player(key)

        while current_player:
            if current_player.uid == key:
                return current_player
            current_player = current_player.prev
        raise KeyError(f"Player with key '{key}' not found.")

    def __delitem__(self, key: str) -> None:
        """Remove a player from the hash map."""
        index = self.get_index(key)
        self.player_list = self.hashmap[index]
        self.player_list.delete_by_key(key)


    def __len__(self) -> int:
        """Return the number of players in the hash map."""
        total = 0
        for self.player_list in self.hashmap:
            current_player = self.player_list.get_tail_player()
            while current_player:
                total += 1
                current_player = current_player.prev
        return total

