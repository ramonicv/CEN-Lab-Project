"""Dare Roulette game implementation"""

from typing import List
from src.core.game_base import GameBase
from src.core.player import Player


class DareRoulette(GameBase):
    """Dare Roulette game"""
    
    def __init__(self, players: List[Player]):
        super().__init__(players, "Dare Roulette")
    
    def play(self):
        """Placeholder for Dare Roulette gameplay"""
        print(f"\n{'=' * 60}")
        print(f"{self.name.upper()}")
        print(f"{'=' * 60}")
        print("\n[The Dare Roulette game would play here...]")
        print("\nRules:")
        print("  - Players take turns getting random dares")
        print("  - Complete the dare or take a drink!")
        print("  - Difficulty increases as the game goes on")
        print(f"\n{'=' * 60}\n")
        input("Press Enter to return to menu...")