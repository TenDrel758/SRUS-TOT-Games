class PlayerNode:
    """A node for a double linked list holding player instances."""

    def init(self, player):
        self.player = player
        self.next = None
        self.prev = None

    @property
    def player(self):
        """Get player instance."""
        return self.player

    @property
    def next(self):
        """Get next node."""
        return self.next

    @property
    def prev(self):
        """Get previous node."""
        return self.prev

    @next.setter
    def next(self, node):
        """Set next node."""
        self.next = node

    @prev.setter
    def prev(self, node):
        """Set previous node."""
        self.prev = node

    @property
    def key(self):
        """return player uid as key"""
        return self.player.uid        #assume player has uid property

    @property
    def __str__(self):
        """return string representation of player node."""
        return f"PlayerNode(uid={self.key}, player_name={self.player.name})"

    @player.setter
    def player(self, value):
        self.player = value

#draft needs more work?