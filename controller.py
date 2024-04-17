from game_state import GameState
from view import GameView, TextualView
import color_view

class GameController:
    state: GameState
    view: GameView

    def __init__(self, initial_inputs=None, names=None, target=None) -> None:
        names = names or self.__get_names()
        self.state = GameState(names, target)
        self.view = color_view.ColorView()
        self.initial_inputs = initial_inputs

    def __get_input(self):
        if self.initial_inputs:
            return str(self.initial_inputs.pop())
        return input(f"Enter your move... ").strip()

    def __get_names(self):
        return input("Enter the names of the players, separated by spaces: ").strip().split(" ")

    def play(self):
        while not self.state.is_game_over():
            self.view.display(self.state)
            move = self.__get_input()
            try:
                move = self.state.apply_move(move)
                self.state.move_history.append(move)
            except Exception as e:
                print(f"invalid move [{move}] {e}")

        self.view.display_game_over(self.state)
