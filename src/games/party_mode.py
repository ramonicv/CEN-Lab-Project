"""Party Mode - mixed games implementation"""

from typing import List
from src.core.game_base import GameBase
from src.core.player import Player


class PartyMode(GameBase):
    """Party Mode - mixed games"""
    
    def __init__(self, players: List[Player]):
        super().__init__(players, "Party Mode")
    
    def play(self):
        """Placeholder for Party Mode gameplay"""
        print(f"\n{'=' * 60}")
        print(f"{self.name.upper()}")
        print(f"{'=' * 60}")
        print("\n[The Party Mode would play here...]")
        print("\nRules:")
        print("  - Mix of all games!")
        print("  - Random game selection")
        print("  - Keep the energy high!")
        print(f"\n{'=' * 60}\n")
        input("Press Enter to return to menu...")