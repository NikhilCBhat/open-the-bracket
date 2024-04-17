import random
from enum import Enum
from operations import Operations, OPERATIONS_MAP


class State(Enum):
    NEED_OPERATION = "expecting a mathematical operation"
    NEED_NUMBER = "expecting a number"


class Player:
    name: str
    best_number: int = 0

    def __init__(self, name: str) -> None:
        self.name = name
        self.remaining_digits = set(range(10))
        self.remaining_ops = set(OPERATIONS_MAP.keys()) | {'(', ')'}

    def update_best(self, num, target):       
        self.best_number = min((self.best_number, num), key=lambda x: abs(target - x))

    def remove_digit(self, digit):
        if digit not in self.remaining_digits:
            raise ValueError(f"This is not one of {self}'s remaining digits")
        self.remaining_digits.remove(digit)

    def remove_op(self, op):
        if op not in self.remaining_ops:
            raise ValueError(f"This is not one of {self}'s remaining ops")
        self.remaining_ops.remove(op)
        self.remaining_ops.add("+")

    def __str__(self) -> str:
        return self.name


class GameState:
    current_nums = []
    current_ops = []
    move_history = []
    players = []

    def __init__(self, names, target=None) -> None:
        self.target = target or random.randint(10, 1000)
        self.players = [Player(name) for name in names]
        self.num_players = len(self.players)
        self.__setup()

    @property
    def current_player(self):
        return self.players[len(self.move_history) % self.num_players]

    @property
    def winner(self):
        return min(self.players, key=lambda p: abs(p.best_number - self.target))

    def __setup(self):
        self.current_nums.append(0)
        self.current_ops.append(Operations.ADDITION.value)
        self.state = State.NEED_NUMBER

    def __perform_op(self, move):
        self.current_nums[-1] = int(
            self.current_ops[-1].apply(self.current_nums[-1], move))
        self.current_ops[-1] = None
        self.state = State.NEED_OPERATION
        if len(self.current_nums) == 1:
            self.current_player.update_best(self.current_nums[0], self.target)

    def __validate_move_and_state(self, move):
        is_valid_need_number_move = move.isnumeric() or move == "("
        if (self.state == State.NEED_NUMBER) != is_valid_need_number_move:
            raise ValueError(self.state.value)

    def apply_move(self, move: str):
        self.__validate_move_and_state(move)

        if move.isnumeric():
            move = int(move)
            self.current_player.remove_digit(move)
            try:
                self.__perform_op(move)
            except Exception as e:
                self.current_player.remaining_digits.add(move)
                raise e

        elif (op := OPERATIONS_MAP.get(move)):
            self.current_player.remove_op(move)
            self.current_ops[-1] = op
            self.state = State.NEED_NUMBER

            if op.is_unary:
                self.__perform_op(move)

        elif move == "(":
            self.__setup()

        elif move == ")":
            if len(self.current_ops) < 2:
                raise ValueError("No left parenthesis to close")
            self.current_ops.pop()
            self.__perform_op(self.current_nums.pop())

        else:
            raise ValueError("Unknown Error")

        return move

    def is_game_over(self):
        """
        Checks if the game is over by seeing is the target is reached
        or whether any players are out of digits.
        """
        return self.current_nums[0] == self.target or \
            not (any(bool(player.remaining_digits) for player in self.players))
