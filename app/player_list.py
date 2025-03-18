"""
Player List class.
    Author: Tendrel Ongmo Tshering
    Student ID: 20149664
    Description: A class to represent a doubly linked list of players.
    Date: 2025-02-28
    File: player_list.pyhttps://www.youtube.com/watch?v=LrCAokPC12g&t=0s
    Refrences: https://www.geeksforgeeks.org/doubly-linked-list-set-2-insert-in-between/
               https://www.youtube.com/watch?v=0BTZB5DU2OE&t=0s
               https://www.youtube.com/watch?v=w-fnG4LIU_0&t=0s
               https://www.youtube.com/watch?v=galDq38nlWg&t=0s
               https://www.youtube.com/watch?v=LrCAokPC12g&t=0s
"""

#app/player_list.py
from app.player_node import PlayerNode


class PlayerList:
    """A class to represent a doubly linked list of players."""

    def __init__(self):
        """Private var to point to the head of the list"""
        self.__head = None      #Private var for head of list
        self.__tail = None      #Private var for end of list
        self.__player_dict = {} #Hash map for searching

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
        self.__player_dict[player.uid] = new_node

    def get_tail_player(self,uid):
        """Return the player at the tail of the list"""
        if uid in self.__player_dict:
            return self.__player_dict[uid].player
        return None

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

        self.__player_dict[player.uid] = new_node

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

        del self.__player_dict[removed_node.player.uid]
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

        del self.__player_dict[removed_node.player.uid]
        return removed_node.player          #Return the deleted player

    def delete_by_key(self, key):

        current = self.__head

        """Delete a player by their unique identifier (UID)."""
        if key in self.__player_dict:  # Only proceed if key exists
            current = self.__player_dict[key]
            if current == self.__head:  # If it is the head
                return self.delete_from_head()
            elif current == self.__tail:  # If it is the tail
                return self.delete_from_tail()
            else:  # If it is in the middle
                current.prev.next = current.next
                current.next.prev = current.prev
                del self.__player_dict[key]  # Remove from hash map
                return current.player  # Return the deleted player
        return None  # If not found                                  #If not found

    def display(self, forward=True):
        """Display the players in the list from head -> tail or tail -> head."""
        if self.is_empty():
            print("The list is empty.")
            return

        if forward:
            current = self.__head
            direction = "Head -> Tail"
        else:
            current = self.__tail
            direction = "Tail -> Head"

        print(f"Players in the {direction}:")
        while current:
            print(f"Player: {current.player.name}, UID: {current.player.uid}")
            current = current.next if forward else current.prev