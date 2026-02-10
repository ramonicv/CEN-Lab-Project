"""Base class for all Chupi games"""

from typing import List
from src.core.player import Player


class GameBase:
    """Base class for all games
    
    Provides common functionality that all games share:
    - Player management
    - Turn tracking
    - Game name
    """
    
    def __init__(self, players: List[Player], name: str):
        """Initialize a game
        
        Args:
            players: List of Player objects
            name: Name of the game
        """
        if not players:
            raise ValueError("At least one player is required")
        
        self.players = players
        self.name = name
        self.current_turn = 0
    
    def get_current_player(self) -> Player:
        """Get the player whose turn it is"""
        return self.players[self.current_turn % len(self.players)]
    
    def next_turn(self):
        """Move to the next player's turn"""
        self.current_turn += 1
    
    def play(self):
        """Main game loop - must be implemented by subclasses"""
        raise NotImplementedError("Subclasses must implement play() method")