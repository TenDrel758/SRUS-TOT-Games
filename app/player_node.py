"""
Player Node class.
    Author: Tendrel Ongmo Tshering
    Student ID: 20149664
    Description: A class to represent a node in a doubly linked list of players.
    Date: 2025-02-28
    File: player_node.py
"""

#app/player_node.py
class PlayerNode:
    """A node for a double linked list holding player instances."""

    def __init__(self, player):
        """Initialize a player node with a player instance."""
        self.__player = player
        self.__next = None
        self.__prev = None

    @property
    def player(self):
        """Get player instance."""
        return self.__player

    @property
    def next(self):
        """Get next node."""
        return self.__next

    @next.setter
    def next(self, next_node):
        """Set next node."""
        self.__next = next_node

    @property
    def prev(self):
        """Get previous node."""
        return self.__prev

    @prev.setter
    def prev(self, prev_node):
        """Set previous node."""
        self.__prev = prev_node

    @property
    def key(self):
        """Return player uid as key"""
        return self.__player.uid

    @property
    def __str__(self):
        """Return string representation of player node."""
        return f"PlayerNode(uid={self.key}, player_name={self.player.name})"

    @player.setter
    def player(self, value):
        self.player = value
