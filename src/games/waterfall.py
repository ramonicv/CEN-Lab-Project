"""Waterfall card game implementation"""

from typing import List
from src.core.game_base import GameBase
from src.core.player import Player


class Waterfall(GameBase):
    """Waterfall card game"""
    
    def __init__(self, players: List[Player]):
        super().__init__(players, "Waterfall")
    
    def play(self):
        """Placeholder for Waterfall gameplay"""
        print(f"\n{'=' * 60}")
        print(f"{self.name.upper()}")
        print(f"{'=' * 60}")
        print("\n[The Waterfall card game would play here...]")
        print("\nRules:")
        print("  - Draw cards, each has a rule")
        print("  - Examples: Ace = Waterfall, King = Make a Rule")
        print("  - Follow the rules or drink!")
        print(f"\n{'=' * 60}\n")
        input("Press Enter to return to menu...")