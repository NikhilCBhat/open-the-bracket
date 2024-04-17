import colorama
from colorama import Fore, Style

from game_state import GameState
from view import GameView

class ColorView(GameView):

    def __init__(self):
        colorama.init(autoreset=True)

    def display(self, state: 'GameState'):
        print(Fore.CYAN + Style.BRIGHT + "=" * 50)
        print(f"Player: {Fore.YELLOW + Style.BRIGHT + state.current_player.name}")
        print(f"Target: {Fore.GREEN + str(state.target)}")
        print(f"Current Numbers: {state.current_nums}")
        print(
            f"{state.current_player.name}'s best number: {state.current_player.best_number}")
        print(
            f"Move History: {Fore.MAGENTA + ''.join(str(x) for x in state.move_history)}")
        print(
            f"Remaining integers: {str(sorted(state.current_player.remaining_digits))}")
        print(
            f"Remaining operations: {', '.join(sorted(state.current_player.remaining_ops))}")
        print(Fore.CYAN + "-" * 50)

    def display_game_over(self, state: 'GameState'):
        winner = state.winner
        print(Fore.GREEN + Style.BRIGHT +
              f"\nGame over! Winner is {winner} with the number {winner.best_number}")
