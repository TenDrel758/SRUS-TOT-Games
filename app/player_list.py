#app/player_list.py
from app.player_node import PlayerNode


class PlayerList:
    """A class to represent a doubly linked list of players."""

    def __init__(self):
        """Private var to point to the head of the list"""
        self.__head = None      #Private var for head of list
        self.__tail = None      #Private var for end of list

    def is_empty(self) -> bool:
        """Returns True if the list is empty, False otherwise"""
        return self.__head is None

    def insert_at_head(self, player):
        """Insert a player at the head of the list"""
        new_node = PlayerNode(player)       #Create a new PlayerNode

        if self.is_empty():
            """If the list is empty, set the head to the new player"""
            self.__head = new_node      #Head to point to new node
            self.__tail = new_node      #tail to point to new node

        else:
            """If the list is not empty, insert the new player after the head"""
            new_node.next = self.__head     #Point new node to the current head
            self.__head.prev = new_node     #Point current head's prev to new node
            self.__head = new_node          #Update the head to the new node

    def get_tail_player(self):
        """Return the player at the tail of the list"""
        return self.__tail.player if self.__tail else None

    def insert_at_tail(self, player):
        """Insert a player at the tail of the list"""
        new_node = PlayerNode(player)

        if self.is_empty():
            """If the list is empty, set the head and tail to the new player"""
            self.__head = new_node
            self.__tail = new_node

        else:
            new_node.prev = self.__tail     #Point the new node's previous to the current tail
            self.__tail.next = new_node     #Link the current tail's next to the new node
            self.__tail = new_node          #Update the tail to new node

    def delete_from_head(self):
        """Delete the player at the head of the list"""
        if self.is_empty():
            return None                     #Nothing to delete

        removed_node = self.__head          #Keep reference to node to remove

        if self.__head == self.__tail:      #Only one node in the list
            self.__head = None
            self.__tail = None
        else:
            self.__head = self.__head.next  #Move Head to the next node
            self.__head.prev = None         #Remove reference from the new head's prev node

        return removed_node.player          #Return the deleted player

    def delete_from_tail(self):
        """Delete the player at the tail of the list"""
        if self.is_empty():
            return None                     #Nothing to delete

        removed_node = self.__tail          #Keep reference to the node to remove

        if self.__head == self.__tail:      #Only one node in the list
            self.__head = None
            self.__tail = None
        else:
            self.__tail = self.__tail.prev  #Move tail to the prev node
            self.__tail.next = None         #Remove reference from the new tail's next node

        return removed_node.player          #Return the deleted player