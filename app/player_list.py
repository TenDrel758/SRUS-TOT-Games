#app/player_list.py
from app.player_node import PlayerNode


class PlayerList:
    """A class to represent a doubly linked list of players."""

    def __init__(self):
        """Private var to point to the head of the list"""
        self.__head = None

    def is_empty(self) -> bool:
        """Returns True if the list is empty, False otherwise"""
        return self.__head is None

    def insert_at_head(self, player):
        """Insert a player at the head of the list"""
        new_node = PlayerNode(player)

        if self.is_empty():
            """If the list is empty, set the head to the new player"""
            self.__head = new_node

        else:
            """If the list is not empty, insert the new player after the head"""
            new_node.next = self.__head     #Point new node to the current head
            self.__head.prev = new_node     #Point current head's prev to new node
            self.__head = new_node          #Update the head to the new node

