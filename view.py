from game_state import GameState


class GameView:

    def display(self, state: GameState):
        pass

    def display_game_over(self, state: GameState):
        pass


class TextualView(GameView):

    def display(self, state: GameState):
        print()
        print(f"Player: {state.current_player.name}")
        print(f"Target: {state.target}")
        print(f"Current Num: {state.current_nums}")
        print(f"Player's Best Num: {state.current_player.best_number}")
        print(f"Move History: {''.join(str(x) for x in state.move_history)}")
        print(f"Remaining ints: {state.current_player.remaining_digits}")
        print(f"Remaining ops: {state.current_player.remaining_ops}")
        print("Current ops: ", ", ".join(str(x) for x in state.current_ops))

    def display_game_over(self, state: GameState):
        winner = state.winner
        print(
            f"\nGame over! Winner is {winner} with the number {winner.best_number}")
