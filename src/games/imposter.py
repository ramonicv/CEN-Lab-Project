"""Imposter game implementation"""

from typing import List
from src.core.game_base import GameBase
from src.core.player import Player


class Imposter(GameBase):
    """Imposter game"""
    
    def __init__(self, players: List[Player]):
        super().__init__(players, "Imposter")
    
    def play(self):
        """Placeholder for Imposter gameplay"""
        print(f"\n{'=' * 60}")
        print(f"{self.name.upper()}")
        print(f"{'=' * 60}")
        print("\n[The Imposter game would play here...]")
        print("\nRules:")
        print("  - One player is secretly the imposter")
        print("  - Everyone gets the same word except the imposter")
        print("  - Guess who the imposter is!")
        print("  - Wrong guess? Drink!")
        print(f"\n{'=' * 60}\n")
        input("Press Enter to return to menu...")