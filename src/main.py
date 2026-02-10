"""Chupi - Party Games Console Application
Main entry point for Phase 1 (Console Prototype)
"""

from src.core.player import Player
from src.games import (
    TruthOrDrink,
    MostLikely,
    DareRoulette,
    Imposter,
    Waterfall,
    PartyMode
)

def get_players() -> list:
    """Get player names from user input
    
    Returns:
        List of Player objects
    """
    
    # Initialize num_players 
    num_players = 0

    while num_players < 2 or num_players > 10:
        try:
            num_players = int(input("\nHow many players? (2-10): "))
            if num_players < 2 or num_players > 10:
                print("Please enter a number between 2 and 10")
        except ValueError:
            print("Please enter a valid number")
            num_players = 0 # keep loop going
    
    players = []
    print()
    for i in range(num_players):
        name = input(f"   Player {i+1} name: ").strip()
        while name == "":
            print("   Name cannot be empty!")
            name = input(f"   Player {i+1} name: ").strip()
        players.append(Player(name))
    
    return players


def show_game_menu():
    """Display game selection menu
    
    Returns:
        User's game choice as string
    """
    menu = """
    Select a game:

    1. Truth or Drink
       Answer personal questions or take a drink

    2. Who's Most Likely To
       Vote on who's most likely to do something

    3. Dare Roulette
       Random dares with escalating difficulty

    4. Imposter
       Find the imposter among the group

    5. Waterfall
       Classic drinking card game

    6. Party Mode
       Mix of all games

    Q. Quit
    """

    print(menu)
    
    choice = input("Enter your choice (1-6 or Q): ").strip().upper()
    while choice not in ['1', '2', '3', '4', '5', '6', 'Q']:
        print("Invalid choice..")
        choice = input("Please enter a valid choice (1-6 or Q): ").strip().upper()
    return choice


def main():
    """Main application loop"""
    print("\nWelcome to Chupi!")
    
    # Get players
    players = get_players()
    
    print(f"\nPlayers: {', '.join(p.name for p in players)}")
    
    # Game selection mapping
    games = {
        '1': TruthOrDrink,
        '2': MostLikely,
        '3': DareRoulette,
        '4': Imposter,
        '5': Waterfall,
        '6': PartyMode
    }
    
    # initialize choice variable
    choice = ''
    
    # Game loop
    while choice != 'Q' or choice != 'q':
        choice = show_game_menu()
        
        if choice == 'Q':
            break
        
        # Create and play the selected game
        game_class = games[choice]
        game = game_class(players)
        game.play()
        
        # Ask if they want to play another game
        play_again = input("\nPlay another game? (Y/N): ").strip().upper()
        if play_again != 'Y':
            break


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print()
    except Exception as e:
        print(f"\nAn error occurred: {e}")