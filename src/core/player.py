"""Player management for Chupi games"""


class Player:
    """Represents a player in the game"""
    
    def __init__(self, name: str):
        self.name = name
    
    def __str__(self):
        return self.name
    
    def __repr__(self):
        return f"Player(name='{self.name}')"