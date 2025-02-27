class PlayerNode:
    """A node for a double linked list holding player instances."""

    def __init__(self):
        self.__player = None
        self.__next = None
        self.__prev = None

    def init(self, player):
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

    @property
    def prev(self):
        """Get previous node."""
        return self.__prev

    @next.setter
    def next(self, node):
        """Set next node."""
        self.__next = node

    @prev.setter
    def prev(self, node):
        """Set previous node."""
        self.__prev = node

    @property
    def key(self):
        """return player uid as key"""
        return self.__player.__uid        #assume player has uid property

    @property
    def __str__(self):
        """return string representation of player node."""
        return f"PlayerNode(uid={self.key}, player_name={self.player.name})"

    @player.setter
    def player(self, value):
        self.player = value

#draft needs more work?