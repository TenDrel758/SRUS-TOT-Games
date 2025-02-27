class Player:
    """A class to represent a player."""

    def __init__(self, uid: str, name: str):
        """Initialize a player instance."""
        self.__uid = uid        #Private var for unique ID
        self.__name = name      #Private var for player name

    @property
    def uid(self) -> str:
        """Return the unique ID of the player."""
        return self.__uid

    @property
    def name(self) -> str:
        """Return the name of the player."""
        return self.__name

    def __str__(self) -> str:
        """Return a string representation of the player."""
        return f"Player(ID: {self.uid}, Name: {self.name})"

