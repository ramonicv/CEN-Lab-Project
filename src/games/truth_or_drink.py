"""Truth or Drink game implementation"""

from typing import List
from src.core.game_base import GameBase
from src.core.player import Player


class TruthOrDrink(GameBase):
    """Truth or Drink game"""
    
    def __init__(self, players: List[Player]):
        super().__init__(players, "Truth or Drink")
    
    def play(self):
        """Placeholder for Truth or Drink gameplay"""
        print(f"\n{'=' * 60}")
        print(f"{self.name.upper()}")
        print(f"{'=' * 60}")
        print("\n[The Truth or Drink game would play here...]")
        print("\nRules:")
        print("  - Players take turns answering personal questions")
        print("  - Answer truthfully or take a drink!")
        print(f"\n{'=' * 60}\n")
        input("Press Enter to return to menu...")