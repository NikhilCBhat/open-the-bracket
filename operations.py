import math
from enum import Enum
from typing import Callable
from dataclasses import dataclass


def safe_division(x: int, y: int) -> int:
    if y == 0 or x % y != 0:
        raise ValueError("We only support division by factors.")
    return int(x / y)


@dataclass
class Operation:
    apply: Callable[[int, int], int]
    is_unary: bool
    name: str

    def __str__(self) -> str:
        return self.name


class Operations(Enum):
    MULTIPLICATION = Operation(lambda x, y: x * y, False, "*")
    ADDITION = Operation(lambda x, y: x + y, False, "+")
    DIVISION = Operation(safe_division, False, "/")
    SUBTRACTION = Operation(lambda x, y: x - y, False, "-")
    POWER = Operation(lambda x, y: x ** y, False, "^")
    MODULUS = Operation(lambda x, y: x % y, False, "mod")
    FACTORIAL = Operation(lambda x, _: math.factorial(x), True, "!")
    RIGHT_SHIFT = Operation(lambda x, y: x >> y, False, ">>")
    LEFT_SHIFT = Operation(lambda x, y: x << y, False, "<<")


OPERATIONS_MAP = {o.value.name: o.value for o in Operations}
