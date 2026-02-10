"""Who's Most Likely To game implementation"""

from typing import List
from src.core.game_base import GameBase
from src.core.player import Player


class MostLikely(GameBase):
    """Who's Most Likely To game"""
    
    def __init__(self, players: List[Player]):
        super().__init__(players, "Who's Most Likely To")
    
    def play(self):
        """Placeholder for Most Likely gameplay"""
        print(f"\n{'=' * 60}")
        print(f"{self.name.upper()}")
        print(f"{'=' * 60}")
        print("\n[The Who's Most Likely To game would play here...]")
        print("\nRules:")
        print("  - Read a prompt (e.g., 'Who's most likely to sleep through an alarm?')")
        print("  - Everyone points to who they think it is")
        print("  - Person with most votes drinks!")
        print(f"\n{'=' * 60}\n")
        input("Press Enter to return to menu...")